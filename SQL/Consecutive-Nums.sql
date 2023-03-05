# Write your MySQL query statement below
SELECT DISTINCT t1.num AS ConsecutiveNums
FROM Logs t1, Logs t2, Logs t3
WHERE t2.id = t1.id + 1 AND t3.id = t2.id + 1 AND t1.num = t2.num  AND t2.num = t3.num
