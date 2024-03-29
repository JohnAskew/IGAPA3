# config_reports.ini

## Purpose

There are 5 System load (system health) sets of tables. Each set consists of an HOURLY table, a DAILY table, a LAST_DAY table and, a MONTHLY table. For example, EXA_DB_SIZE_HOURLY, EXA_DB_SIZE_DAILY, EXA_DB_SIZE_LAST_DAY, EXA_DB_SIZE_MONTHLY. config_reports.ini is the default System load reporting (system health) configuration file. Using 2 variables for each metric, an average and a max, each html page will chart a system statistics table. The average metrics serves as a baseline, where the max shows peak usage.

## Layout and Specs

[DB_SIZE]  >> Arbitray heading meaningful just to the user

CONFIG_HOURLY_TBL        = EXA_DB_SIZE_HOURLY >> (Mandatory) The system statistic table we wish to visualize. MUST be an EXA-xxx-HOURLY table.

CONFIG_DAILY_TBL         = EXA_DB_SIZE_DAILY  >> Deprecated

CONFIG_ROW1_COL_X_AXIS   = INTERVAL_START     >> (Mandatory) Must be a date field to plot the x-axis dateline

CONFIG_ROW1_COL_Y_AXIS_1 = RAW_OBJECT_SIZE_AVG >> (Mandatory) Y-Axis variable. In this case it's an "avg" metric.

CONFIG_ROW1_COL_Y_AXIS_2 = RAW_OBJECT_SIZE_MAX >> Second Y-Axis variable. Ih this case, it's a "max" metric. 

CONFIG_ROW2_COL_X_AXIS   = INTERVAL_START      >> Row 2 charts - the date column. Generally the same as CONFIG_ROW1_COL_X_AXIS.

CONFIG_ROW2_COL_Y_AXIS_1 = MEM_OBJECT_SIZE_AVG >> Row 2 charts - first Y-Axis-variable (see above)

CONFIG_ROW2_COL_Y_AXIS_2 = MEM_OBJECT_SIZE_MAX >> Row 2 chars  - second Y-Axis variable.

CONFIG_ROW3_COL_X_AXIS   = INTERVAL_START      >> Row 3 charts - the date column.

CONFIG_ROW3_COL_Y_AXIS_1 = RECOMMENDED_DB_RAM_SIZE_AVG >> Row 3 chars - first Y-Axis variable

CONFIG_ROW3_COL_Y_AXIS_2 = RECOMMENDED_DB_RAM_SIZE_MAX >> Row 3 charts - second Y-Axis variable

CONFIG_ROW4_COL_X_AXIS   = INTERVAL_START      >> Row 4 charts - the date column.

CONFIG_ROW4_COL_Y_AXIS_1 = STORAGE_SIZE_AVG    >> Row 4 charts - the first Y-Axis column

CONFIG_ROW4_COL_Y_AXIS_2 = STORAGE_SIZE_MAX    >> Row 4 chars  - the second Y-Axis column.

<img src="image-DB_SIZE1.png" img width=800/>
<img src="image-DB_SIZE2.png" img width=800/>
<img src="image-DB_SIZE3.png" img width=800/>
<img src="image-DB_SIZE4.png" img width=800/>
