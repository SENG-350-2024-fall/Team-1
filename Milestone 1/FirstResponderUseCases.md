## Use Case #1: View patient details

| **Use Case**    | 1 View patient details |
| --- | --- |
| **Description** | The first responder should be able to view the details of the patient so they can make any necessary preparations. |
| **Actors**      | First responder, patient |
| **Assumptions** | - First responders are logged in.<br> - The system is operational and accessible. |
| **Steps**       | 1. First responders sees urgent patient in system.<br>2. First responder views patient details to see their symptoms and medical history. |
| **Non-Functional** | - USABILITY: The first responder must be able to view the patient details within 5 seconds of logging in.<br>- SECURITY: As first responders have higher level access to private medical records they must be secure |

## Use Case #2: Check patient notifications

| **Use Case**    | 2 Check patient notifications |
| --- | --- |
| **Description** | First responders should be able to view notifications related to the patient, such as updated triage results or ED preparation status. |
| **Actors**      | First responder |
| **Assumptions** | - Notifications are timely and accurate.<br>- First responders are connected to the network. |
| **Steps**       | 1. First responders receive notification. <br>2. First responders check notification for updates on patient’s condition or ED status. |
| **Non-Functional** | - TIMELINESS: Notifications must arrive in real-time to ensure proper response.<br>- RELIABILITY: Notifications must be delivered without delay. |
| **Issues**      | 	- Missed notifications due to poor connectivity |

## Use Case #3: Perform check-in with patient

| **Use Case**    | 3 Perform check-in with patient |
| --- | --- |
| **Description** | First responders should be able to check in with the patient to confirm their condition or collect additional information. |
| **Actors**      | First responder, patient |
| **Assumptions** | - Reliable communication with the patient.<br>- Patient is conscious and able to provide information. |
| **Steps**       | 1. First responder initiates contact.<br>2. First responder collects additional information from the patient. |
| **Variations**  | #2. Patient is unresponsive, and first responder follows alternative emergency protocols. |
| **Non-Functional** | - ACCESSIBILITY: The check-in process must be quick and easy (5 minutes to hand over the patient).<br>- SECURITY: All communication must be encrypted. |
| **Issues**      | - Patient may be unresponsive or unable to provide necessary information to provide a thorough check. |

## Use Case #4: Access patient GPS location

| **Use Case**    | 4 Access patient GPS location |
| --- | --- |
| **Description** | First responders should be able to access the patient’s GPS location to track their whereabouts during emergencies. |
| **Actors**      | First responder, patient |
| **Assumptions** | - The patient has location sharing enabled.<br>- GPS services are operational. |
| **Steps**       | 1. First responder opens GPS tracking.<br>2. First responder verifies patient’s location. |
| **Variations**  | 4a. GPS data may be unavailable (poor connection, patient doesn't have their location shared). |
| **Non-Functional** | - ACCURACY: GPS must be precise within 100 meters.<br>- TIMELINESS: Location data must update in real-time. |

## Use Case #5: Update ED staff with patient details

| **Use Case**    | 5 Update ED staff with patient details |
| --- | --- |
| **Description** | First responders should be able to update ED staff with the latest patient details during transport. |
| **Actors**      | First responder, Nurse, Doctor |
| **Assumptions** | - Reliable communication between first responders and ED staff. |
| **Steps**       | 1. First responder updates patient status in the system.<br>2. ED staff review updated details and prepare for the patient's arrival. |
| **Variations**  | #5. ED staff may request additional information based on patient’s critical status in order to prepare for their arrival. |
| **Non-Functional** | - RELIABILITY: Data must transfer without interruption.<br>- TIMELINESS: Updates should arrive instantly for timely decision-making. |

## Use Case #6: Transfer patient to ED care

| **Use Case**    | 6 Transfer patient |
| --- | --- |
| **Description** | First responders should be able to transfer patients into the ED system once they arrive at the hospital. |
| **Actors**      | First responder, Nurse, Doctor |
| **Assumptions** | - System is operational and connected to the ED. |
| **Steps**       | 1. First responder arrives at ED.<br>2. First responder transfers patient information into the system. |
| **Non-Functional** | - EFFICIENCY: Transfer must be completed within 2 minutes.<br>- USABILITY: The transfer process should be straightforward. |

## Use Case #7: Check ED load/wait times

| **Use Case**    | 7 Check ED load/wait times |
| --- | --- |
| **Description** | First responders should be able to check the load and wait times at nearby EDs to determine the best destination for the patient. |
| **Actors**      | First responder, Nurse, Doctor |
| **Assumptions** | - ED systems are accurately reporting their load.<br>- Data is accessible to first responders. |
| **Steps**       | 1. First responder checks ED load through the system.<br>2. First responder selects the ED based on load and wait times. |
| **Variations**  | #2 First responder may want to select a different ED depending on the situation (ie may travel slightly further for a lesser wait time) |
| **Non-Functional** | - ACCURACY: Wait times needs to be accurate so first responders can make the appropriate decision. |