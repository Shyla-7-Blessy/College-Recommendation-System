CREATE TABLE colleges (
    college_id VARCHAR(20) PRIMARY KEY,
    college_name VARCHAR(255) NOT NULL,
    city VARCHAR(100),
    state VARCHAR(100),
    course VARCHAR(255),
    college_category VARCHAR(50),
    ownership VARCHAR(20),
    caste VARCHAR(20),
    cut_off DECIMAL(10,2),
    fees INTEGER,
    nirf_rank INTEGER
);

ALTER TABLE colleges DROP COLUMN ownership;


SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'colleges';

COPY colleges
FROM 'D:\shyla\college-recommendation\dataset\college_data.csv'
DELIMITER ','
CSV HEADER;

SELECT table_name
FROM information_schema.tables
WHERE table_name = 'colleges';

CREATE TABLE IF NOT EXISTS colleges (
    college_id VARCHAR(20),
    college_name VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    course VARCHAR(255),
    college_category VARCHAR(50),
    ownership VARCHAR(20),
    caste VARCHAR(20),
    cut_off DECIMAL(10,2),
    fees INTEGER,
    nirf_rank INTEGER
);

SELECT current_database();

SELECT schemaname, tablename
FROM pg_tables
WHERE tablename = 'colleges';

SELECT * from colleges;

DROP TABLE IF EXISTS colleges;

#Creating the colleges table

CREATE TABLE colleges (
    college_id VARCHAR(50) PRIMARY KEY,
    college_name VARCHAR(255) NOT NULL,
    city VARCHAR(100),
    state VARCHAR(100),
    college_tier VARCHAR(50),
    nirf_rank INTEGER,
    accreditation VARCHAR(100),
    total_seats INTEGER
);

COPY colleges
FROM 'D:/shyla/college-recommendation/dataset/College_Table.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM colleges;

