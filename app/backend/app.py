from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd 
import logging as log
import requests
import time
import threading

# Custom modules
from people import Staff, User, Nurse, Patient
import csvdatabase as cdb
from triage import SymptomTriage 
import patient_queue as pq

# Set logger
logger = log.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Initialize core components
patientQ = pq.PatientQueue()
patientQ.build_queue_from_db()
symptom_triage = SymptomTriage()

# Triaging system routes
@app.route('/api/record_symptoms', methods=['POST'])
def record_symptoms():
    data = request.json
    if not data or 'healthCareNumber' not in data or 'symptoms' not in data:
        return jsonify({
            'success': False,
            'message': 'Missing required fields'
        }), 400
    
    patient_id = str(data.get('healthCareNumber'))
    symptoms = data['symptoms']
    
    # Record symptoms and get triage score
    result = symptom_triage.record_symptoms(patient_id, symptoms)
    
    if result['success']:
        # If symptoms were recorded successfully, update patient queue
        if result['score'] is not None:
            # Use the priority from the result instead of calling determine_priority
            priority = result['priority']
            
            # Query the Database for patient info
            u_db = cdb.CSVDatabase('./db/user.csv')
            if u_db.check_value(patient_id, 'hcn'):
                p_info = u_db.get_line_dic(patient_id, 'hcn')
                patient = Patient(
                    hcn=patient_id,
                    name=p_info.get('name'),
                    age=p_info.get('age'),
                    priority=priority,
                    triage_score=result['score'],
                    q_pos=-1
                )
                # Update or add patient to queue
                patientQ.add(patient)
                
                result['queue_updated'] = True
                return jsonify(result), 200
            else:
                result['queue_updated'] = False
                return jsonify(result), 404
    
    return jsonify(result), 400

@app.get('/api/patient_symptoms/<int:patient_id>')
def get_patient_symptoms(patient_id):
    result = symptom_triage.get_patient_history(patient_id)
    
    if result['success']:
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@app.route('/api/login', methods=['POST'])
def staff_login():
    s = Staff('placeholder', 'placeholder')
    return s.login(data=request.json)

@app.route('/api/patient_login', methods=['POST'])
def patient_login():
    u = User('placeholder', 'placeholder', 'placeholder')
    return u.login(data=request.json)

@app.route('/api/add_patient', methods=['POST'])
def add_patient():
    data = request.json
    hcn = str(data.get('healthCareNumber'))
    triage_score = data.get('triageScore')
    
    # Calculate priority using SymptomTriage instance
    priority = symptom_triage.determine_priority(int(triage_score))

    # Query the Database for matching HCN
    u_db = cdb.CSVDatabase('./db/user.csv')
    patient = None
    if u_db.check_value(hcn, 'hcn'):
        p_info = u_db.get_line_dic(hcn, 'hcn')
        patient = Patient(hcn=hcn, name=p_info.get('name'), age=p_info.get('age'), priority=priority, triage_score=triage_score, q_pos=-1)
    
    if patient:
        patientQ.add(patient)
        return jsonify({'message': 'Addition to queue was successful', 'user': hcn}), 200
    else:
        return jsonify({'message': 'Invalid. Patient does not exist'}), 401

@app.route('/api/get_queue_pos', methods=['POST'])
def get_queue_pos():
    data = request.json
    if not data or 'healthCareNumber' not in data:
        return jsonify({
            'message': 'Missing healthcare number',
            'success': False
        }), 400

    hcn = data['healthCareNumber']
    position = patientQ.get_position(hcn)
    
    if position is not None:
        return jsonify({
            'message': 'Queue position found',
            'queue_pos': position,
            'success': True
        }), 200
    else:
        return jsonify({
            'message': 'Patient not found in queue',
            'success': False
        }), 404

@app.route('/api/remove_patient', methods=['POST'])
def remove_patient():
    data = request.json
    if not data or 'healthCareNumber' not in data:
        return jsonify({
            'message': 'Missing healthcare number',
            'success': False
        }), 400

    hcn = str(data['healthCareNumber'])
    # Query the Database for matching HCN
    p_db = cdb.CSVDatabase('./db/patient.csv')
    patient = None
    if p_db.check_value(hcn, 'hcn'):
        patient = Patient(p_info=p_db.get_line_dic(hcn, 'hcn'))
    else:
        return jsonify({
            'message': 'Patient not found in queue',
            'success': False
        }), 404

    if patientQ.remove(patient):
        return jsonify({
            'message': 'Patient removed successfully',
            'success': True
        }), 200
    else:
        return jsonify({
            'message': 'Patient not found in queue',
            'success': False
        }), 404

def heartbeat():
    while True:
        url = "http://localhost:3000"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logger.info(f"Ping to {url} successful: Front end up")
            else:
                logger.error(f"Ping to {url} failed with status code {response.status_code}")
        except requests.ConnectionError:
            logger.error(f"Ping to {url} failed due to connection error")
        time.sleep(5)

def main():
    # Reset log file
    with open('log.txt', 'w'):
        pass
        
    # Configure logging
    log.basicConfig(
        level=log.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            log.FileHandler("log.txt"),
            log.StreamHandler()
        ]
    )

    # Start heartbeat thread
    heartbeat_thread = threading.Thread(target=heartbeat)
    heartbeat_thread.daemon = True
    heartbeat_thread.start()

    # Run Flask app
    app.run(debug=True)
    log.info('Application terminated')

if __name__ == '__main__':
    main()