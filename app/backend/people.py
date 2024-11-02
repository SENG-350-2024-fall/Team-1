
class Staff:
    # Initialize
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def login(self):
        print(f'This function is a placeholder for the staff login')


class Doctor(Staff):
    # Initialize
    def __init__(self, name, role, specialty):
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
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def login(self):
        print(f'This function is a placeholder for the patient/user login')
        
# User becomes a patient when
# a recommendation is made by MrED
class Patient(User):
    def __init__(self, name, age, priority, triage_score, q_pos):
        super().__init__(name, age)
        self.priority = priority
        self.triage_score = triage_score
        self.q_pos = q_pos
        
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



        