This diagram shows the interactions between a **Doctor**, the **Login** system, a **Hospital**, a **PatientFile**, and a **Patient**.

### Description:

1. **Login Process**:
   - The **Doctor** sends a `login(username, password, StaffId)` request to the **Login** system.
   - The **Login** system activates and authenticates the doctor's credentials if they have entered the correct information.
   - If the login is successful, the **Login** system confirms login back to the **Doctor** and the **Login** system deactivates.

2. **Retrieving a Patient from the Queue**:
   - After logging in, the **Doctor** sends a `popPatientFromQueue()` request to the **Hospital** which keeps a queue of patients currently waiting to be seen.
   - The **Hospital** processes the request, retrieves a patient, and returns the patient information to the **Doctor** for the doctor to review.
   - The **Hospital** deactivates after this operation.

3. **Accessing and Modifying Patient Files**:
   - The **Doctor** sends a request `requestFileAccess(Patient, StaffId)` to the **PatientFile** system to access the patient’s medical records.
   - The **PatientFile** system activates, processes the request, and returns a list of the patient's files to the **Doctor**.
   - After reviewing the patient files, the **Doctor** creates a new file in the **PatientFile** system.
   - The **PatientFile** system processes the new file creation and updates the patient's file.

4. **Viewing Diagnosis**:
   - After the new file is created, the **PatientFile** system, the **Patient** can  view their new diagnosis with the `viewDiagnosis(file)`. 
   - The **PatientFile** system deactivates, and the **Patient** briefly activates to view the new file, then deactivates.

### Key Participants:
- **Doctor**: Interacts with the system to log in, retrieve patients, and create/update patient files.
- **Login**: Authenticates the doctor’s credentials.
- **Hospital**: Manages the queue of patients waiting to see a physician and provides patient information to the doctor.
- **PatientFile**: Handles patient medical records, granting access to files, and allowing updates or creation of new records.
- **Patient**: The person whose file is being updated with a new diagnosis and treatment, and who can view the updated medical records.

This sequence diagram describes a happy path flow where a doctor logs in successfully, gets a patient from the hospital queue, accesses the patients medical file, adds a new diagnosis file, and allows the patient to view their updated medical records.
