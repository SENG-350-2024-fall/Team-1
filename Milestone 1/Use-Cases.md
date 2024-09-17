## Use Case #1: Meghan
Check Wait Times

## Use Case #2: Arden
User Registration & Create a Profile: for registration login, logout, register, guest login; for create profile can have medical history and information, potentially medical insurance, emergency contact

| **Use Case**    | 2. User_login                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | User logs in using their profile                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Assumptions** | Is not logged in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Actors**      | User (primary)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Steps**       | 1. User clicks "Log in with BC Services Card app" button <br>2. REPEAT <br>&nbsp;&nbsp;&nbsp;&nbsp;1.1 User gets prompted to pair their BC Services Card App with a six symbol code on their screen. <br>&nbsp;&nbsp;&nbsp;&nbsp;1.2 User enters six symbol code from BC Services Card App into the application. <br>UNTIL user inputs correct code **or** inputs incorrect code 3 times. <br>3. IF correct code THEN 3.1 User is brought to the main page of the application. <br>&nbsp;&nbsp;&nbsp;&nbsp;3.2 ELSE User is unable to log in and they must reset their BC Services Card App |
| **Variations**  | **#1.** User clicks "Log in as guest"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Issues**      | Should a user log in before viewing application or start off as guest                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

| **Use Case**    | 2.1 User_logout                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------- |
| **Description** | User logs in                                                                                      |
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
| **Description** | User provides a description of their symptoms. The system will use this information in conjunction with their                                                                                                                                                |
| **Assumptions** | User is logged in and registered.                                                                                                                                                                                                                            |
| **Actors**      | User (primary), health system database (secondary)                                                                                                                                                                                                           |
| **Steps**       | 1. User provides their symptoms<br>2. User is recommended a course of action by health system database based on symptoms and medical history.<br>3. User takes the recommended course of action: visit ED, wait to visit ED, phone call, acquire medication. |
| **Variations**  | N/A                                                                                                                                                                                                                                                          |
| **Issues**      | Non-registered members should not be able to use the triage system. Otherwise, they would be required to provide medical records or connect health card to make the best estimation *during* a potentially emergency situation.                              |



## Use Case #4: Jordan
Treatment Directions: suggested course of action (home remedy, visit general practitioner, doctor, ER, etc.), further virtual contact with medical professional or in-person medical followup

## Use Case #5: Meghan
Notification to Go to Hospital: which hospital (based on location, urgency, wait times, etc.) and directions

## Use Case #6: Tom
Emergency Escalation
