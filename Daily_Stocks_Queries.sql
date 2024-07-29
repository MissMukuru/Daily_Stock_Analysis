SELECT * FROM Daily_Data_rev
WHERE Moving_Average_30 IS NULL

SELECT DATE, VOLUME
FROM Daily_data_rev
WHERE CAST("Close" AS DECIMAL(10, 2)) > 195;

SELECT MAX(Moving_Average_30) 
FROM Daily_data_rev

SELECT MIN(Moving_Average_30) 
FROM Daily_data_rev

SELECT MAX(Volatility) 
FROM Daily_data_rev

SELECT MIN(Volatility) 
FROM Daily_data_rev

SELECT Date,High, Low, GREATEST(High,Low) as [Max_High_low]
FROM Daily_data_rev