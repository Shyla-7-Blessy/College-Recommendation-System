create table course_eligibility(
	eligibility_id integer primary key,
	course_id varchar(200),
	eligible_group varchar(200), 
	caste varchar(50),
	min_cutoff_mark decimal(5,2),
	entry_type varchar(200)
);

copy course_eligibility
from 'D:\shyla\college-recommendation\dataset\Course_Eligibility.csv'
delimiter ','
csv header;

select * from course_eligibility;

SELECT *
FROM course_eligibility
WHERE course_id = 'CRS_2199';

SELECT
    course_id,
    caste,
    COUNT(*)
FROM course_eligibility
GROUP BY course_id, caste
HAVING COUNT(*) > 1;

select * from course_eligibility ce
join courses c
on c.course_id = ce.cour