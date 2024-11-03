# Note: app must be run in root/admin mode (ie: with sudo) for ping

# Import necessary libraries
from contextlib import nullcontext

from flask import Flask, jsonify, request  # Flask for web framework, jsonify for JSON responses, request to handle incoming data
from flask_cors import CORS  # CORS for handling Cross-Origin Resource Sharing
import pandas as pd 
import logging as log

import requests
import time
import threading

# Custom modules
import people as ppl
import csvdatabase as cdb
import triage 
import patient_queue as pq

# Set logger
logger = log.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Enable CORS for all routes: allows the API to be accessed from different origins
CORS(app)

staff_db = cdb.CSVDatabase('./db/staff.csv')

# Define the login route
@app.route('/api/login', methods=['POST'])
def login():
    # Extract JSON data from the request
    data = request.json
    
    # Get username and password from the request data
    username = data.get('username')
    password = data.get('password')
    
    # Query the Database for matching username and password
    user = None
    if staff_db.check_value(username, 'username') and staff_db.check_value(password, 'password'):
        user = staff_db.get_line_dic(username, 'username') # TODO: Make this more secure
    
    # Check if a matching user was found
    if user:
        # If user found, return success message
        
        return jsonify({'message': 'Login successful', 'user': username}), 200
    else:
        # If no user found, return error message
        return jsonify({'message': 'Invalid credentials'}), 401
    

#  Ping localhost every 5 seconds to verify connection.. 
def hearbeat():
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
    log.basicConfig(filename='log.txt', level=log.INFO)
    logger.info('Started')
    # Create and start the heartbeat thread
    heartbeat_thread = threading.Thread(target=hearbeat)
    heartbeat_thread.daemon = True  # Set as a daemon so it will be killed once the main thread is dead
    heartbeat_thread.start()
    # Init queue:
    patientQ = pq.PatientQueue()
    # Run app:
    app.run(debug=True) # debug flag
    log.info('Ended')

# Run the application if this file is executed directly
if __name__ == '__main__':
    main()
    
    