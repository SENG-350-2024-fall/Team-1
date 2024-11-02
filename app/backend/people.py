
class Staff:
    # Initialize
    def __init__(self, name, role):
        self.name = name
        self.role = role
    

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
        
# User becomes a patient when
# a recommendation is made by MrED
class Patient(User):
    # Initialize
    def __init__(self, name, age, priority, triage_score, q_pos):
        super().__init__(name, age)
        self.priority = priority
        self.triage_score = triage_score
        if 10 <= self.triage_score <= 20: # If patient is "priority", but not "critical" by MrED diagnosis, then they must go to a hospital and get qPosition
            self.q_pos = q_pos

    def modify_q_pos(self, q_pos):
        self.q_pos = q_pos
    
        