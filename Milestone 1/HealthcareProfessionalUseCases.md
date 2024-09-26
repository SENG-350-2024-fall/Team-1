

## Use Case #1: Log In (Authenticate as a Healthcare Professional)

| **Use Case**    | 1 Log In (Authenticate as a Healthcare Professional) |
| --- | --- |
| **Description** | A healthcare professional accesses the Mister Ed system to authenticate their identity and gain access to patient information and system functionalities. |
| **Actors**      | Healthcare professionals (e.g., doctors, nurses, administrative staff) |
| **Assumptions** | - Users have valid credentials (username and password).<br> - The system is operational and accessible. |
| **Steps**       | 1. User navigates to the login page.<br>2. User enters their credentials.<br>3. System verifies credentials.<br>4. User is granted access to the dashboard if authenticated. |
| **Variations**  | - If authentication fails, the user is prompted to retry or reset their password. |
| **Non-Functional** | - The system should respond within 2 seconds for successful login.<br>- Secure encryption of user credentials must be maintained. |
| **Issues**      | - Potential for unauthorized access if security measures are insufficient. |

---

## Use Case #2: View Patient Symptoms/Triage Report

| **Use Case**    | 2 View Patient Symptoms/Triage Report |
| --- | --- |
| **Description** | A healthcare professional views the triage report and symptoms of a patient to assess their condition. |
| **Actors**      | Healthcare professionals. |
| **Assumptions** | - The patient has been triaged and their report is available in the system. |
| **Steps**       | 1. User selects a patient from the list.<br>2. System retrieves the patient’s triage report.<br>3. User reviews the symptoms and triage details. |
| **Variations**  | - If the report is not available, a notification is displayed. |
| **Non-Functional** | - The system should load the report within 3 seconds. |
| **Issues**      | - Incomplete or inaccurate reports may lead to misjudgments. |

---

## Use Case #3: Edit Triage Report

| **Use Case**    | 3 Edit Triage Report |
| --- | --- |
| **Description** | A healthcare professional modifies an existing triage report to update patient information or symptoms. |
| **Actors**      | Healthcare professionals. |
| **Assumptions** | - The user has permission to edit reports.<br>  - The patient has been triaged and their report is available in the system.|
| **Steps**       | 1. User selects the triage report to edit.<br>2. User makes necessary changes.<br>3. User saves the updated report.<br>4. System confirms the changes. |
| **Variations**  | - Changes can be reverted if made within a specific time frame. |
| **Non-Functional** | - Changes should be saved in under 2 seconds. |
| **Issues**      | - Risk of data corruption during the editing process. |

---

## Use Case #4: View Urgent Care Queue

| **Use Case**    | 4 View Urgent Care Queue |
| --- | --- |
| **Description** | A healthcare professional views the current queue of patients awaiting urgent care to manage patient flow. |
| **Actors**      | Healthcare professionals. |
| **Assumptions** | - The queue is actively updated in real-time. |
| **Steps**       | 1. User navigates to the urgent care queue section.<br>2. System displays the list of patients in the queue.<br>3. User reviews the queue order and status. |
| **Variations**  | - Users can filter the queue by urgency level. |
| **Non-Functional** | - Queue information should refresh automatically every minute. |
| **Issues**      | - Delays in updating the queue could lead to patient management issues. |

---


## Use Case #5: Add Patient to Queue

| **Use Case**    | 6 Add Patient to Queue |
| --- | --- |
| **Description** | A healthcare professional adds a new patient to the urgent care queue for treatment. |
| **Actors**      | Healthcare professionals. |
| **Assumptions** | - The patient has walked into the ED and has not been triaged in Mister ED yet |
| **Steps**       | 1. User selects the option to add a patient.<br>2. User enters the patient’s details.<br>3. System adds the patient to the queue.<br>4. System confirms the addition. |
| **Variations**  | - If the patient is already in the queue, a notification is displayed. |
| **Non-Functional** |  |
| **Issues**      | - Duplicate entries could occur if not properly checked. |

---

## Use Case #6: Add Patient Records

| **Use Case**    | 7 Add Patient Records |
| --- | --- |
| **Description** | A healthcare professional adds or updates a patient's medical records in the system. |
| **Actors**      | Healthcare professionals. |
| **Assumptions** | - The user has the appropriate permissions to modify patient records. |
| **Steps**       | 1. User selects the patient whose records need updating.<br>2. User inputs new information or updates existing records.<br>3. User saves the changes.<br>4. System confirms the updates. |
| **Variations**  | - Users can attach documents or images related to the patient’s care. |
| **Non-Functional** | - Record updates should be processed in under 3 seconds. |
| **Issues**      | - Data loss or corrupted during the save process. |

---

## Use Case #7: Assign Patient from Queue to Themselves

| **Use Case**    | 9 Assign Patient from Queue to Themselves |
| --- | --- |
| **Description** | A healthcare professional assigns a patient from the queue to themselves for treatment. |
| **Actors**      | Healthcare professionals. |
| **Assumptions** | - The healthcare professional is authorized to take on patients from the queue. |
| **Steps**       | 1. User selects a patient from the queue.<br>2. User assigns the patient to themselves.<br>3. System updates the patient's status and removed them from queue.<br>4. System confirms the assignment. |
| **Variations**  | - If the patient is already assigned, a notification is displayed. |
| **Non-Functional** | - The assignment process should be completed in under 2 seconds. |
| **Issues**      | - Misassignment could occur if proper checks are not in place. |

---
