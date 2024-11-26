# Note: app must be run in root/admin mode (ie: with sudo) for ping

# Import necessary libraries
from contextlib import nullcontext
#from crypt import methods <-- Do not use! Not supported on Windows

from flask import Flask, jsonify, request  # Flask for web framework, jsonify for JSON responses, request to handle incoming data
from flask_cors import CORS  # CORS for handling Cross-Origin Resource Sharing
import pandas as pd 
import logging as log

import requests
import time
import threading

# Custom modules
from people import Staff, User, Nurse, Patient
import csvdatabase as cdb
from triage import determine_priority
import patient_queue as pq


# Set logger
logger = log.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Enable CORS for all routes: allows the API to be accessed from different origins
CORS(app)

# Init queue - Singleton Design Pattern:
patientQ = pq.PatientQueue()
patientQ.build_queue_from_db()

# Define the login route
@app.route('/api/login', methods=['POST'])
def staff_login():
    # Extract JSON data from the request and call Staff object to compute
    s = Staff('placeholder', 'placeholder')
    return s.login(data=request.json)

# Handle Patient User login
@app.route('/api/patient_login', methods=['POST'])
def patient_login():
    # Extract JSON data from the request and call Patient object to compute
    u = User('placeholder', 'placeholder', 'placeholder')
    return u.login(data=request.json)

# Add patient to queue
@app.route('/api/add_patient', methods=['POST'])
def add_patient():
    data = request.json
    hcn = str(data.get('healthCareNumber'))
    triage_score = str(data.get('triageScore'))
    priority = determine_priority(int(triage_score))

    # Query the Database for matching HCN
    u_db = cdb.CSVDatabase('./db/user.csv')
    patient = None
    if u_db.check_value(hcn, 'hcn'):
        p_info = u_db.get_line_dic(hcn, 'hcn')
        patient = Patient(hcn=hcn, name=p_info.get('name'), age=p_info.get('age'), priority=priority, triage_score=triage_score, q_pos="-1")
    # Check if a matching user was found
    if patient:
        # If user found, return success message
        patientQ.add(patient)
        return jsonify({'message': 'Addition to queue was successful', 'user': hcn}), 200
    else:
        # If no user found, return error message
        return jsonify({'message': 'Invalid. Patient does not exist'}), 401

@app.route('/api/remove_patient', methods=['POST'])
def remove_patient():
    data = request.json
    hcn = data.get('healthCareNumber')

    # Query the Database for matching HCN
    p_db = cdb.CSVDatabase('./db/patient.csv')
    patient = None
    if p_db.check_value(hcn, 'hcn'):
        patient = Patient(p_db.get_line_dic(hcn, 'hcn'))

    # Check if a matching user was found
    if patient:
        # If user found, return success message
        patientQ.remove(patient)
        return jsonify({'message': 'Removal successful', 'user': hcn}), 200
    else:
        # If no user found, return error message
        return jsonify({'message': 'Invalid. Patient is not in Q'}), 401

# Get patient's queue position
@app.route('/api/get_queue_pos', methods=['POST'])
def get_queue_pos():
    data = request.json
    hcn = data.get('healthCareNumber')

    # Query the Database for matching HCN
    p_db = cdb.CSVDatabase('./db/patient.csv')
    patient = None
    if p_db.check_value(hcn, 'hcn'):
        patient = Patient(p_db.get_line_dic(hcn, 'hcn'))

    # Check if a matching user was found
    if patient:
        # If user found, return success message
        return jsonify({'message': 'Queue position found', 'queue_pos': patient.q_pos}), 200
    else:
        # If no user found, return error message
        return jsonify({'message': 'Invalid. Patient is not in queue'}), 401

#  Ping localhost every 5 seconds to verify connection.. 
def heartbeat():
    while True:
        url = "http://localhost:3000"  # URL of React app
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logger.info(f"Ping to {url} successful: Front end up")
            else:
                logger.error(f"Ping to {url} failed with status code {response.status_code}. Front end likely down.")
        except requests.ConnectionError:
            logger.error(f"Ping to {url} failed due to connection error. Front end likely down.")
        
        time.sleep(5)  # Sleep for 5 seconds before the next ping
    


def main():
    # Delete existing log
    with open('log.txt', 'w'):
        pass
    # Set up
    log.basicConfig(
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        log.FileHandler("log.txt"),
        log.StreamHandler()  # This logs to the console
    ]
    )

    # Create and start the heartbeat thread
    heartbeat_thread = threading.Thread(target=heartbeat)
    heartbeat_thread.daemon = True  # Set as a daemon so it will be killed once the main thread is dead
    heartbeat_thread.start()

    # Run app:
    app.run(debug=True) # debug flag
    log.info('Ended')

# Run the application if this file is executed directly
if __name__ == '__main__':
    main()
    
    