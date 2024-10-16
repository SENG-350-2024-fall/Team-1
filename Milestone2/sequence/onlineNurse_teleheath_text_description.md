the process of an **OnlineNurse** arranging a telemedicine appointment for a patient is shown in this diagram.

### Sequence Diagram Description:

1. **Login Process**:
   - The **OnlineNurse** begins by requesting a `login(username, password, StaffId)` to the **Login** system.
   - The **Login** system activates and authenticates the Online Nurse.
   - After the authentication is completed successfully, the **Login** system deactivates.

2. **Retrieving the Next Patient**:
   - The **OnlineNurse** requests the next patient in line by sending `popNextPatient()` to the **PatientQueue**.
   - The **PatientQueue** processes the request, returns the next patient `returnPatientDetails(patient)` containing the patient's info.
   - After providing the patient details, the **PatientQueue** deactivates.

3. **Reviewing the Triage Report**:
   - The **OnlineNurse** sends a request `reviewTriageReport(patient)` to the **TriageReport** system to view the patient's triage report.
   - The **TriageReport** system activates and returns the patient's report with `displayTriageReport(symptoms, history)`, which has the patient's symptoms and medical history.
   - Once the report is displayed, the **TriageReport** system deactivates.

4. **Checking Doctor Availability**:
   - The **OnlineNurse** checks for an available doctor by sending `checkDoctorAvailability(patient)` to the **Staff** system.
   - The **Staff** system activates and returns the an available doctor.
   - The **Staff** system deactivates after returning the information.

5. **Scheduling the Telemedicine Appointment**:
   - The **OnlineNurse** sends the appointment scheduling request `scheduleTelemedicineAppointment(patient, date, doctor)` to the **Scheduler**.
   - The **Scheduler** activates and does the following:
     - Sends a notification to the patient with `NotifyAppointmentScheduled(doctor, date)`.
     - Sends a notification to the doctor with `NotifyAppointmentScheduled(patient, date)`.
     - Confirms to the **OnlineNurse** that the appointment was successfully added with `ConfirmAppointmentAdded()`.
   - After confirming the appointment the **Scheduler** deactivates.

### Key Participants:
- **OnlineNurse**: reviews a patient's triage report and schedules a telemedicine appointment.
- **Login**: Authenticates the nurse's login.
- **PatientQueue**: Provides the details of the next patient in the queue.
- **TriageReport**: Gets the patient's symptoms and medical history.
- **Staff**: Provides info about available doctors for an appointment.
- **Scheduler**: Schedules the telemedicine appointment and notifies the patient and doctor of the confirmed date and time.

This diagram shows the role of the OnlineNurse in handling patient triage, and scheduling telemedicine appointments within the Mister ED system.
