CREATE TABLE students (
	student_id VARCHAR(200) PRIMARY KEY,
	student_name VARCHAR(200) NOT NULL,
	dob DATE,
	email_id VARCHAR(200) UNIQUE,
	phone VARCHAR(15),
	twelveth_Diploma_group VARCHAR(500),
	mark_percentage DECIMAL(5,2),
	board VARCHAR(100),
	school_name VARCHAR(200),
	caste VARCHAR(50),
	religion VARCHAR(50),
	nationality VARCHAR(50),
	address TEXT,
	city VARCHAR(100), 
	father_name VARCHAR(100)
);

COPY students
FROM 'D:\shyla\college-recommendation\dataset\student_table.csv'
DELIMITER ','
CSV HEADER;

select * from students;

SELECT current_database();

SELECT COUNT(*)
FROM information_schema.tables
WHERE table_schema = 'public';