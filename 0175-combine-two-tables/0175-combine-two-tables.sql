# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person left outer join Address on Person.personID = Address.personID