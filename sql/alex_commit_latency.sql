SELECT interval_start
, min(duration_avg) AS min_dur
, max(duration_avg) AS max_dur
, avg(duration_avg) AS avg_dur
, median(duration_avg) AS median_dur
FROM exa_sql_hourly 
WHERE  INTERVAL_start > (current_date - 15)
     AND command_name='COMMIT' 
   GROUP BY INTERVAL_start
   ORDER BY INTERVAL_start;