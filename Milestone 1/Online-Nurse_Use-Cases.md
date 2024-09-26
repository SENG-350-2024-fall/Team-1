## Use Case #1: Log In (with Authentication)

| **Use Case**    | 1. Log In (Authenticate as a Healthcare Professional) |
| --- | --- |
| **Description** | The online nurse logs into the MisterED system with proper identity authentication so that only authorized staff have access to privileged information. |
| **Actors**      | Online Nurse |
| **Assumptions** | - Users have valid credentials (username and password).<br> - The system is operational and accessible. |
| **Steps**       | 1. Nurse navigates to the login page.<br>2. Nurse enters their credentials.<br>3. System verifies credentials.<br>4. Nurse is sent a MFA push notification on their device (through SMS or email, method of preference selected).<br>5. Nurse clicks verification message on their device.<br>6. Verified user (nurse) is logged into the system. |
| **Variations**  | - If authentication fails, the user is prompted to retry or reset their password.<br> - If the MFA push notification is not automatically sent, the user may prompt the system to resend the push notification. |
| **Non-Functional** | - The system should respond within 10 seconds for successful login, any login response greater than 30 seconds should timeout and prompt the user to retry login.<br> - Only verified and authenticated users will be granted access to the system.<br> - Secure encryption of user credentials must be maintained. |
| **Issues**      | - Potential for unauthorized access if security measures are insufficient.<br> - Attackers could steal users' devices and security credentials and spoof/imitate an online nurse login while gaining access to the system.<br> - The nurse may need to reset their password if they have forgotten their credentials which must involve verification with a System Administrator. |

## Use Case #2: View Patient Information (Symptoms & Medical History)

| **Use Case**    | 2. View Patient Information (Submitted Symptoms & any Medical History linked to their BCID) |
| --- | --- |
| **Description** | The online nurse can view Patient Information when they submit a triage request, showing their inputted/selected symptoms, and their medical history including previous admissions to the ER, doctor visits, lab test results, allergies, medications, etc. |
| **Actors**      | Online Nurse |
| **Assumptions** | - The nurse is successfully authenticated and logged in with valid credentials (username and password).<br> - The system is operational and accessible.<br> - The patient's medical information is correctly stored in the database.<br> - The patient has correctly entered/selected their symptoms and submitted them to the system successfully. |
| **Steps**       | 1. Nurse successfully completes login process.<br>2. Nurse selects a patient from the queue on their dashboard.<br>3. System retrieves patient data from the medical information database and the server.<br>4. Nurse can select to view patient's symptoms or patient's medical history.<br>5. The selected field is shown on the nurse's device for them to process. |
| **Variations**  | - Data may be incomplete or incorrectly stored within the database, in which case only the verified and complete data will be shown. This may be the case if the patient does not have a medical history within BC.<br> - The patient may have incorrectly or inaccurately inputted their symptoms, in which case the nurse may see the input or prompt the patient to retry their triage process (resubmit or start over). |
| **Non-Functional** | - The system should respond quickly when the nurse selects the information to be retrieved. Data should be retrieved and displayed within 10 seconds of the request, any retrieval response longer than 30 seconds should timeout and prompt the nurse to retry.<br> - Only verified and authenticated users will be granted access to privileged patient data.<br> - Nurse interactions will be regularly audited to verify no elevation of privilege.<br> - Patient data should be periodically checked to ensure it is readily available to be accessed.<br> - The nurse will only be able to request patient data once per 30 seconds, this is to prevent server overload. |
| **Issues**      | - Potential for incomplete or missing patient data.<br> - Potential for incorrectly inputted patient symptoms.<br> - The server may be slow and require the nurse to retry the request if the load is too high at the time. |

## Use Case #3: Triage Patient

| **Use Case**    | 3. Perform a Virtual Patient Triage |
| --- | --- |
| **Description** | The online nurse will perform a virtual triage for the patient given their inputted symptoms and relevant medical history. From the triage conclusion the nurse will decide the best course of action and proceed to give the patient directions, or involve other personnel should they see fit. |
| **Actors**      | Online Nurse |
| **Assumptions** | - The nurse is successfully authenticated and logged in with valid credentials (username and password).<br> - The system is operational and accessible.<br> - The patient's medical information and symptoms are stored and inputted correctly into the database and the system.<br> - The nurse has successfully requested and retrieved the patient's medical history and their submitted symptoms. |
| **Steps**       | 1. Nurse navigates to the login page.<br>2. Nurse enters their credentials.<br>3. System verifies credentials.<br>4. Nurse is sent a MFA push notification on their device (through SMS or email, method of preference selected).<br>5. Nurse clicks verification message on their device.<br>6. Verified user (nurse) is logged into the system. |
| **Variations**  | - If authentication fails, the user is prompted to retry or reset their password.<br> - If the MFA push notification is not automatically sent, the user may prompt the system to resend the push notification. |
| **Non-Functional** | - The system should respond within 10 seconds for successful login, any login response greater than 30 seconds should timeout and prompt the user to retry login.<br> - Only verified and authenticated users will be granted access to the system.<br> - Secure encryption of user credentials must be maintained. |
| **Issues**      | - Potential for unauthorized access if security measures are insufficient.<br> - Attackers could steal users' devices and security credentials and spoof/imitate an online nurse login while gaining access to the system.<br> - The nurse may need to reset their password if they have forgotten their credentials which must involve verification with a System Administrator. |