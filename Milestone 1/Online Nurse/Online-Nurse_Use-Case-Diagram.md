## PlantUML Use Case Diagram - Actor: Online Nurse

![image](https://github.com/user-attachments/assets/59b507f2-be20-45bc-a1de-2267e485d885)

[You can view the UCD here also](//www.plantuml.com/plantuml/png/RP5HImCn3CVVyod2tZVSvlOWunZe2OBECNJlvIvt1cwj93bqYD_Tw-Xa5HyA_PFVBwJfMis9zOSEEceCBQ1m-sPOir1b73ouoeBWw8dLICexVFOTUy9DBqeZT8e-tY3YphSTuI_v1O3OArLE2KUFeML_4bvlh_uKGc-fCeLCsZDzuDOPapTyy4sGWujJ9NgMmI_2hgKpdf3v9L5gvJfd5DzPxd0h78JjcD3hhDic63V7SxTex5dP1Y_X2_YlzQLmpwA6EzBtu6kIv2q1lW5EMyFnk8ZhoECiZtCO3gucapWYtk1gHPz6ljQYoC557fTvd0Ai1sluwXy0)



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
UC3 <.. UC4 : <<extends>>

nurse --> UC5

nurse --> UC6

nurse --> UC1

@enduml
```
