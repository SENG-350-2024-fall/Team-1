# Queue Class for the backend
# Contains interface for the queue:
# - add
# - remove
# - send update to observers (all patients on queue)
class Queue:
    def __init__(self):
        self.queue = []
        self.observers = []

    # Add a patient to the queue
    def add(self, patient):
        self.queue.append(patient) # TODO: Insert patient into queue based on triage score
        self.notify_observers()
        # Return index of patient in the queue
        return len(self.queue) - 1

    # Remove a patient from the queue
    def remove(self, patient):
        self.queue.remove(patient)
        self.notify_observers()

    # Add an observer to the queue
    def add_observer(self, observer):
        self.observers.append(observer)

    # Notify all observers of a change in the queue -- Need QPosition in Patients in order to update.
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.queue)