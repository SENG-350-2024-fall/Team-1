
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
    def __init__(self, name, role activeLocation): # Change to some API that returns the active location
        super().__init__(name, role)
        self.activeLocation = activeLocation

class Nurse(Staff):
    # Initialize
    def __init__(self, name, role, location):
        super().__init__(name, role)
        self.location = location
