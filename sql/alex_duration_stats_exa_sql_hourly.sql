SELECT interval_start 
, trunc(avg(min_dur),2) AS avg_min
, trunc(avg(max_dur),2) AS avg_max
, trunc(avg(avg_dur),2) AS avg_dur
, trunc(avg(median_dur),2) AS avg_median 
FROM 
   ( 
      SELECT interval_start
      , min(duration_avg) AS min_dur
      , max(duration_avg) AS max_dur
      , avg(duration_avg) AS avg_dur
      , median(duration_avg) AS median_dur
    FROM exa_sql_hourly 
      WHERE command_name='SELECT' GROUP BY INTERVAL_start
     )
GROUP BY 1 
ORDER BY 1 desc;