SELECT name AS customers
FROM Customers
WHERE id NOT IN (
    SELECT customerID
    FROM Orders
)