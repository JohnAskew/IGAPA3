# igapa3
Igapa with multi-flexibility 1. Pull from Jira or from DB.2. Run from config file or commandline. 3. Add your own SQL to visualize.

# Usage
## Help
-c: Config_file override. You must specify which config to use for reporting.
      --> The default config included is config_reports.ini.
      
-j:   Jira Source. The JIRA ticket number which has the CSV attachments

-k:   Jira user. Logon credential for JIRA. Overrides config_admin.ini

-l:   Jira password. Logon credential for JIRA. Overrides config_admin.ini

-m:   Database host name or I.P. address. Overrides _config.py

-n:   Database host port. Overrides _config.py

-u:   Database user logon credential. Overrides _config.py

-p:   Database user password credential. Overrides _config.py

-s:   Database schema. Overrides _config.py

-h:   Usage help

# Quick setup of 2 configuration files.

Update these appropriately for automation defaults.

1. _config.py - holds the default database connection credentials. 

2. config_admin.ini - First paragraph holds credentials to access our JIRA system.

# Automation - using the config files to drive connectivity.

**_config.py** - holds the DB connection string parameters (db, port, user, pw, schema).

**config_admin.ini** - Among other things, holds the JIRA credentials if you are extracting CSV from JIRA ticket.

### Execution example:
Process and visualize the database defined in **_config.py*        >>> **python igapa3.py -c** _config_reports.ini_

Process and visualize CSV files attached to JIRA ticket EXA-28727  >>> **python igapa3.py  -c** _config_reports2.ini_   **-j** _28727_

# Command line overrides

Show parameters for igapa3.py >>> **python igapa3.py**

Pull database data using overrides >>> **python igapa3.py -c config_report2.ini -m 192.168.1.158 -n 8563 -u sys -p secret**

Pull JIRA files attached to ticket EXA-28615 using overrides >>> **python igapa3.py -c config_report2.ini - j 28615 -k exasol_user -l exasol_password**

# Subroutines and Tools
**_config.py** - Database connectivity parameters such as credentials (Defaults for automation).

**config_admin.ini** - JIRA credentials, logging level and visualization properties.

**config_reports.ini** - Visualization properties, which tables and columns to visualize.

**config_report2.ini** - Alternative visualization properties, which tables and columns to visualize.

**config_report3.ini** - Special System table alternative visualization properties, which tables and columns to visualize.

**export_cloud_to_csv.py** - Creates directory of server_name (from *_config.py*) and extracts a single database table to local csv using same name.

**export_sql_to_csv.py** - Reads user sql and extracts CSV.

**export_JIRA_to-csv.py** - Passed EXA- ticket and calls *subr_jira_download.py*.

**igapa2_linkage** - Utility to pass parameters. Included in most of the programs.

**igapa_master** - Decides to call processes to Oownload JIRA files or download files from the database.

**igapa2.py** _Handles program(s) linkage and runs igapa2_validate_config_{jira / db}.py_

**igapa2_main.py** _Validates linkage parameters and calls igpapa_master.py_

**igapa2_main** - Reads igapa2_linkage and calls igapa_master.py using parameters/arguments.

**igapa2_validate_config_db.py** - Reads igapa2_linkage and calls igapa2_main.py using linkage parameters.

**igapa2_validate_config_jira.py** - Validates the JIRA parameters and calls igapa2_main.py using linkage parameters.

**igapa3.py** _MAIN PROGRAM to execute_

**subr_jira_download.py** - Passed EXA- ticket and downloads EXA- ticket attached files.

**subr_char_4_rows.py** - Reads config file and builds charts.

**subr_validate_ticket.py** - Validate JIRA ticket exists on system.

**test_get_config_tbls.py** - Reads config file, extracts Tables and calls *export_cloud_to_csv.py*.

**tools_create_config.py** - Creates the config_report(x).ini for each sql in the ./sql folder

**tools_get_table_cols.py** - Pass in table, get back table columns

**tools_logger.py** - Set up logging. Imported by programs using logging.

**tools_parse_config.py** - Utility to validate the configuration files used. (such as config_admin.ini, config_reports.ini, etc.)
