PlantUML Use Case Diagram
Actor: Online Nurse

[image]


PlantUML Code:

@startuml
left to right direction
actor "MisterED Online Nurse" as nurse
rectangle MisterED {

  usecase "Login" as UC0
  usecase "Logout" as UC1


  usecase "View Patient Information" as UC2

  usecase "Triage Patient" as UC3
  usecase "Escalate to ER Priority" as UC4

  usecase "Notify Patient to Visit ER" as UC5

  usecase "Escalate Patient to First Responder" as UC6

}

nurse --> UC0

nurse --> UC2

nurse --> UC3
UC3 ..> UC4 : extends

nurse --> UC5

nurse --> UC6

nurse --> UC1

@enduml