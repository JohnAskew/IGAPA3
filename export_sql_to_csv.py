#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

import _config as config

# if os.path.exists(logging_filename):

#     os.remove(logging_filename)

from tools_logger import *

try:

    from datetime import datetime as dt

except:

    os.system('pip install datetime')

    from datetime import datetime as dt

try:

    import pyexasol

except:

    os.system('pip install pyexasol')

    import pyexasol

try:

    import csv

except:

    os.system("pip install csv")

    import csv

try:

    import pandas as pd

except:

    os.system('pip install pandas')

    import pandas as pd

try:

    import subprocess

except:

    os.system('pip install subprocess')

    import subprocess


#######################################
# FUNCTIONS
#######################################

#--------------------------------------
def log_and_print(msg=''):
#--------------------------------------

    print("# " + os.path.basename(__file__) + ": " + str(msg))

    logging.info("# " + os.path.basename(__file__) + ": " + str(msg))

#--------------------------------------
def export_table(sql_name, mysql):
#--------------------------------------
    
    try:
        
        pd = C.export_to_pandas(mysql)
       
        pd.to_csv((sql_name + '.csv') , na_rep = 0)

        pd_rows, pd_cols = pd.shape

        log_and_print(f'EXPORTED ' + str({pd.shape[0]}) + f' rows from table {sql_name}')

       


    except Exception as e:

        log_and_print("#######################################")

        log_and_print("ERROR: unable to READ table " + sql_name +  " Aborting with no action taken!")

        log_and_print("#######################################")

        log_and_print(e)


#######################################
# MAIN LOGIC
#######################################

from igapa2_linkage import *

sql_name = 'EXA_DB_SIZE_HOURLY'

mysql = 'hdd_write.sql'

if len(sys.argv) > 1:

    if len(sys.argv[10]) > 0:

        sql_name = sys.argv[10]

        mysql    = sys.argv[11]

my_pgm = os.path.basename(__file__)

my_path = os.getcwd()

now = dt.today().strftime('%Y-%m-%d-%H:%M:%S')

logging_filename = os.path.basename(__file__)[0:(os.path.basename(__file__).index('.py'))] + '.log'

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'a', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')


log_and_print("#--------------------------------------#")

log_and_print("# Entering " + os.path.basename(__file__))

log_and_print("#--------------------------------------#")

log_and_print("called with sql_name -->" + sql_name )




currPath = os.getcwd()              # Directory you are in NOW

if DB_Linkage.pass_host:

    savePath = DB_Linkage.pass_host              # We will be creating this new sub-directory

else:

    savePath = config.dsn

myPath = (currPath + '/' + savePath)# The full path of the new sub-dir


#-----------------------------------#
# Set up place to save spreadsheet
#-----------------------------------#
if not os.path.exists(myPath):      # The directory you are in NOW
   
    os.makedirs(myPath)             # create a new dir below the dir your are in NOW

os.chdir(myPath)                    # move into the newly created sub-dir

log_and_print("working dir directory " + myPath )

subject= sql_name

saveFile=(subject + '.csv')    # The RESUlTS we are saving on a daily basis


#######################################
# Start the database connection using 
# pyexasol connector
#######################################

log_and_print("#--------------------------------------#")

log_and_print("# Entering " + os.path.basename(__file__))

log_and_print("#--------------------------------------#")


try:

    if DB_Linkage.pass_host:

        pass

    else:

        DB_Linkage.pass_host = config.dsn

    if DB_Linkage.pass_port:

        pass

    else:

        DB_Linkage.pass_port = config.port

    if DB_Linkage.pass_user:

        pass

    else:

        DB_Linkage.pass_user = config.user

    if DB_Linkage.pass_pw:

        pass

    else:

        DB_Linkage.pass_pw = config.password

    if DB_Linkage.pass_schema:

        pass

    else:

        DB_Linkage.pass_schema = config.schema
    
    log_and_print("calling with: DB_Linkage.pass_host: " + DB_Linkage.pass_host + " DB_Linkage.pass_port " + str(DB_Linkage.pass_port))

    C = pyexasol.connect(dsn=(DB_Linkage.pass_host + ":" + str(DB_Linkage.pass_port)), user=DB_Linkage.pass_user, password=DB_Linkage.pass_pw, schema=DB_Linkage.pass_schema, compression=True)

    log_and_print("successfully connected to database using schema " +  DB_Linkage.pass_schema)

except Exception as e:

    log_and_print("########################################")

    log_and_print("ERROR: Unable to connect using " +  DB_Linkage.pass_user + ":" + " <secret> " +  "with schema:" +  DB_Linkage.pass_schema)

    log_and_print("########################################")
    
    log_and_print(e)

    raise AttributeError("# " + os.path.basename(__file__) + ": Unable to connect to " + DB_Linkage.pass_host + ":" + DB_Linkage.pass_port)
    
    sys.exit(12)

export_table(sql_name, mysql)

saveFile=(sql_name + '.csv')    # The RESUlTS we are saving on a daily basis

if os.path.exists(saveFile):

    pass

else:

    log_and_print("########################################")

    log_and_print("ERROR: Unable to find " + saveFile + ". Aborting here.")

    log_and_print("########################################")
    
    log_and_print(e)

    raise AttributeError("# " + os.path.basename(__file__) + ": Unable to find " + saveFile + ". Aborting here")
    
    sys.exit(12)

try:
   
    subr_rc = subprocess.call(["python", (currPath + "/" + "tools_create_config.py")
                                               , myPath
                                               , saveFile
                                               ])
except Exception as e:

    log_and_print("########################################")

    log_and_print("ERROR: call to tools_create_config failed. See export_sql_to_csv.log for details. Aborting.")

    log_and_print("########################################")

    log_and_print(e)

    sys.exit(12)

if subr_rc > 0 :

    log_and_print("########################################")

    log_and_print("ERROR: call to tools_create_config failed. See tools_create_config.log for details. Aborting.")

    log_and_print("########################################")

    sys.exit(12)
