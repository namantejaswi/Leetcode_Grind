# Write your MySQL query statement below

Select E.name, B.bonus From
Employee E
Left Join Bonus B on E.empID = B.empID
where B.Bonus<1000 or B.Bonus is null