from flask import Flask, jsonify, request  # Flask for web framework, jsonify for JSON responses, request to handle incoming data


import csvdatabase as cdb

staff_db = cdb.CSVDatabase('./db/staff.csv')
user_db = cdb.CSVDatabase('./db/user.csv')

class Staff:

    # Initialize
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def login(self, data):
        # Get username and password from the request data
        username = data.get('username')
        password = data.get('password')

        # Query the Database for matching username and password
        user = None
        if staff_db.check_value(username, 'username') and staff_db.check_value(password, 'password'):
            user = staff_db.get_line_dic(username, 'username')  # TODO: Make this more secure

        # Check if a matching user was found
        if user:
            # If user found, return success message
            return jsonify({'message': 'Login successful', 'user': username}), 200
        else:
            # If no user found, return error message
            return jsonify({'message': 'Invalid credentials'}), 401

# Template Design Pattern
class Doctor(Staff):
    # Initialize
    def __init__(self, name, role, specialty, location):
        super().__init__(name, role)
        self.specialty = specialty
    
class EMT(Staff):
    # Initialize
    def __init__(self, name, role, activeLocation): # Change to some API that returns the active location
        super().__init__(name, role)
        self.activeLocation = activeLocation

class Nurse(Staff):
    # Initialize
    def __init__(self, name, role, location):
        super().__init__(name, role)
        self.location = location



# everything below is very tentative and more brainstorming. demolish as desired.
class User:
    # initialize
    def __init__(self, hcn, name, age):
        self.hcn = hcn
        self.name = name
        self.age = age

    def login(self, data):
        # Get username and password from the request data
        hcn = data.get('healthCareNumber')

        # Query the Database for matching username and password
        user = None
        if user_db.check_value(hcn, 'hcn'):
            user = user_db.get_line_dic(hcn, 'hcn')

        # Check if a matching user was found
        if user:
            # If user found, return success message
            return jsonify({'message': 'Login successful', 'user': hcn}), 200
        else:
            # If no user found, return error message
            return jsonify({'message': 'Invalid credentials'}), 401
        
# User becomes a patient when
# a recommendation is made by MrED
class Patient(User):

    def __init__(self, hcn=None, name=None, age=None, priority=None, triage_score=None, q_pos=None, p_info=None):
        """
        Initializes Patient object
        :param hcn: Health Care Number
        :param name: Name of patient
        :param age: Age of patient
        :param priority: Priority of patient. Either critical, moderate priority, or low priority
        :param triage_score: Most recent triage score of patient
        :param q_pos: Position of patient in queue
        :param p_info: Dictionary containing previous parameters
        """
        if p_info is None:
            super().__init__(hcn, name, age)
            self.priority = priority
            self.triage_score = triage_score
            self.q_pos = q_pos
        else:
            super().__init__(p_info.get('hcn'), p_info.get('name'), p_info.get('age'))
            self.priority = p_info.get('priority')
            self.triage_score = p_info.get('triage_score')
            self.q_pos = p_info.get('q_pos')

    def modify_q_pos(self, new_pos):
        """Update the patient's position in queue"""
        self.q_pos = new_pos
        
    def update(self, queue_data):
        """
        Receive updates about queue changes.
        Updates patient's queue position if they're in the queue.
        
        Args:
            queue_data: List of patients in current queue order
        """
        # Find this patient in the queue
        for position, patient in enumerate(queue_data):
            if patient.name == self.name:  # Using name as identifier
                self.modify_q_pos(position)
                break
        