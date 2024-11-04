# Based on user input, triage
# scores user priority and assigns
# course of action.

# Each criteria should grant x amount of points.
# The total points will determine the priority of the patient.

# EG: <10 points = Low Priority (online nurse phonecall)
#   10-20 points = Medium Priority (go to hospital)
#   20-30 points = High Priority (ambulance comes to get you, uh oh)

# TODO: Return proper triage questions
def questions():
    """Returns questions used for triage"""
    return "Are you low, moderate, or critical priority?"

def determine_priority(triage_score):
    """Returns priority based on triage score"""
    if triage_score < 10:
        return 'low'
    elif triage_score <= 20:
        return 'moderate'
    else:
        return 'critical'
