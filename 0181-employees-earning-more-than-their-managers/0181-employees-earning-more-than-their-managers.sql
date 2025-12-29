# Write your MySQL query statement below
SELECT a.name as Employee
FROM Employee AS a, Employee As b
WHERE a.ManagerId=b.Id AND a.Salary > b.Salary