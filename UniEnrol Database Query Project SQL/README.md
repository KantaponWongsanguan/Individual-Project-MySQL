# UniEnrol Database Query Project

## Project Overview
This project was completed as part of the **CP2404 Database Modelling** course at James Cook University. The objective of this assignment was to formulate and execute SQL queries using the **UniEnrol Database**, which tracks student enrollments, faculty members, courses, and course offerings at a university. The project demonstrates the ability to extract meaningful data from the database through various SQL queries using **MySQL Workbench**.

### Scenario Overview
The UniEnrol Database is a university enrollment system that manages data on students, instructors, courses, course offerings, registrations, and enrollments. The database schema includes tables for:
- **Faculty**: Contains details of instructors (e.g., SSN, name, salary, city).
- **Courses**: Contains information on the subjects taught at the university.
- **Offerings**: Tracks which courses are taught by which instructors and when.
- **Students**: Tracks student details and registration for courses.
- **Enrollments**: Manages student course enrollments.

### Assignment Specifications
- **Task**: Write 10 SQL queries to extract specific information from the **UniEnrol Database**.
- **Platform**: The SQL queries were written and executed in **MySQL Workbench**.
- **Database File**: The project uses a provided database dump file (`uniEnrolDB.sql`), which is imported into MySQL Workbench for testing the queries.

## Goals
The primary objectives of this project are to:
- **Query the Database**: Write SQL queries to retrieve specific information, including faculty details, course offerings, enrollment statistics, and student schedules.
- **Test Queries**: Ensure that each SQL query produces the expected result based on the provided dataset.
- **Apply SQL Functions**: Use SQL functions like `JOIN`, `GROUP BY`, `SUM`, `AVG`, and `FORMAT` to extract and format the required information.

## Project Files
- **SQL Query File**: 
  - `A2-Wongsanguan-Kantapong.sql` - Contains all the SQL queries formulated for the assignment.
- **Database Dump File**: 
  - `uniEnrolDB.sql` - The MySQL dump file for the **UniEnrol Database**, which is imported into MySQL Workbench for testing the queries.
- **Documentation**:
  - **Assignment Report**: [A2-Wongsanguan-Kantapong.docx](A2-Wongsanguan-Kantapong.docx) - Contains the SQL queries along with screenshots of the query results as executed in MySQL Workbench.
  - **Assignment Specifications**: [2023-SP51-CP2404-A2-Specifications.pdf](2023-SP51-CP2404-A2-Specifications.pdf) - Provides the assignment details and SQL query requirements.

## Key SQL Queries
### 1. **Faculty Salary Query**
- **Goal**: List the first name, last name, city, current salary, and decreased salary (by 5%) of faculty members hired before 1998.
- **Key SQL Functions**: `SELECT`, `FORMAT`, `WHERE`, `DATE_FORMAT`.

### 2. **Faculty Course Query**
- **Goal**: Display the SSN and names of faculty members, along with the course number and offering year for which they teach the same course as their supervisor in the same year.
- **Key SQL Functions**: `JOIN`, `CONCAT`.

### 3. **Winter Finance Courses Query**
- **Goal**: List the course number, offer number, and instructor name for all finance courses (prefix 'FIN') offered in Winter 2006 by professors.
- **Key SQL Functions**: `WHERE`, `LIKE`, `JOIN`.

### 4. **Average GPA by Major Query**
- **Goal**: Summarize the average GPA of upper-division (Junior or Senior) students by major.
- **Key SQL Functions**: `GROUP BY`, `AVG`, `WHERE`.

### 5. **Offerings Count by Location Query**
- **Goal**: Summarize the number of course offerings in 2006 by location.
- **Key SQL Functions**: `GROUP BY`, `COUNT`.

### 6. **Student Schedule Query**
- **Goal**: Retrieve Tess Dodge’s 2006 course schedule, including offer number, course number, days, location, time, and instructor's last name.
- **Key SQL Functions**: `JOIN`, `WHERE`.

### 7. **Average Enrollment by Course Query**
- **Goal**: List the course description, course number, number of offerings, and the average enrollment across offerings.
- **Key SQL Functions**: `GROUP BY`, `SUM`, `AVG`.

### 8. **Offerings with Faculty Information Query**
- **Goal**: Retrieve the offer number, course number, and faculty information for all offerings with course numbers starting with 'IS'. Include offerings even if no faculty is assigned.
- **Key SQL Functions**: `LEFT JOIN`, `LPAD`.

### 9. **Winter Term Faculty Query**
- **Goal**: List the SSN, name, and city of faculty members who teach in winter terms.
- **Key SQL Functions**: `DISTINCT`, `JOIN`.

### 10. **Faculty and Supervisor Information Query**
- **Goal**: List the name and rank of faculty who teach all 2006 IS courses, along with their supervisor's name.
- **Key SQL Functions**: `JOIN`, `CONCAT`.

For detailed SQL code and screenshots of the query results, refer to the [A2-Wongsanguan-Kantapong.docx](A2-Wongsanguan-Kantapong.docx) file.

## Tools & Technologies
- **MySQL Workbench**: Used to write and execute SQL queries.
- **MySQL**: The relational database management system (RDBMS) used to manage the UniEnrol database.
- **SQL**: Structured Query Language, used to query and manipulate the data in the UniEnrol database.

## How to Use
1. Download the SQL files and import the **uniEnrolDB.sql** dump file into MySQL Workbench.
2. Open the **A2-Wongsanguan-Kantapong.sql** file in MySQL Workbench to view and execute the SQL queries.
3. Test the queries to retrieve the expected results from the database.

## Conclusion
This project demonstrates the ability to write complex SQL queries to extract specific information from a relational database. Through this assignment, I gained experience in using various SQL operations, including `JOIN`, `GROUP BY`, and `FORMAT`, to solve real-world data extraction problems.

---