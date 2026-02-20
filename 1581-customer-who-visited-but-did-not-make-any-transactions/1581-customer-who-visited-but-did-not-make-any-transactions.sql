SELECT customer_id, count(*) as count_no_trans
FROM Visits
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE transaction_id  is null
GROUP BY customer_id
ORDER BY customer_id