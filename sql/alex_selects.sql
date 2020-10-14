SELECT interval_start
, sum(count) FROM exa_sql_hourly 
WHERE INTERVAL_start > (current_date -15) 
  AND command_name='SELECT'
GROUP BY INTERVAL_start
ORDER BY INTERVAL_start 
;
