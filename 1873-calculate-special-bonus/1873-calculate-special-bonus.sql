select employee_id, IF(employee_id % 2 = 1 AND name not like 'm%', salary, 0) as bonus
from Employees
order by employee_id