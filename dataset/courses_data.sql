create table courses (
	course_id varchar(500) primary key,
	course_name varchar(255) not null,
	course_short_name varchar(255),
	eligible_groups varchar(100),
	min_cutoff decimal(5,2),
	diploma_entry VARCHAR(200),
	duration VARCHAR(200),
	diplomaindustry_demand TEXT,
	top_job_roles TEXT, 
	degree_type VARCHAR(500)
);

copy courses
from 'D:\shyla\college-recommendation\dataset\Course_Table_TN.csv'
delimiter ','
csv header;

select * from courses;

DROP TABLE IF EXISTS courses;