SELECT *
FROM colleges c
JOIN college_courses cc
ON c.college_id = cc.college_id
JOIN courses co
ON cc.course_id = co.course_id
WHERE lower(co.course_name) =
lower('B.E. in Computer Science and Engineering with Specialization in Blockchain Technology')
AND lower(cc.eligible_caste) =
lower('MBC')
AND 190 >= cc.min_cutoff;

SELECT column_name
FROM information_schema.columns
WHERE table_name = 'course_eligibility';

SELECT DISTINCT eligible_groups
FROM courses;