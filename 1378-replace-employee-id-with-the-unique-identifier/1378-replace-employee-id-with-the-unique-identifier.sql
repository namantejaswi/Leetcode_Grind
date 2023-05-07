# Write your MySQL query statement below

Select unique_id, name
From Employees
left Join  EmployeeUNI
using(id)