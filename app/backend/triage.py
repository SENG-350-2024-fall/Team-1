import pandas as pd
from datetime import datetime
import os

class SymptomTriage:
    def __init__(self):
        self.symptoms = {
            "Coughing": 2,
            "Headache": 2,
            "Vomiting/Nausea": 5,
            "Chest Pain": 10,
            "Limb Numbness": 15,
            "Vision Impacted": 5,
            "Hearing Impacted": 3,
            "Shortness of Breath": 15,
            "Fever": 8,
            "Fatigue": 2
        }
        
        self.csv_path = './db/triage.csv'
        self._initialize_csv()

    def _initialize_csv(self):
        """Initialize the triage.csv file if it doesn't exist"""
        if not os.path.exists(self.csv_path):
            df = pd.DataFrame(columns=['patient_id', 'timestamp', 'symptoms', 'total_score'])
            df.to_csv(self.csv_path, index=False)

    def validate_symptoms(self, symptoms_list):
        """Validate that all submitted symptoms exist in our defined set"""
        return all(symptom in self.symptoms for symptom in symptoms_list)

    def calculate_score(self, symptoms_list):
        """Calculate total triage score based on selected symptoms"""
        return sum(self.symptoms[symptom] for symptom in symptoms_list)

    def determine_priority(self, triage_score):
        """
        Determine priority level based on triage score
        
        Args:
            triage_score (int): The calculated triage score
            
        Returns:
            int: Priority level (1-5, where 1 is highest priority)
        """
        if triage_score >= 25:
            return 1  # critical - Immediate attention needed
        elif triage_score >= 15:
            return 2  # moderate
        elif triage_score >= 5:
            return 3  # standard
        else:
            return 4  # non-urgent

    def record_symptoms(self, patient_id, symptoms_list):
        """
        Record patient symptoms and calculate triage score
        
        Args:
            patient_id (str): Patient's health care number
            symptoms_list (list): List of symptoms selected by the patient
            
        Returns:
            dict: Response containing success status, triage score, and priority level
        """
        try:
            # Validate symptoms
            if not self.validate_symptoms(symptoms_list):
                return {
                    'success': False,
                    'message': 'Invalid symptoms provided',
                    'score': None,
                    'priority': None
                }

            # Calculate total score
            total_score = self.calculate_score(symptoms_list)
            
            # Determine priority
            priority = self.determine_priority(total_score)
            
            # Prepare data for CSV
            new_record = {
                'patient_id': patient_id,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'symptoms': '|'.join(symptoms_list),
                'total_score': total_score
            }
            
            # Read existing CSV
            df = pd.read_csv(self.csv_path)
            
            # Append new record
            df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
            
            # Save updated DataFrame
            df.to_csv(self.csv_path, index=False)
            
            return {
                'success': True,
                'message': 'Symptoms recorded successfully',
                'score': total_score,
                'priority': priority
            }
            
        except Exception as e:
            return {
                'success': False,
                'message': f'Error recording symptoms: {str(e)}',
                'score': None,
                'priority': None
            }
            
    def get_patient_history(self, patient_id):
        """
        Retrieve symptom history for a specific patient
        
        Args:
            patient_id (str): Patient's health care number
            
        Returns:
            dict: Response containing success status and patient history
        """
        try:
            df = pd.read_csv(self.csv_path)
            patient_records = df[df['patient_id'] == patient_id].to_dict('records')
            
            # Convert pipe-separated symptoms back to lists and add priority levels
            for record in patient_records:
                record['symptoms'] = record['symptoms'].split('|')
                record['priority'] = self.determine_priority(record['total_score'])
                
            return {
                'success': True,
                'history': patient_records
            }
            
        except Exception as e:
            return {
                'success': False,
                'message': f'Error retrieving patient history: {str(e)}',
                'history': []
            }