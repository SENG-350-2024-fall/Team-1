# Level 0 Data Flow Diagram

The wiki for this data flow model can be found [here](https://github.com/SENG-350-2024-fall/Team-1/wiki/Data-Flow-Models#level-0-data-flow-diagram).

You can view an interactive version of the Level 0 DFD at the following link: [Lucidchart Level 0 DFD](https://lucid.app/lucidchart/52753124-a834-4edb-8beb-e425640bbf18/edit?viewport_loc=305%2C445%2C2002%2C1182%2C0_0&invitationId=inv_087923eb-33e6-4ad2-b98c-fb21ac9298ee)

The Level 0 DFD delves into the system's core processes, showing the flow of data within each major component of the system. We have broken the system's operations down into five major processes:

**1.0 - User Authentication & Account Management**
> This process encompasses the MFA login process for users and staff. Users will also be prompted to login/register with their BC Service Card. Here they will also be able to create and manage their profile information.

**2.0 - Virtual Patient Triage Management**
> This process illustrates how patients can receive virtual triage. They will be prompted to input their symptoms, which will be sent to the Online Nurse alongside their medical information attached to their profile via the BC Service Card. Patients will receive a triage report accompanied by follow-up treatment directions as the Online Nurse places them into the appropriate ED queue. The system will deliver a notification to the patient when they have reached the front of the ED queue and it is their turn. If necessary, the Online Nurse can escalate the patient's case to the First Responder, who can use the MisterED system to view the triage report and medical information, patient GPS location, and nearby ED information ahead of time.

**3.0 - ED & Queue Information**
> This process is responsible for maintaining both the ED queue and the information of the ED such as the current wait time / queue length and the location. Users, Online Nurses, and First Responders will be able to request the wait time and location of a given ED. Patients can view their position in the ED queue, and the Online Nurse can place a patient in the queue after completing their triage according to the severity of their report results. Doctors and Nurses on-site can update the ED queue when either a patient walks into the ED or they remove a patient from the queue for treatment. 

**4.0 - Patient Treatment**
> This process involves the treatment of patients in the ED and by First Responders. The system will provide the patient's medical information and the most recent triage report. The First Responders can update the triage report with more accurate findings once they assess and begin to treat the patient en-route to the ED. Doctors and Nurses at the ED can view the most recent triage report before attending to a patient, and after the physical treatment they can submit the new medical records to the system, or submit a prior record modification for approval by a System Administrator.

**5.0 - System Maintenance**
> This process ensures that both the system and all important data is secured and taken care of. System Administrators can perform regular system updates and data backups during common downtimes. They can also provide IT Support and respond to tickets opened by users and employees, generally related to accounts or front-facing issues within the system. They can conduct audits to ensure that there is no breach of privacy or elevation of privilege taking place, and can also ensure that important data is securely encrypted and cannot be accessed by unauthorized users.


![Level 0 DFD (2)](https://github.com/user-attachments/assets/e1290ac8-4463-4d78-9b17-93a53db7f7bd)