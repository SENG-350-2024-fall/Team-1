## PlantUML Use Case Diagram - Actor: Online Nurse

![image](https://github.com/user-attachments/assets/7abe9309-ffc1-48e2-8083-c4f9e02f4b11)

[You can view the UCD here also](//www.plantuml.com/plantuml/png/RP5FIyD04CNlyoaUkRVOF-t1WnGqWg2r5ErzIIPn8DsLsGbQnEzkKXBfYeU5USplzmwpcsXEhJqsr71bi02L-irGYd9X4Zovme8YUv9ehFaTddqZdh5jDN865-7xYNhS-RfX_99VH40RkN2HaJs6MlnPUBsz-hC8hGsR6INIGVW3EsV2tl3Wgw37BeInPvx0BogkvX4VaCKbaSV2DSuO5f3liLC9AdOQq6NIjWqcrMbiwus3HB7E6_0L_Ljz8ToBHiEUutlm9UlWhOc-YSvNmsHoqvyZZVCqBgXxc4xxUObhyAUnBsCAhTAuJkECDftI_V8F)



## PlantUML Code:

```
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
```
