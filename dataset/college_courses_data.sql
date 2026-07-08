create table college_courses(
	college_course_id NUMERIC PRIMARY KEY,
	college_id varchar(200),
	course_id varchar(200),
	eligible_caste varchar(200),
	min_cutoff decimal(5,2),
	annual_fees NUMERIC,
	total_seats NUMERIC
);


copy college_courses
from 'D:\shyla\college-recommendation\dataset\College_Courses_Junction.csv'
delimiter ','
csv header;

select * from college_courses;

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;

SELECT * FROM college_courses LIMIT 1;