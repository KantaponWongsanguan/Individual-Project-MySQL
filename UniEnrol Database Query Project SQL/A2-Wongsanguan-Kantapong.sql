SET GLOBAL sql_mode=(SELECT CONCAT(@@sql_mode, ',ONLY_FULL_GROUP_BY'));

/* Q1 List the First name, Last name, city, current salary and decreased salary (decrease thesalary by 5 percent) of faculty hired before 1998*/
select FacFirstName as "FirstName", FacLastName as "LastName", FacCity as "City", FacSalary, replace(format((FacSalary * 0.95), 0), ',', '') As "DecreasedSalary", DATE_FORMAT(FacHireDate, '%c/%e/%Y') as "HireDate"
from faculty
where year(FacHireDate) < 1998;

/* Q2  display the SSN and names of faculty members, and the course number
and offering-year for which the faculty member teaches the same course number as his or
her supervisor in the same year. */
select o1.FacSSN as "facssn", concat(f1.FacFirstName, ' ',f1.FacLastName) as "Faculty Name", o1.OffYear as "Offyear", o1.CourseNo
from offering o1
join faculty f1 on o1.FacSSN = f1.FacSSN
join faculty f2 on f1.FacSupervisor = f2.FacSSN 
join offering o2 on f2.FacSSN = o2.FacSSN
where o1.OffYear = o2.OffYear and o1.CourseNo = o2.CourseNo;

/* Q3 List the offer number, course number, and full name of the instructor (faculty) of all
FINANCE courses (the course number’s prefix is ‘FIN’) offered in winter 2006 taught by
professor. Note: professor’s rank is “PROF” in the database. */
select o.OfferNo, o.CourseNo, concat(f.FacFirstName, ' ',f.FacLastName) as "Instructor Name"
from offering o
join faculty f on o.facssn = f.facssn
where o.courseno like "%FIN%" and o.offterm = "WINTER" and o.offyear = 2006 and f.facrank = "PROF";

/* Q4 Write a query to summarize the average GPA of upper-division (junior (JR) or senior (SR))
students by major. Only list the majors with average GPA greater than 2. */
select StdMajor, format(sum(StdGPA)/count(StdGPA), 1)  as "AvgGPA"
from student
group by StdMajor;

/* Q5 Summarize the number of offerings run in 2006 by offering location.*/
select OffLocation, count(*) as "2006OfferCount"
from offering
where offyear = "2006" 
group by offlocation;

/* Q6 List the offering number, course number, days, location, time, and instructor’s last name,
for student Tess Dodge’s course schedule in 2006.*/
select o.OfferNO, o.CourseNo, o.OffDays, o.OffLocation, o.OffTime, f.FacLastName
from offering o
join enrollment e on e.offerno = o.offerno
join registration r on r.RegNo = e.RegNo
join student s on s.stdssn = r.stdssn
join faculty f on o.facssn = f.facssn 
where o.offyear = "2006" and s.stdssn = "678901234" ;

/* Q7 List the course description, the course number, the number of offerings, and the average
enrollment across offerings.*/
select c.CrsDesc, o.CourseNo, count(o.courseno), format(sum(o.offnumenrolled)/count(o.courseno), 0) as "AvgEnroll"
from offering o
join course c on o.courseno = c.courseno
where o.offnumenrolled > 0
group by o.courseno
order by o.courseno;

/* Q8 For offerings beginning with IS in the associated course number, retrieve the offer number,
the course number, the faculty number, and the faculty name. Include an offering in the result
even if the faculty is not assigned. */
select o.OfferNo, o.CourseNo, LPAD(f.facssn, 9, 0) as "faculty.FacSSN", f.FacFirstName ,f.FacLastName
from offering o
left join faculty f on o.facssn = f.facssn
where o.courseno like "IS%"
order by f.facssn;

/* Q9 List the Social Security Number (SSN), name and city of faculty who teach in winter terms. */
select distinct o.FacSSN, concat(f.FacFirstName, ' ',f.FacLastName) as "Instructor Name", f.FacCity
from offering o
join faculty f on o.facssn = f.facssn
where o.offterm = "WINTER";


/* Q10 List the name and rank of faculty who teach at least one offering of all of the 2006
information systems (IS) courses and his/her supervisor’s name.*/
select distinct f.FacFirstName, f.FacLastName, f.FacRank, concat(f2.facfirstname, ' ', f2.faclastname) as Supervisor
from faculty f
join offering o on f.facssn = o.facssn
join faculty f2 on f.FacSupervisor = f2.facssn
where o.CourseNo like "%IS%" and o.OffYear = "2006";


