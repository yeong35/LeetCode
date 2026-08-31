# Write your MySQL query statement below
SELECT M.name
FROM Employee AS E JOIN Employee AS M ON E.managerId = M.id
GROUP BY E.managerId
HAVING count(E.managerId) >= 5
