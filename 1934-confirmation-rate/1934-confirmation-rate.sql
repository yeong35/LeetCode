# Write your MySQL query statement below
SELECT S.user_id, ROUND(COUNT(CASE WHEN action="confirmed" THEN 1 END)/COUNT(*), 2) as confirmation_rate
FROM Signups as S LEFT JOIN Confirmations AS C ON S.user_id = C.user_id
GROUP BY user_id
ORDER BY user_id