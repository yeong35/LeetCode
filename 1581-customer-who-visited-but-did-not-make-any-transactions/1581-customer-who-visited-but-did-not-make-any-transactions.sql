-- SELECT customer_id, COUNT(amount) AS count_no_trans
SELECT customer_id, count(*) AS count_no_trans
FROM Visits 
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE transaction_id is null
GROUP BY customer_id