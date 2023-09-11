# Write your MySQL query statement below
Select  e.name, eu.unique_id
From Employees e 
Left Join EmployeeUNI eu on e.id=eu.id;
