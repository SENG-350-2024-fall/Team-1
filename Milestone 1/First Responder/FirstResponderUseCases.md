## Use Case #1: View patient details

This use case is to ensure that fist responders can access patient information efficiently. The first responder uses MisterEd system to view information about the patient such as the symptoms they are experiencing as well as their medical history. This will allow them to make an informed decision to care for the patient.

| **Use Case**    | 1 View patient details |
| --- | --- |
| **Description** | The first responder should be able to view the details of the patient so they can make any necessary preparations. |
| **Actors**      | First responder, patient |
| **Assumptions** | - First responders are logged in.<br> - The system is operational and accessible. |
| **Steps**       | 1. First responders sees urgent patient in system.<br>2. First responder views patient details to see their symptoms and medical history. |
| **Non-Functional** | - USABILITY: The first responder must be able to view the patient details within 5 seconds of logging in.<br>- SECURITY: As first responders have higher level access to private medical records they must be secure |

## Use Case #2: Check patient notifications

This use case is to ensure that the first responders are notified of urgent patients. These updates are to ensure that if a patient has been marked as high risk a first responder can assist them.

| **Use Case**    | 2 Check patient notifications |
| --- | --- |
| **Description** | First responders should be able to view notifications related to the patient, such as updated triage results or ED preparation status. |
| **Actors**      | First responder |
| **Assumptions** | - Notifications are timely and accurate.<br>- First responders are connected to the network. |
| **Steps**       | 1. First responders receive notification. <br>2. First responders check notification for updates on patient’s condition or ED status. |
| **Non-Functional** | - TIMELINESS: Notifications must arrive in real-time to ensure proper response.<br>- RELIABILITY: Notifications must be delivered without delay. |
| **Issues**      | 	- Missed notifications due to poor connectivity |

## Use Case #3: Perform check-in with patient

The first responder checks in with the patient to confirm their current condition and determine further steps. They can consider specific care needs of the patient before transporting them to the ED.

| **Use Case**    | 3 Perform check-in with patient |
| --- | --- |
| **Description** | First responders should be able to check in with the patient to confirm their condition or collect additional information. |
| **Actors**      | First responder, patient |
| **Assumptions** | - Reliable communication with the patient.<br>- Patient is conscious and able to provide information. |
| **Steps**       | 1. First responder initiates contact.<br>2. First responder collects additional information from the patient. |
| **Variations**  | - Patient is unresponsive, and first responder follows alternative emergency protocols. |
| **Non-Functional** | - ACCESSIBILITY: The check-in process must be quick and easy (5 minutes to hand over the patient).<br>- SECURITY: All communication must be encrypted. |
| **Issues**      | - Patient may be unresponsive or unable to provide necessary information to provide a thorough check. |

## Use Case #4: Access patient GPS location

In the case that a patient is non-responsive they can access the patients GPS location. This will allow the first responders to check up on the patient if they have gone un conscious or are immobile and require to be transported to the ED.

| **Use Case**    | 4 Access patient GPS location |
| --- | --- |
| **Description** | First responders should be able to access the patient’s GPS location to track their whereabouts during emergencies. |
| **Actors**      | First responder, patient |
| **Assumptions** | - The patient has location sharing enabled.<br>- GPS services are operational. |
| **Steps**       | 1. First responder opens GPS tracking.<br>2. First responder verifies patient’s location. |
| **Variations**  | - GPS data may be unavailable (poor connection, patient doesn't have their location shared). |
| **Non-Functional** | - ACCURACY: GPS must be precise within 100 meters.<br>- TIMELINESS: Location data must update in real-time. |

## Use Case #5: Update ED staff with patient details

This use case allows first responders to update the ED staff of their arrival time and status of the patient when they are transporting the patient and treating the patient.

| **Use Case**    | 5 Update ED staff with patient details |
| --- | --- |
| **Description** | First responders should be able to update ED staff with the latest patient details during transport. |
| **Actors**      | First responder, Nurse, Doctor |
| **Assumptions** | - Reliable communication between first responders and ED staff. |
| **Steps**       | 1. First responder updates patient status in the system.<br>2. ED staff review updated details and prepare for the patient's arrival. |
| **Variations**  | - ED staff may request additional information based on patient’s critical status in order to prepare for their arrival. |
| **Non-Functional** | - RELIABILITY: Data must transfer without interruption.<br>- TIMELINESS: Updates should arrive instantly for timely decision-making. |

## Use Case #6: Transfer patient to ED care

Upon arrival at the hospital the first responders transfers the patient as well as their information to the ED staff. This ensures that the ED staff have all relevant information to care for the patient. Once patient is trasfered to ED staff, first responders should no longer have access to patient files.

| **Use Case**    | 6 Transfer patient |
| --- | --- |
| **Description** | First responders should be able to transfer patients into the ED system once they arrive at the hospital. |
| **Actors**      | First responder, Nurse, Doctor |
| **Assumptions** | - System is operational and connected to the ED. |
| **Steps**       | 1. First responder arrives at ED.<br>2. First responder transfers patient information into the system. |
| **Non-Functional** | - EFFICIENCY: Transfer must be completed within 2 minutes.<br>- USABILITY: The transfer process should be straightforward. |

## Use Case #7: Check ED load/wait times

The first responders should be able to check the current load and wait times ad different EDs located in their area. This will allow the first responders to make informed decision about which ED they should go to depending on the severity of the patient and their needs.

| **Use Case**    | 7 Check ED load/wait times |
| --- | --- |
| **Description** | First responders should be able to check the load and wait times at nearby EDs to determine the best destination for the patient. |
| **Actors**      | First responder |
| **Assumptions** | - ED systems are accurately reporting their load.<br>- Data is accessible to first responders. |
| **Steps**       | 1. First responder checks ED load through the system.<br>2. First responder selects the ED based on load and wait times. |
| **Variations**  | - First responder may want to select a different ED depending on the situation (ie may travel slightly further for a lesser wait time) |
| **Non-Functional** | - ACCURACY: Wait times needs to be accurate so first responders can make the appropriate decision. |

## Use Case #8: Log In

The first responder needs to be able to log in in order to use application

| **Use Case**    | 8 Log In |
| --- | --- |
| **Description** | A first responder accesses the MisterEd system to authenticate their identity and gain access to the patient data |
| **Actors**      | First responder |
| **Assumptions** | - First responder has valid credentials. <br> - The system is operational and accessible  |
| **Steps**       | 1. First responder navigates to the login page. <br> 2. First responder selects the First Responder Portal. <br> 3. First responder enters their credentials. <br> 4. First responder is granted access to system if authenticated |
| **Variations**  | - If authentication fails, the user is prompted to retry or reset their password. |
| **Non-Functional** | - The system should respond within 2 seconds for successful login.<br>- Secure encryption of user credentials must be maintained. |

## Use Case #8: Log Out

The first responder needs to be able to log out when done using system


| **Use Case**    | 9 Log Out |
| --- | --- |
| **Description** | The First Responder logs out from the MisterED system. |
| **Actors**      | First responder |
| **Assumptions** | - The First Responder is authenticated and logged in with valid credentials (username and password).<br> - The system is operational and accessible. |
| **Steps**       | 1. User locates the logout button on their main page/dashboard.<br>2. User clicks logout.<br>3. System logs the the user out and displays a successful logout message and returns them to the landing/login page |
| **Variations**  | - If the user is inactive for an hour the system will automatically log out the user. |
