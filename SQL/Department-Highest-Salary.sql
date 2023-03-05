# Write your MySQL query statement below
SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee, Department
WHERE Employee.departmentId = Department.id AND (departmentId, salary) IN
(select departmentId, MAX(Salary) AS max FROM Employee GROUP BY departmentId)
