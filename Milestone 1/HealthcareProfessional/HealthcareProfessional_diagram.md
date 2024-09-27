## PlantUML Use Case Diagram - Actor: Online Nurse
![image](https://github.com/user-attachments/assets/a8fa3538-115a-4c24-8569-20ae6b042f73)


## PlantUML Code:

```
@startuml
actor "Healthcare Professional" as HP
left to right direction
rectangle "Mister Ed System" {
    usecase "Log In" as UC1
    usecase "View Patient Symptoms/Triage Report" as UC2
    usecase "Edit Triage Report" as UC3
    usecase "View Urgent Care Queue" as UC4
    usecase "Add Patient to Queue" as UC5
    usecase "Add Patient Records" as UC6
    usecase "Assign Patient from queue to self" as UC7
    usecase "Log out" as UC8
   
}

HP --> UC1
HP --> UC2
HP --> UC4
HP --> UC5
HP --> UC6
HP --> UC7
HP --> UC8


UC2 <.. UC3 : <<extend>>
@enduml
```
