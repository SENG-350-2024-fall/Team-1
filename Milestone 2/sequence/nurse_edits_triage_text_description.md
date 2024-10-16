This sequence diagram shows how a **Nurse** can edit a patient's triage report using the Mister ED system.

### Sequence Diagram Description:

1. **Login Process**:
   - The **Nurse** initiates the process by sending a `login(username, password, StaffId)` request to the **Login** system.
   - The **Login** system activates and processes the authentication if the credentials provided are correct.
   - Once authentication is complete, the **Login** system deactivates.

2. **Retrieving a Patient from the Queue**:
   - After logging in, the **Nurse** sends a `popPatientFromQueue()` request to the **Hospital** to retrieve a patient from the emergency department queue.
   - The **Hospital**  returns the patient info.
   - The **Hospital** deactivates after this operation.

3. **Accessing the Triage Report**:
   - The **Nurse** requests access to the patient's triage report with `requestFileAccess(patient)` to the **TriageReportFile** system.
   - The **TriageReportFile** system activates and returns the patient's relevant triage file.

4. **Updating the Triage Report**:
   - The **Nurse** then updates the triage report by sending an updated report with `updateReport(triageFile)` to the **TriageReportFile** system.
   - After processing the update, the **TriageReportFile** system confirms the update.
   - The **TriageReportFile** system deactivates after the confirmation.

### Key Participants:
- **Nurse**: Interacts with system to log in, retrieve patients and files, and edit triage reports.
- **Login**: Authenticates the nurse's credentials.
- **Hospital**: Manages the queue of patients and provides patient information to the nurse.
- **TriageReportFile**: Handles access to and updates of patient triage reports.

This sequence diagram displays the workflow of a nurse logging in, retrieving a patient from the hospital queue, accessing the patient's triage report, and updating it. 
