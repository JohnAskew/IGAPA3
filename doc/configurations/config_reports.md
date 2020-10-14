# config_reports.ini

## Purpose

There are 5 System load (system health) sets of tables. Each set consists of an HOURLY table, a DAILY table, a LAST_DAY table and, a MONTHLY table. For example, EXA_DB_SIZE_HOURLY, EXA_DB_SIZE_DAILY, EXA_DB_SIZE_LAST_DAY, EXA_DB_SIZE_MONTHLY. config_reports.ini is the default System load reporting (system health) configuration file. Using 2 variables for each metric, an average and a max, each html page will chart a system statistics table. The average metrics serves as a baseline, where the max shows peak usage.

## Layout and Specs

[DB_SIZE]                                       Arbitray heading meaningful just to the user
CONFIG_HOURLY_TBL        = EXA_DB_SIZE_HOURLY
CONFIG_DAILY_TBL         = EXA_DB_SIZE_DAILY
CONFIG_ROW1_COL_X_AXIS   = INTERVAL_START
CONFIG_ROW1_COL_Y_AXIS_1 = RAW_OBJECT_SIZE_AVG
CONFIG_ROW1_COL_Y_AXIS_2 = RAW_OBJECT_SIZE_MAX
CONFIG_ROW2_COL_X_AXIS   = INTERVAL_START
CONFIG_ROW2_COL_Y_AXIS_1 = MEM_OBJECT_SIZE_AVG
CONFIG_ROW2_COL_Y_AXIS_2 = MEM_OBJECT_SIZE_MAX
CONFIG_ROW3_COL_X_AXIS   = INTERVAL_START
CONFIG_ROW3_COL_Y_AXIS_1 = RECOMMENDED_DB_RAM_SIZE_AVG
CONFIG_ROW3_COL_Y_AXIS_2 = RECOMMENDED_DB_RAM_SIZE_MAX
CONFIG_ROW4_COL_X_AXIS   = INTERVAL_START
CONFIG_ROW4_COL_Y_AXIS_1 = STORAGE_SIZE_AVG
CONFIG_ROW4_COL_Y_AXIS_2 = STORAGE_SIZE_MAX
