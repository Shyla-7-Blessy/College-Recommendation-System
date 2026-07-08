CREATE TABLE student_profiles (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100),
    percentage NUMERIC(5,2),
    cutoff NUMERIC(5,2),
    caste VARCHAR(50),
    eligible_group VARCHAR(50),
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from student_profiles;
