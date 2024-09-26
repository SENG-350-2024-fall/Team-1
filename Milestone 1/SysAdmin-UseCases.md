# Use Cases for System Admins
## Use Case 1: Manage User Accounts

| **Use Case**       | UC1 Manage User Accounts                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description**    | The administrator is responsible for managing employee accounts (e.g., patients, doctors, nurses). This involves creating/removing accounts as needed. |
| **Actors**         | Admin (primary), health system database (secondary), employee database (secondary)                                                                     |
| **Assumptions**    | Admin is logged in and registered.                                                                                                                     |
| **Steps**          | 1. Admin retrieves employee data from employee database<br>2. Admin creates an account for employee<br>3. Admin sends login credentials to employee    |
| **Variations**     | N/A                                                                                                                                                    |
| **Non-Functional** | - Admin-generated credentials must be secure                                                                                                           |
| **Issues**         | N/A                                                                                                                                                    |

## Use Case 2: Provide IT Support

| **Use Case**       | UC2 Provide IT support                                                                                                                                                                                                                                                                                         |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**    | The administrator is responsible for providing IT support to both potential clients and employees.                                                                                                                                                                                                             |
| **Actors**         | Admin (primary), end-users: clients and employees (primary)                                                                                                                                                                                                                                                    |
| **Assumptions**    | A client or employee (end-user) submitted a ticket through the "submit a ticket" option available **after** account creation                                                                                                                                                                                   |
| **Steps**          | 1. Admin accepts a ticket.  <br>2. Admin reviews the details of the issue reported by the end-user.  <br>3. Admin communicates with the end-user for clarification if needed.  <br>4. Admin diagnoses the problem and provides a solution.  <br>6. Admin marks the ticket as solved and notifies the end-user. |
| **Variations**     | -  In some cases, the problem may require escalation to specialized support groups or forwarding to external organizations.<br>- In some cases, emergency IT support may be required in case of after-hours outages. This must be handled by on-call IT.                                                       |
| **Non-Functional** | - Admin must respond to tickets within a set timeframe to ensure rapid support.<br>- End-user feedback should be collected by survey to evaluate the quality of support where applicable.<br>- Emergency IT support should be available 24/7 for emergencies and during the workday for non-emergency.         |
| **Issues**         | Emergency IT support may be required after hours.                                                                                                                                                                                                                                                              |
## Use Case 3: Manage Server Updates

| **Use Case**       | UC3 Manage server updates                                                                                                                                                                                                                                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**    | The administrator is responsible for managing server health by deploying updates regularly                                                                                                                                                                                                                                                   |
| **Actors**         | Admin (primary), Mr Ed Servers: health system db and employee db (Secondary)                                                                                                                                                                                                                                                                 |
| **Assumptions**    | The server has updates available, and the admin has the permissions to manage these updates.                                                                                                                                                                                                                                                 |
| **Steps**          | 1. Admin logs into the server management system.  <br>2. Admin reviews available updates.  <br>3. Admin schedules the update during low-traffic hours.  <br>4. Admin initiates the update process and monitors status.  <br>5. Admin verifies the system functions as expected.  <br>6. Admin logs the update details for auditing purposes. |
| **Variations**     | - Admin may *rollback* an update in cases of error or security.                                                                                                                                                                                                                                                                              |
| **Non-Functional** | - Updates should minimally affect the availability of the system.<br>- The system should maintain performance during and after updates                                                                                                                                                                                                       |
| **Issues**         | N/A                                                                                                                                                                                                                                                                                                                                          |
## Use Case 4: Modify Existing Records 

| **Use Case**       | UC4 Modify Existing Records                                                                                                                                                                                                                                                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**    | The administrator modifies existing patient or employee records in the system based on a request created by employees                                                                                                                                                                                                                                                             |
| **Actors**         | Admin (primary), health system database (secondary)                                                                                                                                                                                                                                                                                                                               |
| **Assumptions**    | There is a request created by an employee to modify patient records                                                                                                                                                                                                                                                                                                               |
| **Steps**          | 1. Admin logs into the system.  <br>2. Admin retrieves the modification request from the employee.    <br>3. Admin accesses the record in patient records.<br>4. Admin makes the necessary changes to the record.  <br>5. Admin saves the changes and logs the modification in the system for audit purposes.  <br>6. Admin notifies the employee of the successful modification. |
| **Variations**     | N/A                                                                                                                                                                                                                                                                                                                                                                               |
| **Non-Functional** | - All modifications must be logged for auditing, ensuring a chain of accountability                                                                                                                                                                                                                                                                                               |
| **Issues**         | N/A                                                                                                                                                                                                                                                                                                                                                                               |

## Use Case 5: Data Backup 

| **Use Case**       | UC5 Data Backup                                                                                                                                                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description**    | The administrator is responsible for ensuring regular data backups and restoring data in case of system failure.                                                                                                                                          |
| **Actors**         | Admin (primary), Mr Ed Servers (Secondary)                                                                                                                                                                                                                |
| **Assumptions**    | The admin has access to backup tools, the admin has the relevant permissions to be able to manage backups and some backup schedule exists.                                                                                                                |
| **Steps**          | 1. Admin logs into the server management system.  <br>2. Admin checks the schedule for the next backup or manually initiates a backup.  <br>3. Admin verifies the successful completion of the backup process.  <br>4. Admin logs the backup for auditing |
| **Variations**     | - Admin needs to recover data from a backup                                                                                                                                                                                                               |
| **Non-Functional** | - Backups must be reliable, regularly scheduled and with no data loss<br>- Backup operations should minimally impact system functionality<br>- Backups must be stored securely and encrypted.                                                             |
| **Issues**         | - Possible corruption during backups                                                                                                                                                                                                                      |

```UML
@startuml
left to right direction

actor "System Admin" as SysAdmin

package Sys_Admin_Roles{
    SysAdmin --> (Provide IT Support)
    SysAdmin --> (Manage Server Updates) 
    SysAdmin --> (Modify Existing Records)
    SysAdmin --> (Data Backup)

	(Provide IT Support) ..> (Manage User Accounts): "includes" 
	(Provide IT Support) ..> (Modify Existing Records): "includes" 

}

@enduml
```

## Use Case Diagram
Model System Admin use cases

![[SysAdmin_UML.png]]