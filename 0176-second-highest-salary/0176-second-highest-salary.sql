# Write your MySQL query statement below


Select max(salary) as SecondHighestSalary 
From Employee
Where salary < (select max(salary) From Employee)