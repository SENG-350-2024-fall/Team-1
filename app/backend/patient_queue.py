# Queue Class for the backend
# Contains interface for the queue:
# - add
# - remove
# - send update to observers (all patients on queue)
import csvdatabase as cdb
from people import Patient
from typing import List
import csv

queue_db = cdb.CSVDatabase('./db/patient.csv')

class PatientQueue:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.queue = []
            cls._instance.observers = []
        return cls._instance

    def build_queue_from_db(self):
        """
        Build queue and observers from queue database
        """
        queue = []
        observer = []

        for p in queue_db.read_all():
            patient = Patient(p_info=p)
            queue.insert(int(patient.q_pos), patient)
            observer.append(patient)

        self.queue = queue
        self.observers = observer

    def add(self, patient):
        """
        Add a patient to the queue based on triage score and priority.
        
        Args:
            patient: Patient object to be added
            
        Returns:
            int: Position where patient was inserted
        """
        # Find insert position based on triage score and priority
        insert_position = 0
        for i, existing_patient in enumerate(self.queue):
            # Critical patients go first
            if patient.priority == "critical" and existing_patient.priority != "critical":
                break
            # Then sort by triage score
            elif patient.triage_score <= existing_patient.triage_score:
                insert_position = i + 1
            else:
                break
        patient.q_pos = insert_position
        queue_db.add_line(patient.to_dict())
        self.queue.insert(insert_position, patient)
        self.add_observer(patient)  # Automatically add patient as observer
        self.update_queue_positions() # Why are we updating queue positions?
        self.notify_observers() 
        return insert_position

    def remove(self, patient):
        """
        Remove a patient from the queue
        
        Args:
            patient: Patient object to be removed
        """
        if patient in self.queue:
            queue_db.remove_str_line(patient.hcn, 'hcn')
            self.queue.remove(patient)
            self.remove_observer(patient)  # Remove patient from observers
            self.update_queue_positions()
            self.notify_observers()


    def add_observer(self, observer):
        """
        Add a patient as an observer
        
        Args:
            observer: Patient object to observe queue
        """
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        """
        Remove a patient from observers
        
        Args:
            observer: Patient object to remove from observers
        """
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        """Notify all observers of queue changes"""
        for observer in self.observers:
            observer.update(self.queue)
            # Unnecessary -> queue_db.update_value(queue_db.get_line_num(observer.hcn), 'q_pos', observer.q_pos)

    def update_queue_positions(self):
        """Update positions for all patients in queue"""
        # Sort queue from greatest triage score to lowest
        self.queue.sort(reverse=True)
        for index, patient in enumerate(self.queue):
            patient.modify_q_pos(index)
            queue_db.update_value(queue_db.get_line_num(patient.hcn, 'hcn'), 'q_pos', index)