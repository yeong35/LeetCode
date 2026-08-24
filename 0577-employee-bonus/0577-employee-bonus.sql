# Write your MySQL query statement below
select name, bonus
from Employee as E LEFT JOIN Bonus AS B ON E.empId = B.empId
where B.bonus IS NULL OR B.bonus < 1000;