# ActiveKids Sports Training School Database Project

## Project Overview
This project was completed as part of the **CP2404 Database Modelling** course at James Cook University. The project involves designing a conceptual database model using MySQL Workbench based on a business scenario for a sports training school, **ActiveKids**. The aim is to integrate multiple independent branches into a centralized database system, allowing for efficient management of staff, customers, training sessions, and equipment.

### Scenario Overview
ActiveKids is a group of sports training schools in Singapore, and the objective is to design a database that centralizes the management of the branches, staff, children, training sessions, equipment, and customer interactions. The database will support operational tasks like report generation for HR purposes, tracking training sessions, issuing invoices, and managing equipment assigned to staff.

## Goals
The key objectives of this project are to:
- **Design a Database**: Develop an Entity-Relationship Diagram (ERD) using MySQL Workbench to model the centralized system.
- **Normalize Data**: Apply database normalization techniques to minimize redundancy and ensure data integrity.
- **Justify Assumptions**: Provide detailed assumptions, justifications, and limitations for the database design.

## Project Files
- **ERD File (MySQL Workbench)**: 
  - `WongsanguanKantapong-A1.mwb` - The main MySQL Workbench file containing the database design for ActiveKids.
  - **Backup Files**: 
    - `WongsanguanKantapong-A1 HQ.mwb.bak` 
    - `WongsanguanKantapong-A1 no HQ.mwb.bak`
- **Documentation**:
  - **Assignment Document**: [WongsanguanKantapong-A1.docx](WongsanguanKantapong-A1.docx) - Contains the justifications, assumptions, and limitations of the database design.
  - **Assignment Brief**: [SP51-2023-CP2404-Assignment1 - DB Modelling.pdf](SP51-2023-CP2404-Assignment1 - DB Modelling(2).pdf) - Provides the scenario details and requirements for the project.

!(A1)[<>]

## Key Project Steps

### 1. **Entity-Relationship Diagram (ERD)**
- **Goal**: Design a fully-labeled ERD using Crow’s Foot Notation to represent the relationships between entities in the database.
- **Details**:
  - Includes entities for **Branches**, **Staff**, **Customers**, **Children**, **Training Sessions**, and **Equipment**.
  - Models relationships between these entities and accounts for cardinalities, optionalities, and constraints.
  - Tracks which staff work at which branch, the training sessions for children, and the equipment assigned to staff members.
  
### 2. **Normalization**
- **Goal**: Apply normalization rules to ensure data consistency and avoid redundancy.
- **Techniques**:
  - Ensured that all tables are in **3rd Normal Form (3NF)**.
  - Avoided data duplication, especially for **Training Sessions**, **Staff Access Cards**, and **iPads** issued to staff.

### 3. **Assumptions, Justifications, and Limitations**
- **Assumptions**: 
  - Each staff member works at only one branch.
  - Training sessions are limited to one sport per session.
  - Each child’s records are managed independently of their parent or guardian’s details.
- **Justifications**: 
  - A separate table for **Staff Access Cards** and **iPads** helps manage equipment assignment and track issues or repairs.
  - A separate table for **Children** ensures proper tracking of child-specific details like training history and physical attributes.
- **Limitations**: 
  - The current design does not account for scheduling conflicts (e.g., if a staff member is assigned to multiple training sessions at the same time).
  - The database does not track equipment used during training sessions.
  
  For more details, refer to the [WongsanguanKantapong-A1.docx](WongsanguanKantapong-A1.docx) file.

## Example Reports
The database design supports the generation of the following reports:
1. **Session Attendance Report**: Lists children who attended sessions during a specific period, along with session fees.
2. **Employee Salary Report**: Shows the total salary paid to employees for each branch by year.
3. **Equipment Assignment Report**: Lists all iPads and the employees to whom they were assigned, including details of equipment repairs and replacements.
4. **Customer Invoice**: Generates an itemized invoice for customers, showing session details, purchased gear, discounts, and taxes.

## Tools & Technologies
- **MySQL Workbench**: Used to design the ERD and create the database model.
- **MySQL**: The relational database system for which the database is designed.
- **Microsoft Word**: For documenting justifications, assumptions, and limitations.

## How to Use
1. Download the **.mwb** file and open it in MySQL Workbench to view or modify the ERD.
2. Run the SQL scripts generated from the MySQL Workbench file to implement the database structure in a MySQL environment.
3. Use the ERD and provided documentation to understand the design and assumptions made during the project.

## Conclusion
This project demonstrates my ability to design a relational database system based on a real-world scenario. The conceptual model developed ensures efficient data management and reporting for a sports training school, supporting tasks like employee management, training session scheduling, and customer invoicing.

---