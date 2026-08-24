# Write your MySQL query statement below
select p.product_id, IFNULL(ROUND(SUM(p.price*u.units)/SUM(units), 2), 0) AS average_price
from Prices AS P LEFT JOIN UnitsSold AS U ON P.product_id = U.product_id AND U.purchase_date BETWEEN p.start_date AND p.end_date
group by product_id