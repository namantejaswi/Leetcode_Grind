# Write your MySQL query statement below

Select email 
From Person
Group by email
Having (Count(email)>1)