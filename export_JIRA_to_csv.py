#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

try:

    import subprocess

except:

    os.system("pip install subprocess")

    import subprocess

try:

    import logging

except:

    os.system('pip install logging')

    import logging

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt

try:

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    logger.error("#######################################")

    logger.error("# ERROR in " +  os.path.basename(__file__))
    
    logger.error("# " + msg)

    logger.error("# " +  os.path.basename(__file__) + " aborting with no action taken.")

    logger.error("#######################################")

    log_and_print("#######################################")

    log_and_print("# ERROR in", os.path.basename(__file__))
    
    log_and_print(msg)

    log_and_print("#", os.path.basename(__file__), "aborting with no action taken.")

    log_and_print("#######################################")

    sys.exit(13)

try:
    import ntpath

except:

    os.system('pip install ntpath')

    import ntpath

#######################################
# FUNCTIONS
#######################################
#--------------------------------------
def log_and_print(msg = ""):

    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)


#######################################
# VARIABLES
#######################################

# now = dt.today().strftime('%Y%m%d_%H%M%S')

dir_path = os.path.dirname(os.path.realpath(__file__))

new_dir =""

global in_ticket

in_ticket = ""

class_chart = 'DB_SIZE'

now = dt.today().strftime('%Y%m%d_%H%M%S')

my_pgm = ntpath.basename(os.path.basename(__file__))

logging_filename = ("./logs/" + my_pgm[0:(my_pgm.index('.py'))] + '.log')

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

log_and_print("#--------------------------------------#")

log_and_print("# Entering " + os.path.basename(__file__))

log_and_print("#--------------------------------------#")

#######################################
# Save off the old report - do not overlay
#######################################
#-------------------------------------#
# Extract log_level for reporting details
# ------------------------------------#
try:

    b = ParseConfig(class_chart, 'config_admin.ini')

except Exception as e:

    log_and_print("#######################################")

    log_and_print("# WARNING")

    log_and_print("#-------------------------------------#")

    log_and_print("# Unable to read config_admin.ini section REPORTING to get log_level")

    log_and_print("# Using defaults:")

    log_and_print(" using log_level of WARNING")

    log_and_print(e)

try:

    log_level, outlier_threshold, reports_hourly, reports_daily = b.read_config_admin_reporting('.', 'config_admin.ini')

    log_and_print("# REPORTING variables log_level " + log_level )


except Exception as e:

    log_and_print("#------------------------------------#")

    log_and_print("WARNING")

    log_and_print("#------------------------------------#")

    log_and_print("unable to reference REPORTING section of config_admin.ini")

    log_and_print("Using defaults:")

    log_and_print("==> log_level " + log_level)

    log_and_print(e)


#######################################
# Start by extracting the LOGGING 
#    reporting level for output 
#    granularity (how much detail).
#######################################




#######################################
# Log the beginning of processsing
#######################################



logger = logging.getLogger()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

fh = logging.FileHandler(logging_filename, mode = 'a')

fh.setLevel(logging.INFO)

fh.setFormatter(formatter)

logger.addHandler(fh)

ch = logging.StreamHandler()

ch.setLevel(logging.INFO)

ch.setFormatter(formatter)

logger.addHandler(ch)

try:

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    log_and_print("#######################################")

    log_and_print("ERROR")
    
    log_and_print(msg)

    log_and_print("aborting with no action taken.")

    log_and_print("#######################################")

   
    sys.exit(13)




# log_level = "WARNING"

######################################
# START LOGIC for MAIN
######################################
if __name__ == "__main__":

    if len(sys.argv) > 1:

        in_ticket = sys.argv[1]

        new_dir = str("EXA-" + str(in_ticket))

    else:

        in_ticket = 28615

        new_dir = str("EXA-" + str(in_ticket))

    if len(sys.argv) > 2:

        config_in = sys.argv[2]

    else:

        config_in = 'config_reports.ini'

else:

    in_ticket - 28615

    new_dir = str("EXA-" + str(in_ticket))

    config_in = 'config_reports.ini'

#######################################
#######################################
# BEGIN MAIN LOGIC
#######################################
#######################################


log_and_print("#####################################")

msg_info = "# Starting " + os.path.basename(__file__)

log_and_print(msg_info)

filename = str(os.getcwd() + '\\' + config_in)

if os.path.exists(filename):

    log_and_print("was given config file " + config_in)

else:

    log_and_print("#####################################")

    log_and_print("Could not find config file: " + config_in)

    log_and_print("Ensure " + config_in + " exists in this directory: " + os.getcwd())

    log_and_print("# ---> Does " + config_in + " exist?")

    log_and_print("# ---> Is "  + config_in + " a readable file?")

    log_and_print("Aborting with no action taken")

    log_and_print("#####################################")

    
    sys.exit(0)


msg_info = "Calling jira_download.py with " + str(in_ticket)

log_and_print(msg_info)

log_and_print("INFO:")

log_and_print("is calling jira_download.py with " + str(in_ticket))

log_and_print("#####################################")

log_and_print()

msg_info = "Executing call " + dir_path + '\\' + "subr_jira_download.py " + str(in_ticket)

log_and_print(msg_info)


subr_rc = subprocess.call(["python", dir_path + "/" + "subr_jira_download.py", str(in_ticket)])

if subr_rc != 0:

    log_and_print(" received return code " + str(subr_rc) + " from subr_jira_download.py")

    log_and_print("Aborting with no action taken.")

    log_and_print("Aborting after receiving subr_rc:" + str(subr_rc) + " from subr_jira_download.py")

    log_and_print("#####################################")

    sys.exit(-1)

#######################################
# Return to processing the attachments
#######################################

work_dir = os.path.join(dir_path, new_dir)

msg_info = "received ticket: " + str(in_ticket) + " creating new_dir " + new_dir

log_and_print(msg_info)

msg_info = "Current directory is " + os.getcwd() + " | Working directory is " + new_dir + " |  Output_dir: " + work_dir

log_and_print(msg_info)

log_and_print("#####################################")

log_and_print("#INFO:")

log_and_print("# received ticket: " + str(in_ticket ) + " creating new_dir " + new_dir)

log_and_print("# Current directory is " + os.getcwd())

log_and_print("# Working directory is " + new_dir)

log_and_print("# Output_dir: " + work_dir)

log_and_print("#####################################")

log_and_print()

DAILY_TBLZ   = ['EXA_DB_SIZE_DAILY', 'EXA_SQL_DAILY', 'EXA_MONITOR_DAILY', 'EXA_USAGE_DAILY']

HOURLY_TBLZ  = ['EXA_DB_SIZE_HOURLY','EXA_SQL_HOURLY','EXA_MONITOR_HOURLY','EXA_USAGE_HOURLY']

for table in range(len(DAILY_TBLZ)):

    DAILY_TBLZ[table] = str(DAILY_TBLZ[table] + '.csv')

    HOURLY_TBLZ[table] = str(HOURLY_TBLZ[table] + '.csv')

os.chdir(dir_path)

msg_info = "processing igapa pgms in directory " + os.getcwd()

log_and_print(msg_info)

log_and_print("#####################################")

log_and_print("#INFO:")

log_and_print(("# processing igapa pgms in directory "  + os.getcwd()))

log_and_print("#####################################")

log_and_print()

if (
     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[0])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[0]))) or

     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[1])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[1]))) or 

     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[2])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[2]))) or 

     (os.path.exists(work_dir + '\\' + DAILY_TBLZ[3])  and (os.path.exists(work_dir + '\\' + HOURLY_TBLZ[3]))) 
    ):
    pass

else:

    log_and_print("#####################################")

    log_and_print("# ===> Check other logs for ERRORS! <=== ")

    log_and_print("# ===> Check other logs for ERRORS! <=== ")

    log_and_print("# ===> Check other logs for ERRORS! <=== ")
 
    msg_info = "# WARNING: "

    log_and_print(msg_info)

    log_and_print("# processed ticket:\t " +  new_dir)

    log_and_print("# BUT did not find any usable CSV files for")

    log_and_print("# generating charts. Ending processing without any charts.")

    log_and_print("#")

    log_and_print("# This solution is looking for either: ")

    log_and_print("# " +  str(new_dir + '\\' + DAILY_TBLZ[0]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[0]) )

    log_and_print("# OR")

    log_and_print("# " +  str(new_dir + '\\' + DAILY_TBLZ[1]) +" and " +  str(new_dir + '\\' + HOURLY_TBLZ[1]) )

    log_and_print("# OR")

    log_and_print("# " +  str(new_dir + '\\' + DAILY_TBLZ[2]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[2]) )

    log_and_print("# OR")

    log_and_print("# " +  str(new_dir + '\\' + DAILY_TBLZ[3]) + " and " +  str(new_dir + '\\' + HOURLY_TBLZ[3]) )

   

log_and_print("Removing CSV files downloaded.")

log_and_print("succeessful exit.")

log_and_print("#####################################")
