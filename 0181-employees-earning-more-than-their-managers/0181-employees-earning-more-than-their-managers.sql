# Write your MySQL query statement below

Select e.name as employee
From employee as e
inner join employee as m
on e.managerId = m.id
where e.salary>m.salary
