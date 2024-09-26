## Use Case #1: Log In (with Authentication)

| **Use Case**    | 1. Log In (Authenticate as a Healthcare Professional) |
| --- | --- |
| **Description** | The online nurse logs into the MisterED system with proper identity authentication so that only authorized staff have access to privileged information. |
| **Actors**      | Online Nurse |
| **Assumptions** | - Users have valid credentials (username and password).<br> - The system is operational and accessible. |
| **Steps**       | 1. Nurse navigates to the login page.<br>2. Nurse enters their credentials.<br>3. System verifies credentials.<br>4. Nurse is sent a MFA push notification on their device (through SMS or email, method of preference selected).<br>5. Nurse clicks verification message on their device.<br>6. Verified user (nurse) is logged into the system. |
| **Variations**  | - If authentication fails, the user is prompted to retry or reset their password.<br> - If the MFA push notification is not automatically sent, the user may prompt the system to resend the push notification. |
| **Non-Functional** | - System should respond within 10 seconds for successful login, any login response greater than 30 seconds should timeout and prompt the user to retry login.<br> - Only verified and authenticated users will be granted access to the system.<br> - Secure encryption of user credentials must be maintained. |
| **Issues**      | - Potential for unauthorized access if security measures are insufficient.<br> - Attackers could steal users' devices and security credentials and spoof/imitate an online nurse login while gaining access to the system.<br> - The nurse may need to reset their password if they have forgotten their credentials which must involve verification with a System Administrator. |

## Use Case #2: View Patient Information (Symptoms & Medical History)

| **Use Case**    | 2. View Patient Information (Submitted Symptoms & any Medical History linked to their BCID) |
| --- | --- |
| **Description** | The online nurse can view Patient Information when they submit a triage request, showing their inputted/selected symptoms, and their medical history including previous admissions to the ER, doctor visits, lab test results, allergies, medications, etc. |
| **Actors**      | Online Nurse |
| **Assumptions** | - The nurse is successfully authenticated and logged in with valid credentials (username and password).<br> - The system is operational and accessible.<br> - The patient's medical information is correctly stored in the database.<br> - The patient has correctly entered/selected their symptoms and submitted them to the system successfully. |
| **Steps**       | 1. Nurse successfully completes login process.<br>2. Nurse selects a patient from the queue on their dashboard.<br>3. System retrieves patient data from the medical information database and the server.<br>4. Nurse can select to view patient's symptoms or patient's medical history.<br>5. The selected field is shown on the nurse's device for them to process. |
| **Variations**  | - Data may be incomplete or incorrectly stored within the database, in which case only the verified and complete data will be shown. This may be the case if the patient does not have a medical history within BC.<br> - The patient may have incorrectly or inaccurately inputted their symptoms, in which case the nurse may see the input or prompt the patient to retry their triage process (resubmit or start over). |
| **Non-Functional** | - System should respond quickly when the nurse selects the information to be retrieved. Data should be retrieved and displayed within 10 seconds of the request, any retrieval response longer than 30 seconds should timeout and prompt the nurse to retry.<br> - Only verified and authenticated users will be granted access to privileged patient data.<br> - Nurse interactions will be regularly audited to verify no elevation of privilege.<br> - Patient data should be periodically checked to ensure it is readily available to be accessed and properly maintained.<br> - The nurse will only be able to request patient data once per 30 seconds, this is to prevent server overload and improve availability. |
| **Issues**      | - Potential for incomplete or missing patient data.<br> - Potential for incorrectly inputted patient symptoms.<br> - The server may be slow and require the nurse to retry the request if the load is too high at the time. |

## Use Case #3: Triage Patient

| **Use Case**    | 3. Perform a Virtual Patient Triage |
| --- | --- |
| **Description** | The online nurse will perform a virtual triage for the patient given their inputted symptoms and relevant medical history. From the triage conclusion the nurse will decide the best course of action and proceed to give the patient directions, or involve other personnel should they see fit. |
| **Actors**      | Online Nurse |
| **Assumptions** | - The nurse is successfully authenticated and logged in with valid credentials (username and password).<br> - The system is operational and accessible.<br> - The patient's medical information and symptoms are stored and inputted correctly into the database and the system.<br> - The nurse has successfully requested and retrieved the patient's medical history and their submitted symptoms. |
| **Steps**       | 1. Nurse selects a patient from the triage queue.<br>2. The system collects the symptoms and medical history data for the patient and provides it to the nurse.<br>3. Nurse evaluates the presented symptoms paired with the medical history data.<br>4. Nurse places the patient in the ER queue with a position based on the priority they assign them. The triage results from the nurse are sent to the ER attached to their queue position for the in-person ER staff to view.<br>5. Nurse provides follow-up directions to the patient based on their triage results. These directions are also sent to the ER attached to their virtual triage report for the in-person staff to view. |
| **Variations**  | - If the patient's triage results are urgent enough the nurse will place them at the front of the ER queue, in which case the patient receives a message to visit the ER immediately.<br> - If the patient's triage results includes non life-threatening but severe symptoms the system will prioritize their case so that the nurse triages them as soon as possible. |
| **Non-Functional** | - System should have minimal delays when processing triage cases so that patients are helped as soon as possible.<br> - System must be available and usable at all times so that patients can be adequately serviced in the event of medical emergencies.<br> - Patient data and symptoms, including triage results and follow-up directions, must be encrypted so to preserve data security and integrity. |
| **Issues**      | - Ensuring that triage process follows standard medical guidelines can be difficult when done virtually since certain information is difficult to obtain without physical tests (ex: checking blood pressure, heart rate, oxygen saturation level, etc.).<br> - Nurse may be occupied with patients and miss patients with severe symptoms.<br> - Nurse may be unsure of triage results with the lack of physical assessment. |

## Use Case #4: Notify Patient to Visit ER

| **Use Case**    | 4. Notify Patient to Visit the ER  |
| --- | --- |
| **Description** | The online nurse will notify the patient when it is their turn to visit the ER based on either their position in the ER queue or their triage results. If there are severe symptoms listed in the patient's information the nurse may choose to place their case at the front of the ER queue manually or notify the patient to visit the ER right away. |
| **Actors**      | Online Nurse (Primary), Patient (Secondary) |
| **Assumptions** | - The nurse is successfully authenticated and logged in with valid credentials (username and password).<br> - The system is operational and accessible.<br> - The ER has a queue with patients added based on the priority from their triage results. |
| **Steps**       | 1. Nurse selects the first patient in the ER priority queue.<br>2. The system displays the patient's triage results and information as well as their ER queue position.<br>3. Nurse clicks a button that sends the selected patient a notification recommending they come in and visit the ER as soon as possible.<br>4. Nurse is given the option to provide a notification with more specific directions.<br>5. Patient receives notification to visit the ER and any additional instructions the nurse provides.<br>6. Patient responds to the nurse's notification indicating whether they are following their directions, heading to the ER, or require further assistance. |
| **Variations**  | - Notifications may be sent by the patient's preferred method of contact (SMS, email, etc.).<br> - If a patient has been at the front of the ER priority queue for more than 15 minutes without being sent a notification by the nurse the system will automatically notify them to visit the ER they are in queue for. This is to prevent patients that have been waiting for long periods of time from continuously being jumped in queue by people with more urgent cases so that they are treated accordingly. |
| **Non-Functional** | - System should have minimal delays when sending notifications to patients and messages should be delivered a minimum of 99% of the time.<br> - System must be available and usable at all times so that patients can be notified in a timely manner without being interrupted by any system queue or notifiation delays.<br> - Patient notifications and directions must be encrypted so to preserve data security and integrity. |
| **Issues**      | - Patients may miss notifications that are sent to them.<br> - Some notifications may be undelivered, in this case nurses should be notified that their directions were not delivered successfully.<br> - Patients may not respond to notifications due to worsening medical conditions or potential inability to respond. |

## Use Case #5: Escalate Patient to First Responder / EMS

| **Use Case**    | 4. Escalate Patient to First Responder / EMS  |
| --- | --- |
| **Description** | The online nurse will escalate a patient's case to a First Responder / Emergency Medical Services (EMS) if they identify any life-threatening or critical symptoms. This helps provide quicker intervention than continuing with the triage process. The system will also send the patient's information (medical history and symptoms) to the First Responders so that they can be better prepared ahead of time. |
| **Actors**      | Online Nurse (Primary), First Responder (Secondary) |
| **Assumptions** | - The nurse is successfully authenticated and logged in with valid credentials (username and password).<br> - The system is operational and accessible.<br> - The patient has entered life-threatening or critical symptoms.<br> - There is a First Responder readily available to respond to the patient. |
| **Steps**       | 1. Nurse identifies critical life-threatening symptoms on the patient's submitted triage request.<br>2. Nurse triggers the escalation to the First Responders via the system.<br>3. System notifies the First Responders there is a patient requiring immediate medical attention and a First Reponder indicates they are responding to the case.<br>4. The system sends and displays the the patient's medical history and submitted symptoms to the First Responders. |
| **Variations**  | - There may not be a First Responder immediately available.<br> |
| **Non-Functional** | - System should have no delays when alerting First Responders and sending patient information.<br> - System must be available and usable at all times so that patients treated as soon as possible.<br> - Patient medical data and symptom information must be encrypted so to preserve data security and integrity. |
| **Issues**      | - First Responders may not be immediately available. |

## Use Case #6: Log Out

| **Use Case**    | 6. Log Out |
| --- | --- |
| **Description** | The online nurse logs out from the MisterED system. |
| **Actors**      | Online Nurse |
| **Assumptions** | - The nurse is successfully authenticated and logged in with valid credentials (username and password).<br> - The system is operational and accessible. |
| **Steps**       | 1. Nurse locates the logout button on their main page/dashboard.<br>2. Nurse clicks logout.<br>3. System logs the nurse out and displays a successful logout message. |
| **Variations**  | - If the logout fails the nurse is prompted to retry logging out. |
| **Non-Functional** | - System should respond within 10 seconds for successful logout, any logout response greater than 30 seconds should timeout and prompt the user to retry logout.<br> - System should display a successful logout message so the user can ensure their device is not left logged in with their elevated privileges. |
| **Issues**      | - None specified |