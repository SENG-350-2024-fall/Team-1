# MrED Deployment Diagram Description

This deployment diagram represents a healthcare system architecture, focusing on ED management. The system is composed of three main nodes: Hospital Systems, a Central Server, and User Devices, with an additional cloud component for the BC Public Health DB.

## Cloud Component: BC Public Health DB

This cloud-based database contains:
- Provincial Health Number (PHN)
- Patient Records
- API for data access

It has a secure connection for data exchange with the Hospital Systems and a secure connection with the Central Server.

## Main Nodes

### 1. Hospital Systems
This node represents the on-premises hospital infrastructure:
- Components:
  - Hospital Staff
  - Online Nurse
  - Hospital Workstations
- Database (Hospital Database):
  - Patient Records
  - Staff Records
  - ED Waiting List

### 2. Central Server
This node acts as the core of the system:
- Components:
  - System Admin
- Database (Central Database):
  - Load Balancer
  - Health Records
  - User Data

The Central Server has an internal network connection to the Hospital Systems.

### 3. User Devices
This node represents various user interfaces:

#### Mobile App:
- GPS Location
- Symptom Checker
- Wait Time Check

#### Web App:
- Symptom Checker
- Wait Time Check

#### Shared Components (Mobile and Web):
- Patient Login
- Staff Login
- Provide Recommendation
- Call
- Chat

User Devices connect to the Central Server via a secure external connection.

## Overview:

1. User Authentication:
   - Patient and Staff logins authenticate against the Central Database

2. Symptom Checking:
   - Both mobile and web symptom checkers query the Central Database

3. Wait Time Checking:
   - Mobile and web wait time checkers access the ED Waiting List in the Hospital Database

4. Recommendations:
   - The recommendation component fetches data from the Central Database

5. Communication with Online Nurse:
   - Call and Chat components connect to the Online Nurse in the Hospital Systems

6. Data Exchange:
   - Secure data exchange occurs between the Hospital Systems and the BC Public Health DB
