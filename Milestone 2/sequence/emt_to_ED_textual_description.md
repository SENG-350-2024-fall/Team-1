The process where an **EMT** interacts with mister ED to manage a new patient request, edit a triage report, and admit the patient to a hospital, is shown in this sequence diagram.

### Sequence Diagram Description:

1. **Login Process**:
   - The **EMT** begins by requesting a `login(username, password, StaffId)` to the **Login** system.
   - The **Login** system activates and authenticates the EMT.
   - After the authentication is completed successfully, the **Login** system deactivates.

2. **Receiving a New Patient Request**:
   - The **NotificationSystem** sends a message `newPatientRequest()` to the **EMT**, indicating that there is a new patient they must assist.
   - The **EMT** accepts this request by sending `acceptRequest(patient)` back to the **NotificationSystem**.

3. **Retrieving Patient Records**:
   - The **NotificationSystem** requests the patient records by sending `getPatientRecords(patient)` to the **PatientDB** (patient database).
   - The **PatientDB** processes the request, activating to retrieve patient info, and sends the patient records to the **EMT** with `sendPatientRecords(file)`.

4. **Editing the Triage Report**:
   - The **EMT** then sends the message `editTriageReport(patientReport)` to the **TriageSystem** to update the patient’s triage report based on their in person assessment of the patient.
   - The **TriageSystem** confirms the update with `confirmReportUpdate()` to the **EMT**.

5. **Finding the Nearest Hospital**:
   - The **EMT** requests the location of the nearest hospital by sending `getNearestHospitalLocation(location)` to the **LocationService**.
   - The **LocationService** responds by sending back the closest hospital's location with `sendHospitalLocation(Hospital)`.

6. **Admitting the Patient to the Hospital**:
   - The **EMT** then takes the patient to the **Hospital** and upon arrival can admit the patient to the hospital with `admitPatient(patient)`.
   - The **Hospital** processes the admission request, activating to confirm the patient’s admission, and sends back a confirmation message `confirmAdmission()`.

7. **Removing the Current Patient**:
   - Now that the patient is at the hospital they are out og the EMT's care so **EMT** sends a message to the **Patient** to indicate that the current patient is being removed with `removeCurrentPatient()`.
   - The **Patient** confirms this action by responding with `confirmPatientRemoved()`, after which the **Patient** deactivates.

### Key Participants:
- **EMT**: Interacts with various systems to log in, manage patient requests, and admit patients to hospitals.
- **Login**: Authenticates the EMT's credentials.
- **NotificationSystem**: Sends notifications for new patient requests and facilitates communication about patient records.
- **PatientDB**: Stores and retrieves patient records.
- **TriageSystem**: Handles updates to the patient's triage reports.
- **LocationService**: Provides information about the nearest hospital location.
- **Hospital**: Admits the patient and confirms their admission.

This sequence diagram depicts the comprehensive workflow that an EMT follows when responding to a new patient request, ensuring that all necessary information is gathered and the patient is safely admitted to the hospital.
