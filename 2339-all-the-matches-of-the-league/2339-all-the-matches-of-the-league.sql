# Write your MySQL query statement below
SELECT a.team_name AS home_team, b.team_name as away_team
FROM Teams as a, Teams as b
WHERE a.team_name != B.team_name
GROUP BY a.team_name, b.team_name