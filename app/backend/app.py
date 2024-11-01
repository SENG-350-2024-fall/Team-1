# Import necessary libraries
from flask import Flask, jsonify, request  # Flask for web framework, jsonify for JSON responses, request to handle incoming data
from flask_cors import CORS  # CORS for handling Cross-Origin Resource Sharing
import pandas as pd 
import logging as log
import os 

# Set logger
logger = log.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Enable CORS for all routes: allows the API to be accessed from different origins
CORS(app)

# TODO: Update to contain users. PW and user will be user properties.
df = pd.DataFrame({
    'username': ['staff123'],
    'password': ['password']
})

# Define the login route
@app.route('/api/login', methods=['POST'])
def login():
    # Extract JSON data from the request
    data = request.json
    
    # Get username and password from the request data
    username = data.get('username')
    password = data.get('password')
    
    # Query the DataFrame for matching username and password
    user = df[(df['username'] == username) & (df['password'] == password)]
    
    # Check if a matching user was found
    if not user.empty:
        # If user found, return success message
        
        return jsonify({'message': 'Login successful', 'user': username}), 200
    else:
        # If no user found, return error message
        return jsonify({'message': 'Invalid credentials'}), 401
    

# Ping localhost every 5 seconds to verify connection.. todo
def hearbeat():
    hostname = ""


def main():
    log.basicConfig(filename='log.txt', level=log.INFO)
    logger.info('Started')
    app.run(debug=True) # debug flag
    log.info('Ended')

# Run the application if this file is executed directly
if __name__ == '__main__':
    main()
    
    