# Write your MySQL query statement below
SELECT max(total)-min(total) as difference_in_score
FROM Scores
JOIN (
    SELECT student_id, assignment1+assignment2+assignment3 as total
    FROM Scores
    GROUP BY student_id
) AS Sub on Scores.student_id = Sub.student_id