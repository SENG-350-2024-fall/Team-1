### **Key Entities and Their Relationships:**

1. **Person**: 
   - The base class for human actors in the system such as `Patient` and `Staff`
   - Class contains personal information like names,  date of registration with mister ED, and methods of contact (phone number, and email).
   - Methods are available to update contact info, log out, and send notifications.

2. **Patient**:
   - Inherits from `Person`, contains attributes allergies, birthdate (which can derive age), prescriptions, emergency contact, and occupation.
   - Patients can log in using a healthcare card number and see their medical history, emergency contacts, triage reports, and telemedicine appointments.
   - Patients are associated with care providers, ED queues, and hospitals when they are using the triage of mister ED.

3. **Staff**:
   - Inherits from `Person`, includes roles `Doctor`, `Nurse`, `OnlineNurse`, `EMT`, and `Admin`.
   - Staff has attributes for their shift schedule, on-call status, username, password, department information, and availability if they are currently with a patient or able to take a new patient.
   - There are methods to allow staff to log in, view and update shift schedules, view assigned patients, assign patients to care, remove patients from their care, and manage their availability.

4. **Doctor Class** (inherits from **Staff**):
   - Represents a doctor with a list of their specialties and list of current patients.
   - They have the ability to order medical scans for patients (`orderScan()`).

5. **Nurse Class** (inherits from **Staff**):
   - Represents a nurse with a list of specialties and current patients they are tending to.

6. **OnlineNurse Class** (inherits from **Staff**):
   - Represents a nurse working online, responsible for handling virtual consultations with patients.
   - Can retrieve the next patient from their queue using the `getNextPatient()` method.

7. **EMT Class** (inherits from **Staff**):
   - Represents an emergency medical technician or paramedic.
   - Contains methods for dispatching to a patient, getting the closest emergency department to their location, and accessing information about the current patient under care.

8. **Admin Class** (inherits from **Staff**):
   - Represents the system administrator.
   - Admins have the attributes `Username`, `Password`, and `Permissions`, and they can manage medical records if there are errors in medical files via the **Alters** class.

9. **Hospital Class**:
   - Represents a hospital with attributes `Location` the physical address of the hospital, `EstimatedWaitTime` the approximate wait time a patient can expect in the emergency room, `PhoneNumber`, `Capacity` the number of patients the hospital can accommodate, and the `EDQueue` the list of patients currently waiting treatment at the hospital.
   - Methods to manage hospital capacity, wait times, and patient queues.

10. **MedicalRecord Class**:
   - Represents a patient's medical record, with attributes like `FileName`, `FileSize`, `FileType`, `LastUpdated`, `DateCreated`, and `Patient`.
   - Methods to update or view file details.

11. **TriageReportFile, MedicalImaging, and MedicationFile Classes**:
   - These classes represent different types of medical records and inherit from **MedicalRecord**.
     - **TriageReportFile**: Stores triage information and symptoms.
     - **MedicalImaging**: this is MRI images or Xray images or other medical images the hospital may produce, diagnoses, and observations.
     - **MedicationFile**: Stores information about medications including prescribing doctors, and prescription details. Also includes a method to cancel prescriptions.

12. **Treats Class**:
   - Represents actions related to a care physician treating a patient.
   - Doctors can diagnose patients, prescribe medications, admit patients, and discharge them using methods from this class.

13. **Triages Class**:
   - Represents actions related to triaging a patient.
   - Nurses and online nurses can edit triage reports, admit patients, update patient priority, and assign patients to hospital queues.

14. **Assists Class**:
   - Represents actions related to assisting emergency medical technicians.
   - EMTs can edit triage reports, update patient priorities, and get patient locations.

15. **Alters Class** (New Addition):
   - The **Alters** class has methods for editing patient files (`editPatientFile()`) and deleting files (`deletePatientFile()`).
   - It is connected to **Admin**, since only system administrators to can alter patient history if there is a mistake in their records.

16. **Relationships**:
   - **Patient**  is related to **Doctor** by being treated, **Nurse**  by being triaged, **OnlineNurse** by being triage, and **EMT**  by being assisted.
   - **Person** is the base class for **Patient** and **Staff**.
   - **Staff** includes different healthcare workers like **Doctor**, **Nurse**, **OnlineNurse**, **EMT**, and **Admin**.
   - **MedicalRecord** is connected to different types of records: **TriageReportFile**, **MedicalImaging**, and **MedicationFile** and are associated with specific **Patient** objects.
   - **Admin** is linked to **MedicalRecord** through the **Alters** class, allowing them to correct patient files.
   - **Hospital** employs **Staff** and maintains patient queues.
