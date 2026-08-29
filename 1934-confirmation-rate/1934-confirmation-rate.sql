# Write your MySQL query statement below
select S.user_id, ROUND(COUNT(CASE WHEN action="confirmed" THEN 1 END)/COUNT(*), 2) AS confirmation_rate
from Signups AS S LEFT JOIN Confirmations AS C ON S.user_id = C.user_id
GROUP BY S.user_id