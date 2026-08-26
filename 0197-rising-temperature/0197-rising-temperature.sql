# Write your MySQL query statement below
select Today.id
from Weather AS Today JOIN Weather AS Yesterday ON DATEDIFF(Today.recordDate, Yesterday.recordDate)=1
where Today.temperature > Yesterday.temperature