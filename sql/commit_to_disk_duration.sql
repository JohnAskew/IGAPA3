select M.INTERVAL_START
, M.NET_AVG
, M.hdd_read_avg
, M.hdd_write_avg
, S.Duration_avg
from exa_MONITOR_hourly M 
join exa_sql_hourly S on M.INTERVAL_START = S.INTERVAL_START 
  where S.Command_name = 'COMMIT' 
    and S.Success;