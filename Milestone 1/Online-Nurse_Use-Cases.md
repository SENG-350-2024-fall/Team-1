## Use Case #1: Log In (with Authentication)

| **Use Case**    | 1 Log In (Authenticate as a Healthcare Professional) |
| --- | --- |
| **Description** | The online nurse logs into the MisterED system with proper identity authentication so that only authorized staff have access to privileged information. |
| **Actors**      | Online Nurse |
| **Assumptions** | - Users have valid credentials (username and password).<br> - The system is operational and accessible. |
| **Steps**       | 1. Nurse navigates to the login page.<br>2. Nurse enters their credentials.<br>3. System verifies credentials.<br>4. Nurse is sent a MFA push notification on their device (through SMS or email, method of preference selected).<br>5. Nurse clicks verification message on their device.<br>6. Verified user (nurse) is logged into the system. |
| **Variations**  | - If authentication fails, the user is prompted to retry or reset their password.<br> - If the MFA push notification is not automatically sent, the user may prompt the system to resend the push notification. |
| **Non-Functional** | - The system should respond within 2 seconds for successful login.<br> - Only verified and authenticated users will be granted access to the system.<br> - Secure encryption of user credentials must be maintained. |
| **Issues**      | - Potential for unauthorized access if security measures are insufficient.<br> - Attackers could steal users' devices and security credentials and spoof/imitate an online nurse login while gaining access to the system. |

## Use Case #2: View Patient Information (Symptoms & Medical History)

| **Use Case**    | 2 View Patient Information (Submitted Symptoms & any Medical History linked to their BCID) |
| --- | --- |
| **Description** | The online nurse can view Patient Information when they submit a triage request, showing their inputted/selected symptoms, and their medical history including previous admissions to the ER, doctor visits, lab test results, allergies, medications, etc. |
| **Actors**      | Online Nurse |
| **Assumptions** | - The nurse is successfully authenticated and logged in with valid credentials (username and password).<br> - The system is operational and accessible.<br> - The patient's medical information is correctly stored in the database.<br> - The patient has correctly entered/selected their symptoms and submitted them to the system successfully. |
| **Steps**       | 1. Nurse successfully completes login process.<br>2. Nurse selects a patient from the queue on their dashboard.<br>3. System retrieves patient data from the medical information database and the server.<br>4. Nurse can selet to view patient's symptoms or patient's medical history.<br>5. The selected field is shown on the nurse's device for them to process. |
| **Variations**  | - If authentication fails, the user is prompted to retry or reset their password.<br> - If the MFA push notification is not automatically sent, the user may prompt the system to resend the push notification. |
| **Non-Functional** | - The system should respond within 2 seconds for successful login.<br> - Only verified and authenticated users will be granted access to the system.<br> - Secure encryption of user credentials must be maintained. |
| **Issues**      | - Potential for unauthorized access if security measures are insufficient.<br> - Attackers could steal users' devices and security credentials and spoof/imitate an online nurse login while gaining access to the system. |