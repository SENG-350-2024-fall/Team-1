# Healthcare System ERD Description

This ERD represents a comprehensive healthcare system focusing on patient care, professional roles, and hospital management. Here's a breakdown of the entities and their relationships:

## Entities

1. **FirstResponder**
   - Attributes: Name, ID (key), Position, Location, OnCallStatus

2. **OnlineNurse**
   - Attributes: Name, ID (key), Position, ShiftSchedule, Available

3. **HealthcareProfessional**
   - Attributes: Specialization, ShiftSchedule, OnCallStatus, Username, Password

4. **Patient**
   - Attributes: Name, PHN (key), HealthCareCardNumber, Location, Gender, Birthdate, Occupation, HealthRecords, queuePosition

5. **SystemAdmin**
   - Attributes: Name, ID (key), Position, Schedule

6. **Symptom** (weak entity)
   - Attributes: Symptom_Info

7. **Hospital**
   - Attributes: Name, ID (key), Location, EstimatedWaitTime, PhoneNumber, Capacity

8. **TriageReport** (weak entity)
   - Attributes: ReportID (key), ReportContent, DateCreated

## Relationships

1. **exhibitsSymptoms**: 
   - Between Patient (1) and Symptom (N)

2. **provideTechSupport**:
   - Between SystemAdmin (1) and Patient, OnlineNurse, HealthcareProfessional, FirstResponder (N)
   - Attribute: supportTicket

3. **createsTriageReport**:
   - Between OnlineNurse (1) and TriageReport (N)
   - Also involves Patient (1)

4. **treatsPatient**:
   - Between HealthcareProfessional (N) and Patient (N)

5. **triagesPatient**:
   - Between OnlineNurse (1) and Patient (N)
   - Attribute: recommendation

6. **assistsPatient**:
   - Between FirstResponder (N) and Patient (N)

7. **employedAt**:
   - Between Hospital (1) and HealthcareProfessional, OnlineNurse, FirstResponder, SystemAdmin (N)

## Overview

1. The system revolves around the Patient entity, which is central to most relationships.
2. Healthcare professionals are categorized into distinct roles: FirstResponder, OnlineNurse, and HealthcareProfessional, each with specific responsibilities.
3. The SystemAdmin provides technical support to all user types.
4. The Hospital entity represents the physical location where most healthcare activities occur.
5. Triage reports and symptoms are treated as weak entities, likely dependent on the Patient entity for their existence.
6. The system accounts for both in-person (treatsPatient, assistsPatient) and remote (triagesPatient) patient care.

