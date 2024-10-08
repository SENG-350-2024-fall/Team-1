# Patient Use Cases and Diagram #

## Patient Use Case Diagram ##

![alt text](PatientUCD.png "PatientUCD")

## Patient Use Case Descriptions ##

### UC1: Log in

| **Use Case**    | UC1 Patient_login                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Patient logs in using their profile                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Assumptions** | Is not logged in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Actors**      | Patient (primary)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Steps**       | 1. Patient clicks "Log in with BC Services Card app" button <br>2. REPEAT <br>&nbsp;&nbsp;&nbsp;&nbsp;1.1 Patient gets prompted to pair their BC Services Card App with a six symbol code on their screen. <br>&nbsp;&nbsp;&nbsp;&nbsp;1.2 Patient enters six symbol code from application into BC Services Card App. <br>UNTIL Patient inputs correct code **or** inputs incorrect code 3 times. <br>3. IF correct code THEN 3.1 Patient is brought to the main page of the application. <br>&nbsp;&nbsp;&nbsp;&nbsp;3.2 ELSE Patient is unable to log in |
| **Issues**      | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### UC2: Log out

| **Use Case**    | 2 Patient_logout                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------- |
| **Description** | Patient logs out                                                                                      |
| **Assumptions** | Is logged in                                                                                      |
| **Actors**      | Patient (primary)                                                                                    |
| **Steps**       | 1. Patient clicks the log out option on the application. <brl>2. Patient is logged out of their session |
| **Variations**  | **#1.** Patient exits out of the application                                                         |
| **Issues**      | How does application process unfinished virtual triage processes?                                 |
|                 |                                                                                                   |

### UC3: Edit profile

| **Use Case**    | UC3 Edit_profile                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------- |
| **Description** | Patient edits their profile information, including address or contact details.              |
| **Assumptions** | Patient is logged.                                                            |
| **Actors**      | Patient (primary)                                                                                  |
| **Steps**       | 1. Patient selects "Edit profile" option.<br>2. Patient modifies personal details.<br>3. System saves changes. |
| **Issues**      | None                                                                                               |

### UC3.1: Modify medical history

| **Use Case**    | UC3.1 Modify_medical_history                                                                                      |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Description** | Patient modifies their medical history, such as conditions or allergies.                                           |
| **Assumptions** | Patient is logged in.                                                                 |
| **Actors**      | Patient (primary), System Administrator                                                                                                 |
| **Steps**       | 1. Patient selects "Edit profile" option.<br>2. Patient chooses "Modify medical history" and requests a change to their medical history. An appointment is scheduled with a doctor.<br>3. Doctor submits medical history revision to System Admin. |
| **Issues**      | - Appointment with a doctor means a change in medical history anyways, meaning no matter what Patient medical history will be changed.<br> - Doctor doesn't have to be an ED doctor.                                                                                                              |

### UC3.2: Modify emergency contact

| **Use Case**    | UC3.2 Modify_emergency_contact                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Description** | Patient modifies their emergency contact information.                                                             |
| **Assumptions** | Patient is logged in.                                                                 |
| **Actors**      | Patient (primary)                                                                                                 |
| **Steps**       | 1. Patient selects "Edit profile" option.<br>2. Patient chooses "Modify emergency contact" and updates the contact information.<br>3. System saves changes. |
| **Issues**      | None                                                                                                              |

### UC4: Find nearest ED

| **Use Case**    | UC4 Find_nearest_ED                                                                                    |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| **Description** | Patient searches for and identifies the nearest emergency department (ED).                            |
| **Assumptions** | Patient is logged in.                          |
| **Actors**      | Patient (primary)                                                                                     |
| **Steps**       | 1. Patient selects "Find nearest ED" option.<br>2. System locates the nearest ED based on patient’s current location, wait time, and time to destination. |
| **Issues**      | None                                                                                                  |

### UC5: See ED wait times

| **Use Case**    | UC5 See_ED_wait_times                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| **Description** | Patient views the current estimated wait times at nearby emergency departments.                        |
| **Assumptions** | Patient is logged in.                          |
| **Actors**      | Patient (primary)                                                                                     |
| **Steps**       | 1. Patient selects "See ED wait times" option.<br>2. System provides estimated wait times for nearby EDs. |
| **Issues**      | None                                                                                                  |

### UC6: Undergo virtual triage

| **Use Case**    | UC6 Undergo_virtual_triage                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| **Description** | Patient undergoes a virtual triage process to assess the urgency of their condition.                  |
| **Assumptions** | Patient is logged in.                         |
| **Actors**      | Patient (primary), Online Nurse                                                                                   |
| **Steps**       | 1. Patient selects "Undergo virtual triage" option.<br>2. Patient waits for Online Nurse to provide online triage.<br>3. After online triage, Online Nurse places Patient into queue for the nearest ED. |
| **Issues**      | None                                                                                                 |

### UC6.1: Contact emergency contact

| **Use Case**    | UC6.1 Contact_emergency_contact                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| **Description** | Patient contacts their emergency contact directly from the system.                                    |
| **Assumptions** | Patient is logged in and has an emergency contact saved.                                              |
| **Actors**      | Patient (primary)                                                                                    |
| **Steps**       | 1. Patient selects "Contact emergency contact" during or after virtual triage.<br>2. System initiates a call or message to the emergency contact. |
| **Issues**      | None                                                                                                 |

### UC7: View ED Queue

| **Use Case**    | UC7 View_ED_queue                                                                                     |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| **Description** | Patient views their position in the emergency department queue.                                       |
| **Assumptions** | Patient has checked into an ED queue via the system.                                                  |
| **Actors**      | Patient (primary)                                                                                    |
| **Steps**       | 1. Patient selects "View ED Queue" option.<br>2. System displays the patient’s current position in the queue. |
| **Issues**      | None                                                                                                 |

### UC7.1: Front of ED Queue notification

| **Use Case**    | UC8.1 Front_of_ED_queue_notification                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| **Description** | Patient receives a notification when they are at the front of the ED queue.                           |
| **Assumptions** | Patient is in the ED queue.                                                                           |
| **Actors**      | Patient (primary), Online Nurse                                                                                    |
| **Steps**       | 1. System monitors the ED queue. Once Patient reaches front of queue, wait for Online Nurse<br>2. IF Online Nurse takes more than 15 minutes THEN 2.1 System sends notification to patient's cell via SMS.<br> ELSE 2.2 Online Nurse sends notification to patient's cell via SMS. |
| **Issues**      | None                                                                                                 |

### UC7.2: Remove self from queue

| **Use Case**    | UC8.2 Remove_self_from_queue                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| **Description** | Patient removes themselves from the ED queue.                                                         |
| **Assumptions** | Patient has checked into an ED queue via the system.                                                  |
| **Actors**      | Patient (primary)                                                                                    |
| **Steps**       | 1. Patient selects "View ED Queue" option then selects "Remove self from Queue" option.<br>2. System confirms the action.<br>3. Patient is removed from the queue. |
| **Issues**      | None                                                                                                 |
