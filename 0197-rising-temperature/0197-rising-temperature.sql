# Write your MySQL query statement below
SELECT today.id as Id
FROM Weather AS yesterday CROSS JOIN Weather AS today
WHERE DATEDIFF(today.recordDate, yesterday.recordDate) = 1 and today.temperature > yesterday.temperature