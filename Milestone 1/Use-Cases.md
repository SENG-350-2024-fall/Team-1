## Use Case #1: Meghan
User checks wait times for hospitals. 

| **Use Case**    | 1. Getting Emergency Department Wait Times |
| --- | --- |
| **Description** | Patient wants to know the wait time for a given hospital.|
| **Assumptions** | The wait time is available for the given hospital (ie. Has been estimated and updated based on ER conditions).<br> The system is running.<br> User is logged in. |
| **Actors**      | Patient (primary), Hospital wait time api|
| **Steps**       | 1. Patient selects the look up wait time <br> 2. System prompts the patient to enter the name of the hospital <br> 3. Patient provides hospital name <br> 4. The system shows the wait time for the given hospital|
| **Variations**  |  |
| **Non-Functional**   |Availability: Wait time is available 99.9% of the time <br>Scalability: must be able to huddle multiple hospitals <br>Usability: the wait times should be easy to find regardless of how technical the user is. <br>Accessibility: the times should be displayed such that anyone can understand them. |
| **Issues**      | How do we get the estimated wait time? How can we assure wait time is accurate? What gets displayed if we don’t have a wait time available? |

## Use Case #2: Arden
User Registration & Create a Profile: for registration login, logout, register, guest login; for create profile can have medical history and information, potentially medical insurance, emergency contact

| **Use Case**    | 2. User_login                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | User logs in using their profile                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Assumptions** | Is not logged in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Actors**      | User (primary)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Steps**       | 1. User clicks "Log in with BC Services Card app" button <br>2. REPEAT <br>&nbsp;&nbsp;&nbsp;&nbsp;1.1 User gets prompted to pair their BC Services Card App with a six symbol code on their screen. <br>&nbsp;&nbsp;&nbsp;&nbsp;1.2 User enters six symbol code from application into BC Services Card App. <br>UNTIL user inputs correct code **or** inputs incorrect code 3 times. <br>3. IF correct code THEN 3.1 User is brought to the main page of the application. <br>&nbsp;&nbsp;&nbsp;&nbsp;3.2 ELSE User is unable to log in |
| **Issues**      | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

| **Use Case**    | 2.1 User_logout                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------- |
| **Description** | User logs out                                                                                      |
| **Assumptions** | Is logged in                                                                                      |
| **Actors**      | User (primary)                                                                                    |
| **Steps**       | 1. User clicks the log out option on the application. <brl>2. User is logged out of their session |
| **Variations**  | **#1.** User exits out of the application                                                         |
| **Issues**      | How does application process unfinished virtual triage processes?                                 |
|                 |                                                                                                   |

##### Comments: 
I realized BC Services Card app is a thing and it has access to medical records.

## Use Case #3: Konrad
Undergo Virtual Triage: input symptoms, check urgency, capacity, location, patient profile & history

| **Use Case**    | 3. Undergo Virtual Triage                                                                                                                                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | User provides a description of their symptoms, along with an optional image. The system will use this information in conjunction with their medical history and local hospital wait times to make a recommendation.                                          |
| **Assumptions** | User is logged in and registered.                                                                                                                                                                                                                            |
| **Actors**      | User (primary), health system database (secondary)                                                                                                                                                                                                           |
| **Steps**       | 1. User provides their symptoms<br>2. User is recommended a course of action by health system database based on symptoms and medical history.<br>3. User takes the recommended course of action: visit ED, wait to visit ED, phone call, acquire medication. |
| **Variations**  | N/A                                                                                                                                                                                                                                                          |
| **Issues**      | Non-registered members should not be able to use the triage system. Otherwise, they would be required to provide medical records or connect health card to make the best estimation *during* a potentially emergency situation.                              |

note: add option for patient to include photo, also add option to change emergency response and travel radius based on physical condition

## Use Case #4: Jordan
Treatment Directions: suggested course of action (home remedy, visit general practitioner, doctor, ER, etc.), further virtual contact with medical professional or in-person medical followup

| **Use Case**         | 4. Treatment Directions |
|---|---|
| **Primary Actors**                            | Patient, Mister ED Virtual Triage System |
| **Secondary Actors (if needed)**              | Medical Professional                     |
| **Use Case Description** | The system provides treatment directions after a virtual triage process. Recommendations include home remedies, visiting a general practitioner, contacting a doctor, or going to the emergency room. The system may suggest further virtual or in-person follow-ups. |
| **Preconditions** | - The patient has registered and completed the virtual triage. <br> - The system is operational, and patient data has been inputted.|
| **Postconditions** | - Patient receives treatment directions based on triage results. <br> - Recommendation for further virtual consultation or in-person follow-up.   |
|**Steps**| 1. Patient completes the virtual triage. <br> 2. System analyzes patient input and assesses the patient's condition. <br> 3. System provides treatment directions (home remedy, GP visit, doctor, ER, etc.). <br> 4. If necessary, system suggests further virtual contact or an in-person follow-up with a medical professional. |
|**Variations**|2.1. If the system cannot make a decision, it escalates the case to a human medical professional for review. |
|**Exceptions**| - Incomplete or inconsistent data leads to an error message requesting further details. <br> - System failure or technical issue prevents assessment, prompting the patient to retry later or seek immediate help. |

note: notification with queue based on priority, automatically adds them to queue based on symptoms after triage is completed if it's determined they should receive examination
note: patient should have the option to remove themselves from the queue
 
## Use Case #5: Meghan
Notification to Go to Hospital: which hospital (based on location, urgency, wait times, etc.) and directions
| **Use Case**    | 5. ED visit time notification |
| --- | --- |
| **Description** | Patient gets notified when it is their turn to visit the ED.|
| **Assumptions** | Patient is logged in to system<br>Patient has been triaged<br>Mister MD determined patient must visit a hospital<br>Patient has set a travel range in their profile/or in triage and can physically get to those hospitals.<br>Wait times are available for hospitals in range<br>Patient has allowed push notifications<br>System refers patients to the hospital that is closest to them(in their travel range) with the lowest wait time.<br> there is at least one Emergency department in the users travel range<br> User has allowed push notifications (text or call)|
| **Actors**      | Patient (primary), text message/call api|
| **Steps**       | 1.Patient selects log in<br> 2.System prompts patient to enter account credentials<br> 3.Patient provides account credentials<br> 4.System authenticates patient<br> 5.Patient selects notifications<br> 6.System displays notifications by recency.<br> 7.Patient sees notification that it is their turn to visit the ED at specified hospital|
| **Variations**  | Patient receives push notification call or text that it is their turn to visit a specified hospital.  |
| **Non-Functional**   |Availability: this service must be available 99.9% of the time so users are not waiting. indefinitely to be called to the ED<br>Scalability: must be able to handle multiple hospitals and patients <br>Usability: users should be able to find their notification <br>Recoverability: if the system crashes how do we regain the queue<br>Accessibility: everyone should be able to receive the notifications<br>Security: the notification should not contain more sensitive information than is needed and the notifications should go to the correct person. |
| **Issues**      | What happens if a user doesn’t go to hospital when notified?<br>Can a person move down in priority if they have more serious conditions walking into the ER? How does that show? What If the notification has already gone out?|

## Use Case #6: Tom
Emergency Escalation

| **Use Case 6**           | **Emergency Escalation**                                                                                                                                       |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description**        | Any patient that requires immediate medical attention due to their symptoms can have first responders dispatched to them through the app.           |
| **Primary Actor**      | Patient                                                                                                                                          |
| **Secondary Actors**   | Doctor, Nurses, First Responders                                                                                                                 |
| **Assumptions**        | - The patient is logged into the app. <br> - The patient is sharing user data with the app. <br> - Local first responders are available.          |
| **Steps**              | 1. Patient logs into MisterEd. <br> 2. Patient enters their symptoms in MisterEd. <br> 3. If the system detects life-threatening symptoms, it will contact first responders with the symptoms. <br> 4. If first responders are available, they can be dispatched to the user. <br> 5. Doctors and Nurses at the nearest hospital are notified of the patient’s symptoms and expected arrival. |
| **Variations**         | 1. If the patient is not logged in, we will not contact first responders automatically, but give them the option to call first responders. <br> 2. If location services are not shared or the app cannot determine the location, we do not automatically dispatch but give the user the option to call first responders. |
| **Non-Functional Requirements** | - **Security**: Patient data must comply with local privacy regulations (e.g., PIPEDA). <br> - **Performance**: Must escalate emergencies within 10 seconds. |
| **Issues**             | - Handling incorrect or intentionally wrong data input by patients, or false positives in symptom detection. <br> - Legal concerns for automated emergency recommendations. |

