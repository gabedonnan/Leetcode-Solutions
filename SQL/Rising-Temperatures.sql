# Write your MySQL query statement below
SELECT t2.id
FROM Weather t1, Weather t2
WHERE DATE_ADD(t1.recordDate, INTERVAL 1 DAY) = t2.recordDate AND t1.temperature < t2.temperature
