SELECT DATE_FORMAT(trans_date, '%Y-%m') as month, country, count(id) AS trans_count, count(case when state='approved' THEN 1 END) AS approved_count, sum(amount) as trans_total_amount, sum(case when state='approved' THEN amount ELSE 0 END) as approved_total_amount
FROM Transactions
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country