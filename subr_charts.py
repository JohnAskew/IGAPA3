#! python3
#------------------------------------#
# This section will install python 
# modules needed to run this script
#------------------------------------#
import os, sys

#sys.path.insert(0, 'C:\\Users\\joas\\Desktop\\Exasol\\IGAPA3\\chromedriver.exe')
#print("Sys.Path =" + str(sys.path))
try:

    import base64

except:

    os.system('pip install base64')

    import base64

try:

    import selenium

    from selenium import webdriver

except:

    os.system('pip install selenium')

    import selenium

    from selenium import webdriver

try:

    import phantomjs

except:

    os.system('pip install phantomjs')

    import phantomjs

try:

    from PIL import Image

except:

    os.system('pip install PIL')

    from PIL import Image

try:
    import ntpath

except:

    os.system('pip install ntpath')

    import ntpath


my_pgm = ntpath.basename(os.path.basename(__file__))


logging_filename = ("./logs/" + my_pgm[0:(my_pgm.index('.py'))] + '.log')

try:

    from statistics import mean

except:

    os.system('pip install statistics')

    from statistics import mean

try:

    import numpy as np

    from numpy.polynomial import Polynomial

except:

    os.system('pip install numpy')

    import numpy as np

    from numpy.polynomial import Polynomial

try:

    import bokeh

    from bokeh.io import show

    from bokeh.plotting import figure, output_file, show

    from bokeh.layouts import column, gridplot

    from bokeh.models import ColumnDataSource, Legend, LabelSet, Label, LegendItem, Div, HoverTool, NumeralTickFormatter, ColorPicker

    from bokeh.io import export_png


except:

    os.system('pip install bokeh')

    from bokeh.plotting import figure, output_file, show

    from bokeh.layouts  import column, gridplot

    from bokeh.models import ColumnDataSource, Legend, LabelSet, Label, LegendItem, Div, HoverTool, NumeralTickFormatter, ColorPicker

    from bokeh.io import export_png

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

    import shutil

except:

    os.system('pip install shutil')

    import shutil

try:

    import numpy as np

except:

    os.system("pip install numpy")


try:

    import datetime as dt

    from datetime import date

    from datetime import time, timedelta

except:

    os.system('pip install datetime')

    import datetime as dt

    from datetime import date

    from datetime import time, timedelta

try:
    
    import configparser

except:
    
    os.system('pip install configparser')
    
    import configparser

try:

    from tools_parse_config import ParseConfig

except:
    
    msg = "Unable to find tools_parse_config.py"

    print("#######################################")

    print("# ERROR in", os.path.basename(__file__))
    
    print(msg)

    print("#", os.path.basename(__file__), "aborting with no action taken.")

    print("#######################################")

    sys.exit(13)

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

    import time

except:

    os.system("pip install time")

    import time

from igapa3_predictor import Predictor

my_pgm = os.path.basename(__file__)

now = dt.today().strftime('%Y%m%d_%H%M%S')

logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'a', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

log_level = "INFO"

outlier_threshold = float(3.0)
  
#######################################
# FUNCTTIONS BEFORE MAIN CODE
#######################################

#-------------------------------------#
def best_fit(xs, ys):
#-------------------------------------#
    m = 0

    b = 0

    m = (  ( (mean(xs) * mean(ys)) - mean(xs * ys) )  /
           ( (mean(xs) * mean(xs)) - mean(xs * xs))
        )

    if np.all(np.isnan(m)):

        m = -0
 
    b = mean(ys) - m * mean(xs)


    if np.all(np.isnan(b)):

        b = -0
  
    return m, b

#-------------------------------------#
def date_to_seconds(timestamp):
#-------------------------------------#

    d = dt.strptime(str(timestamp), "%Y-%m-%d %H:%M:%S")

    secs = time.mktime(d.timetuple())

    #print("secs: " + str(secs))
    
    return int(secs)

#-------------------------------------#
def my_logger(orig_func):
#-------------------------------------#
    import logging

    mylogr = logging.getLogger(orig_func.__name__)

    mylogr.setLevel(logging.INFO)

    mylogr_fh = logging.FileHandler('{}.log'.format(orig_func.__name__))

    mylogr_fmt = ('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

    formatter = logging.Formatter(mylogr_fmt)

    mylogr_fh.setFormatter(formatter)

    mylogr.addHandler(mylogr_fh)

    def wrapper(*args, **kwargs):

        mylogr.info(

            'Function {} Ran with arg: {} and kwargs {}'.format(orig_func.__name__, args, kwargs))

        return orig_func(*args, **kwargs)

    return wrapper

#-------------------------------------#
def log_and_print(msg = ''):
#-------------------------------------#

    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)


#######################################
# Set up processinging logic
#######################################

save_dir = os.getcwd() 

log_and_print("#--------------------------------------#")

log_and_print("# Entering " +  os.path.basename(__file__))

log_and_print("#--------------------------------------#")

if __name__ == "__main__":

    if len(sys.argv) > 1:

        log_and_print("using host_name as the directory to process in:  " + sys.argv[1])

        in_ticket = sys.argv[1]

    else:
       
        in_ticket = 'EXA-28615'

    if len(sys.argv) > 2:

        class_chart = 'DB_SIZE'

        config_in   = sys.argv[2]

        log_and_print("received these arguments: in_ticket " + str(in_ticket) + " config_in: " + config_in)

    else:

        class_chart = 'DB_SIZE'

        config_in = 'config_report2.ini'

    log_and_print("received these arguments: in_ticket " + str(in_ticket) + " config_in: " + config_in)

else:
   
    in_ticket = sys.argv[1]

    config_in = sys.argv[2]

    log_and_print("#------------------------------------#")
  
    log_and_print("# Entering " +  os.path.basename(__file__))

    log_and_print("#------------------------------------#")

    log_and_print("# received these arguments: in_ticket " + str(in_ticket) + " config_in: " + config_in)


in_dir = "./"


#######################################
# C H A N G E    D I R E C T O R Y
#######################################

os.chdir(in_dir) 

#######################################
# VARIABLES
#######################################

dailySYSTABLE = ""

reports_daily = 30

reports_hourly = 168                          #HOURLY SYS Table over past week

N_hourly_days = 7                      #Needs to match reports_hourly 


try:

    b = ParseConfig(class_chart, config_in)

except Exception as e:

    log_and_print("#######################################")

    log_and_print("FATAL: " + os.path.basename(__file__))

    log_and_print("# " + os.path.basename(__file__) + " Unable to reference ParseConfig using:")

    log_and_print("# b = ParseConfig(class_chart)")

    log_and_print("# Does pgm tools_parse_config.py exist in " + os.getcwd(),"?" )

    log_and_print("# " + os.path.basename(__file__) + " Aborting with no action taken.")

    logging.error(e, exc_info = True)

    print(e)

    log_and_print("#######################################")

    sys.exit(13)

config_sections = b.read_config_sections(save_dir)

if len(config_sections) == 0:

    log_and_print("FATAL: " + os.path.basename(__file__))

    log_and_print("# " + os.path.basename(__file__) + " unable to reference ParseConfig using:")

    log_and_print("# config_sections = b.read_config_sections()")

    log_and_print("# Does pgm tools_parse_config.py exist in " + os.getcwd(),"?" )

    log_and_print("# " + os.path.basename(__file__) + " Aborting with no action taken.")

    sys.exit(13)

for item in config_sections:

    log_and_print("received this section from tool_parse_config: " + item)


legend_font_size, legend_location, plotWidth, plotHeight, smallplotWidth, smallplotHeight, largeplotWidth, largeplotHeight = b.read_config_admin_layout(save_dir, 'config_admin.ini')

plotWidth       = int(plotWidth)

plotHeight      = int(plotHeight)

smallplotWidth  = int(smallplotWidth)

smallplotHeight = int(smallplotHeight)

largeplotWidth  = int(largeplotWidth)

largeplotHeight = int(largeplotHeight)

#######################################
# Parse Config - get REPORTING secttion items
#######################################

try:

    log_level, outlier_threshold, reports_hourly, reports_daily = b.read_config_admin_reporting(save_dir, 'config_admin.ini')

    log_and_print("# " + os.path.basename(__file__) + " REPORTING variables log_level " + log_level +
                                                           " outlier_threshold "  + outlier_threshold    + 
                                                           " reports_hourly "     + reports_hourly       + 
                                                           " reports_daily "      + reports_daily)
    reports_hourly = int(reports_hourly)

    reports_daily  = int(reports_daily)

    N_hourly_days =  int((reports_hourly) / 24)


except:

    log_and_print_warning("WARNING: " + os.path.basename(__file__))

    log_and_print_warning("# " + os.path.basename(__file__) + " unable to reference REPORTING section of config_admin.ini")

    log_and_print_warning("# Using defaults:")

    log_and_print_warning("# ==> log_level " + log_level)

    log_and_print_warning("# ==> outlier_threshold " + outlier_threshold)

try:

    if len(outlier_threshold) > 0:

        outlier_threshold = float(outlier_threshold)

except:
     

    log_and_print_warning("WARNING: " + os.path.basename(__file__))

    log_and_print_warning("# " + os.path.basename(__file__) + " unable to process config_admin.ini REPORTING variable outlier_threshold")

    log_and_print_warning("# Using defaults:")

    log_and_print_warning("# ==> log_level " + log_level)

    log_and_print_warning("# ==> outlier_threshold " + outlier_threshold)


CONFIG_HOURLY_TBL        = False
CONFIG_ROW1_COL_X_AXIS   = False
CONFIG_ROW1_COL_Y_AXIS_1 = False
CONFIG_ROW1_COL_Y_AXIS_2 = False
CONFIG_ROW2_COL_X_AXIS   = False
CONFIG_ROW2_COL_Y_AXIS_1 = False
CONFIG_ROW2_COL_Y_AXIS_2 = False
CONFIG_ROW3_COL_X_AXIS   = False
CONFIG_ROW3_COL_Y_AXIS_1 = False
CONFIG_ROW3_COL_Y_AXIS_2 = False
CONFIG_ROW4_COL_X_AXIS   = False
CONFIG_ROW4_COL_Y_AXIS_1 = False
CONFIG_ROW4_COL_Y_AXIS_2 = False
COLS_TBL1 = False
COLS_TBL2 = False
COLS_TBL3 = False
COLS_TBL4 = False


#######################################
# LOOP for duration of the program
#
# #      # # #   # # #   #  #
# #      #   #   #   #   #    #
# #      #   #   #   #   #  #
# #      #   #   #   #   #
# # # #  # # #   # # #   #
# 
########################################


os.chdir(in_ticket)

for config_section in config_sections:

    log_and_print("config_section: " + config_section + " config_in: " + config_in)

    process_section = ParseConfig(config_section, config_in) 

    CONFIG_HOURLY_TBL,CONFIG_ROW1_COL_X_AXIS,CONFIG_ROW1_COL_Y_AXIS_1,CONFIG_ROW1_COL_Y_AXIS_2,CONFIG_ROW2_COL_X_AXIS,CONFIG_ROW2_COL_Y_AXIS_1,CONFIG_ROW2_COL_Y_AXIS_2,CONFIG_ROW3_COL_X_AXIS,CONFIG_ROW3_COL_Y_AXIS_1,CONFIG_ROW3_COL_Y_AXIS_2,CONFIG_ROW4_COL_X_AXIS,CONFIG_ROW4_COL_Y_AXIS_1,CONFIG_ROW4_COL_Y_AXIS_2 = process_section.run(save_dir)

    if CONFIG_ROW1_COL_X_AXIS:

        if  CONFIG_ROW1_COL_Y_AXIS_1:

            if CONFIG_ROW1_COL_Y_AXIS_2:

               COLS_TBL1 = [CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2]

            else:

                COLS_TBL1 = [CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1]
    else:

        COLS_TBL1 = False

    if   CONFIG_ROW2_COL_X_AXIS:

        if  CONFIG_ROW2_COL_Y_AXIS_1:

            if CONFIG_ROW2_COL_Y_AXIS_2:

               COLS_TBL2 = [CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2]

            else:

                COLS_TBL2 = [CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1]
    else:
        
        COLS_TBL2 = False


    if   CONFIG_ROW3_COL_X_AXIS:

        if  CONFIG_ROW3_COL_Y_AXIS_1:

            if CONFIG_ROW3_COL_Y_AXIS_2:

               COLS_TBL3 = [CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2]

            else:

                COLS_TBL3 = [CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1]
    else:
        
        COLS_TBL3 = False

    if   CONFIG_ROW4_COL_X_AXIS:

        if  CONFIG_ROW4_COL_Y_AXIS_1:

            if CONFIG_ROW4_COL_Y_AXIS_2:

               COLS_TBL4 = [CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2]

            else:

                COLS_TBL4 = [CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1]
    else:
        
        COLS_TBL4 = False

    log_and_print("Processing\tConfig section:\t " + config_section)

    log_and_print("Processing\tCONFIG_HOURLY_TBL:\t " + CONFIG_HOURLY_TBL)

#######################################
# Set up directory to use
#######################################

    currPath = os.getcwd()              # Directory you are in NOW

    log_and_print()

    log_and_print("About to process TABLES in dir " + currPath)

    log_and_print()


###############################################################################
#   #######   #     ####    #      ######  ##
#      #     #  #   #   #   #      #        #
#      #    ######  ####    #      ###      #
#      #    #    #  #   #   #      #        #
#      #    #    #  ####    #####  ###### #####
###############################################################################

#######################################
# Extract TBL1 Hourly Records
#######################################

    try:

        df_hourly_full_tbl_1 = pd.read_csv(CONFIG_HOURLY_TBL + '.csv')

    except Exception as e:

        log_and_print("# FATAL ERROR in " + os.path.basename(__file__))

        log_and_print("# ---> File is NOT FOUND!")

        log_and_print("# " + os.path.basename(__file__) + " config.ini section:\t " + config_section)

        log_and_print("# which specified:\t " + CONFIG_HOURLY_TBL)

        log_and_print("# Needs CSV file:\t " + str(CONFIG_HOURLY_TBL + '.csv'))

        log_and_print("# in directory:\t\t " + in_dir + ".")

        log_and_print("#  " + os.path.basename(__file__) + " Aborting with no action taken.")

        logging.error(e, exc_info = True)

        print(e)

        sys.exit(13)

    if df_hourly_full_tbl_1.empty:

        log_and_print("#######################################")

        log_and_print("#-------------------------------------#")

        log_and_print(CONFIG_HOURLY_TBL + '.csv' + " is EMPTY. Skipping with no action taken.")

        log_and_print("# --> The CSV had this many rows: " + str(df_hourly_full_tbl_1.shape[0]) + " and this many columns: " +  str(df_hourly_full_tbl_1.shape[1]))

        log_and_print("# --> Are you running a  query containing profile tables without profiling enabled?")

        log_and_print("# --> Are you running a query containing audit tables without auditing enabled?")

        log_and_print("#-------------------------------------#")

        log_and_print("#######################################")

        sys.exit(0)


    try:

        df_hourly_full_tbl_1 = df_hourly_full_tbl_1[COLS_TBL1]

        df_hourly_full_tbl_1_extracted = df_hourly_full_tbl_1.shape[0]


    except Exception as e:

        log_and_print("# " + os.path.basename(__file__) + " unable to read " + CONFIG_HOURLY_TBL + " skipping!")

        log_and_print("# " + os.path.basename(__file__) + " Aborting with no action taken.")

        logging.error(e, exc_info = True)

        print(e)

        sys.exit(13)


    try:

        df_hourly_full_tbl_1[CONFIG_ROW1_COL_X_AXIS] = pd.to_datetime(df_hourly_full_tbl_1[CONFIG_ROW1_COL_X_AXIS], errors = 'coerce')

        df_hourly_full_tbl_1.dropna(inplace = True)


    except Exception as e:

        log_and_print("#Error!")

        log_and_print("Unable to parse CONFIG_ROW1_COL_X_AXIS")

        log_and_print("when trying to set datetime using pd.to_datetime." )

        logging.error(e, exc_info = True)

        print(e)

        log_and_print("#-------------------------------------#")

        log_and_print("Aborting with no action taken.")

        log_and_print("#-------------------------------------#")

        sys.exit(13)
 
    if df_hourly_full_tbl_1.empty:

        log_and_print("#######################################")

        log_and_print("#-------------------------------------#")

        log_and_print(CONFIG_HOURLY_TBL + '.csv' + " could not parse 1st column as datetime. Skipping with no action taken.")

        log_and_print("# --> The CSV had this many rows: " + str(df_hourly_full_tbl_1.shape[0]) + " and this many columns: " +  str(df_hourly_full_tbl_1.shape[1]))

        log_and_print("# --> Are you running a  query containing profile tables without profiling enabled?")

        log_and_print("# --> Are you running a query containing audit tables without auditing enabled?")

        log_and_print("#-------------------------------------#")

        log_and_print("#######################################")

        sys.exit(0)



    date_max_hourly = df_hourly_full_tbl_1[CONFIG_ROW1_COL_X_AXIS].max()

    if str(date_max_hourly) == '1970-01-01 00:00:00':

        log_and_print("#######################################")

        log_and_print("#-------------------------------------#")

        log_and_print(CONFIG_HOURLY_TBL + '.csv' + " could not find valid date for first column. Skipping with no action taken.")

        log_and_print("# --> The CSV had this many rows: " + str(df_hourly_full_tbl_1.shape[0]) + " and this many columns: " +  str(df_hourly_full_tbl_1.shape[1]))

        log_and_print("# --> Are you running a  query containing profile tables without profiling enabled?")

        log_and_print("# --> Are you running a query containing audit tables without auditing enabled?")

        log_and_print("#-------------------------------------#")

        log_and_print("#######################################")

        sys.exit(0)

    log_and_print("read " + CONFIG_HOURLY_TBL +  " date_max_hourly: " + str(date_max_hourly))

    #######################################
    # For TBL1 Hourly Table - read past 5 days
    #######################################   

    date_reports_hourly_ago = date_max_hourly - timedelta(hours= reports_hourly)

    df_hourly_work_tbl_1 = pd.DataFrame(df_hourly_full_tbl_1, columns = COLS_TBL1).copy(deep = True)

    df_hourly_work_tbl_1.reset_index(inplace = True, drop = True)

    df_hourly_work_tbl_1[CONFIG_ROW1_COL_X_AXIS] = pd.to_datetime(df_hourly_work_tbl_1[CONFIG_ROW1_COL_X_AXIS], errors = 'coerce')

    df_hourly_work_tbl_1.dropna(inplace = True)

    mask = (df_hourly_work_tbl_1[CONFIG_ROW1_COL_X_AXIS] >  date_reports_hourly_ago )

    df_hourly_7_day_tbl_1 = df_hourly_work_tbl_1.loc[mask].copy(deep = True)

      


    ###############################################################################
    #   #######   #     ####    #      ######  ###
    #      #     #  #   #   #   #      #      #   #
    #      #    ######  ####    #      ###       #
    #      #    #    #  #   #   #      #        #
    #      #    #    #  ####    #####  ######  ####
    ###############################################################################


    #######################################
    # Extract TBL2 Hourly Records
    #######################################

    if COLS_TBL2:

        try:

            df_hourly_full_tbl_2 = pd.read_csv(CONFIG_HOURLY_TBL + '.csv', usecols = COLS_TBL2)

            df_hourly_full_tbl_2_extracted = df_hourly_full_tbl_2.shape[0]


        except Exception as e:

            log_and_print("Unable to READ " + CONFIG_HOURLY_TBL + "...Aborting with no action taken.")

            logging.error(e, exc_info = True)

            print(e)

            sys.exit(13)

  

        #######################################
        #  Set CONFIG_ROW1_COL_X_AXIS as timestamp for Hourly full tbl 2
        #######################################

        df_hourly_full_tbl_2[CONFIG_ROW1_COL_X_AXIS] = pd.to_datetime(df_hourly_full_tbl_2[CONFIG_ROW1_COL_X_AXIS], errors = 'coerce')

        df_hourly_full_tbl_2.dropna(inplace = True)

        #######################################
        # For TBL2 Hourly Table - read past 5 days
        #######################################   

        date_reports_hourly_ago = date_max_hourly - timedelta(hours= reports_hourly)

        df_hourly_work_tbl_2 = pd.DataFrame(df_hourly_full_tbl_2, columns = COLS_TBL2).copy(deep = True)



        df_hourly_work_tbl_2.reset_index(inplace = True, drop = True)

        df_hourly_work_tbl_2[CONFIG_ROW1_COL_X_AXIS] = pd.to_datetime(df_hourly_work_tbl_2[CONFIG_ROW1_COL_X_AXIS])

        mask = (df_hourly_work_tbl_2[CONFIG_ROW1_COL_X_AXIS] >  date_reports_hourly_ago )

        df_hourly_7_day_tbl_2 = df_hourly_work_tbl_2.loc[mask].copy(deep = True) 



    ###############################################################################
    #   #######   #     ####    #      ######  ####
    #      #     #  #   #   #   #      #         #
    #      #    ######  ####    #      ###      ####
    #      #    #    #  #   #   #      #           #
    #      #    #    #  ####    #####  ###### #####
    ###############################################################################

    #######################################
    # Extract TBL3 Hourly Records
    #######################################

    if COLS_TBL3:

        try:

            df_hourly_full_tbl_3 = pd.read_csv(CONFIG_HOURLY_TBL + '.csv', usecols = COLS_TBL3)

            df_hourly_full_tbl_3_extracted = df_hourly_full_tbl_3.shape[0]


        except Exception as e:

            log_and_print("Unable to READ " + CONFIG_HOURLY_TBL + " ...Aborting with no action taken.")

            logging.error(e, exc_info = True)

            print(e)

            sys.exit(13)



        #######################################
        # Read the max df_hourly_full_tbl_3 timestamp
        #######################################

        df_hourly_full_tbl_3[CONFIG_ROW1_COL_X_AXIS] = pd.to_datetime(df_hourly_full_tbl_3[CONFIG_ROW1_COL_X_AXIS], errors = 'coerce')

        df_hourly_full_tbl_3.dropna(inplace = True)

        date_max_hourly = df_hourly_full_tbl_3[CONFIG_ROW1_COL_X_AXIS].max()

        #######################################
        # For TBL3 Hourly Table - read past 5 days
        #######################################   

        date_reports_hourly_ago = date_max_hourly - timedelta(hours= reports_hourly)

        df_hourly_work_tbl_3 = pd.DataFrame(df_hourly_full_tbl_3, columns = COLS_TBL3).copy(deep = True)

        df_hourly_work_tbl_3.reset_index(inplace = True, drop = True)

        df_hourly_work_tbl_3[CONFIG_ROW1_COL_X_AXIS] = pd.to_datetime(df_hourly_work_tbl_3[CONFIG_ROW1_COL_X_AXIS])

        mask = (df_hourly_work_tbl_3[CONFIG_ROW1_COL_X_AXIS] >  date_reports_hourly_ago )

        df_hourly_7_day_tbl_3 = df_hourly_work_tbl_3.loc[mask].copy(deep = True)


    ###############################################################################
    #   #######   #     ####    #      ######    #
    #      #     #  #   #   #   #      #       # #
    #      #    ######  ####    #      ###    ######
    #      #    #    #  #   #   #      #         #
    #      #    #    #  ####    #####  ######  ####
    ###############################################################################


    #######################################
    # Extract TBL4 Hourly Records
    #######################################

    if COLS_TBL4:

        try:

            df_hourly_full_tbl_4 = pd.read_csv(CONFIG_HOURLY_TBL + '.csv', usecols = COLS_TBL4)#  export_params={"columns": COLS_TBL4}) #["INTERVAL_START",CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2]})

            df_hourly_full_tbl_4_extracted = df_hourly_full_tbl_4.shape[0]


        except Exception as e:

            log_and_print("Unable to READ " + CONFIG_HOURLY_TBL + " ...Aborting with no action taken.")

            logging.error(e, exc_info = True)

            log_and_print(str(e))


        #######################################
        #  Set CONFIG_ROW1_COL_X_AXIS as timestamp for Hourly full tbl 2
        #######################################

        df_hourly_full_tbl_4[CONFIG_ROW1_COL_X_AXIS] = pd.to_datetime(df_hourly_full_tbl_4[CONFIG_ROW1_COL_X_AXIS], errors='coerce')

        df_hourly_full_tbl_4.dropna(inplace = True)

        #######################################
        # For TBL4 Hourly Table - read past 5 days
        #######################################   

        date_reports_hourly_ago = date_max_hourly - timedelta(hours= reports_hourly)

        df_hourly_work_tbl_4 = pd.DataFrame(df_hourly_full_tbl_4, columns = COLS_TBL4).copy(deep = True) #["INTERVAL_START", CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2])


        df_hourly_work_tbl_4.reset_index(inplace = True, drop = True)

        df_hourly_work_tbl_4[CONFIG_ROW1_COL_X_AXIS] = pd.to_datetime(df_hourly_work_tbl_4[CONFIG_ROW1_COL_X_AXIS])

        mask = (df_hourly_work_tbl_4[CONFIG_ROW1_COL_X_AXIS] >  date_reports_hourly_ago )

        df_hourly_7_day_tbl_4 = df_hourly_work_tbl_4.loc[mask].copy(deep = True) 

#######################################
# DATA CLEAN UP  - Charts Row 1 Set NULLS To 0.
#######################################

    df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1].fillna(0, inplace = True)

    if CONFIG_ROW1_COL_Y_AXIS_2:

        df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2].fillna(0, inplace = True)

    df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1].fillna(0, inplace = True)

    if CONFIG_ROW1_COL_Y_AXIS_2:

        df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2].fillna(0, inplace = True)



#######################################
# DATA CLEAN UP  - Charts Row 2 Set NULLS To 0.
#######################################

    if COLS_TBL2:

        df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1].fillna(0, inplace = True)

        if CONFIG_ROW2_COL_Y_AXIS_2:

            df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2].fillna(0, inplace = True)

        df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1].fillna(0, inplace = True)

        if CONFIG_ROW2_COL_Y_AXIS_2:

            df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2].fillna(0, inplace = True)


#######################################
# DATA CLEAN UP  - Charts Row 3 Set NULLS To 0.
#######################################
    if COLS_TBL3:

        df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1].fillna(0, inplace = True)

        if CONFIG_ROW3_COL_Y_AXIS_2:

            df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2].fillna(0, inplace = True)

        df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1].fillna(0, inplace = True)

        if CONFIG_ROW3_COL_Y_AXIS_2:

            df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2].fillna(0, inplace = True)

   
#######################################
# DATA CLEAN UP  - Charts Row 4 Set NULLS To 0.
#######################################

    if COLS_TBL4:

        df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1].fillna(0, inplace = True)

        if CONFIG_ROW4_COL_Y_AXIS_2:

            df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2].fillna(0, inplace = True)

        df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1].fillna(0, inplace = True)

        if CONFIG_ROW4_COL_Y_AXIS_2:

            df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2].fillna(0, inplace = True)

 
    ###############################################################################
    # Convert Hourly full TBL1 CONFIG_ROW1_COL_Y_AXIS_1 / _2 to float
    ###############################################################################

    try:
    
        df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1] = df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1].astype(float)

    except Exception as e:

        log_and_print("##########################################")

        log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW1_COL_Y_AXIS_1 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

        log_and_print("##########################################")

        log_and_print(str(e))

        sys.exit(12)

    if CONFIG_ROW1_COL_Y_AXIS_2:

        try:

            df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2] = df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2].astype(float)

        except Exception as e:

            log_and_print("##########################################")

            log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW1_COL_Y_AXIS_2 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

            log_and_print("##########################################")

            log_and_print(str(e))

            sys.exit(12)

    ###############################################################################
    # Convert Hourly 5 day TBL1 CONFIG_ROW1_COL_Y_AXIS_1 / _2 to float
    ###############################################################################

    try:

        df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1] = df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1].astype(float)

    except Exception as e:

        log_and_print("##########################################")

        log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW1_COL_Y_AXIS_1 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

        log_and_print("##########################################")

        log_and_print(str(e))

        sys.exit(12)

    if CONFIG_ROW1_COL_Y_AXIS_2:

        try:

            df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2] = df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2].astype(float)

        except Exception as e:

            log_and_print("##########################################")

            log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW1_COL_Y_AXIS_2 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

            log_and_print("##########################################")

            log_and_print(str(e))

            sys.exit(12)


  
    ###############################################################################
    # Convert Hourly full TBL2 CONFIG_ROW2_COL_Y_AXIS_1 / _2 to float
    ###############################################################################

    if COLS_TBL2:

        try:

            df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1] = df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1].astype(float)

        except Exception as e:

            log_and_print("##########################################")

            log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW2_COL_Y_AXIS_1 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

            log_and_print("##########################################")

            log_and_print(str(e))

            sys.exit(12)

        if CONFIG_ROW2_COL_Y_AXIS_2:

            try:

                df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2] = df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2].astype(float)

            except Exception as e:

                log_and_print("##########################################")

                log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW2_COL_Y_AXIS_2 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

                log_and_print("##########################################")

                log_and_print(str(e))

                sys.exit(12)

        ###############################################################################
        # Convert Hourly 5 day TBL2 CONFIG_ROW2_COL_Y_AXIS_1 / _2 to float
        ###############################################################################

        df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1] = df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1].astype(float)

        if CONFIG_ROW2_COL_Y_AXIS_2:

             df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2] = df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2].astype(float)

   
    ###############################################################################
    # Convert Hourly full TBL3 CONFIG_ROW3_COL_Y_AXIS_1 / _2 to float
    ###############################################################################

    if COLS_TBL3:

        try:

            df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1] = df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1].astype(float)

        except Exception as e:

            log_and_print("##########################################")

            log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW3_COL_Y_AXIS_1 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

            log_and_print("##########################################")

            log_and_print(str(e))

            sys.exit(12)

        if CONFIG_ROW3_COL_Y_AXIS_2:

            try:

                df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2] = df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2].astype(float)

            except Exception as e:

                log_and_print("##########################################")

                log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW3_COL_Y_AXIS_2 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

                log_and_print("##########################################")

                log_and_print(str(e))

                sys.exit(12)

        ###############################################################################
        # Convert Hourly 5 day TBL3 CONFIG_ROW3_COL_Y_AXIS_1 / _2 to float
        ###############################################################################

        df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1] = df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1].astype(float)

        if CONFIG_ROW3_COL_Y_AXIS_2:

            df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2] = df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2].astype(float)

        
    ###############################################################################
    # Convert Hourly full TBL4 CONFIG_ROW4_COL_Y_AXIS_1 / _2 to float
    ###############################################################################

    if COLS_TBL4:

        try:

            df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1] = df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1].astype(float)

        except Exception as e:

            log_and_print("##########################################")

            log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW4_COL_Y_AXIS_1 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

            log_and_print("##########################################")

            log_and_print(str(e))

            sys.exit(12)

        if CONFIG_ROW4_COL_Y_AXIS_2:

            try:

                df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2] = df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2].astype(float)

            except Exception as e:

                log_and_print("##########################################")

                log_and_print("FATAL! Unable to numerically parse " + CONFIG_ROW4_COL_Y_AXIS_1 + " in query " + CONFIG_HOURLY_TBL + ". Aborting now.")

                log_and_print("##########################################")

                log_and_print(str(e))

                sys.exit(12)

        ###############################################################################
        # Convert Hourly 5 day TBL4 CONFIG_ROW4_COL_Y_AXIS_1 / _2 to float
        ###############################################################################

        df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1] = df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1].astype(float)

        if CONFIG_ROW4_COL_Y_AXIS_2:

            df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2] = df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2].astype(float)


    

    ###############################################################################
    # #         # #########  ####### #       # 
    #  #       #      #     #        #       #
    #   #     #       #       #      #       #
    #    #   #        #         #    #       #
    #     # #         #           #  #       #
    #      #      ########## ####### ######### als   (fine, you type it out)
    ###############################################################################   


    output_title = str(config_section + '_' + str(now) +  '.html')

    output_file(output_title, title = config_section)

    outfile = (str(config_section + '_' + str(now) +  '.png'))


    

    ###############################################################################
    #   #######   #     ####    #      ######  ##
    #      #     #  #   #   #   #      #        #
    #      #    ######  ####    #      ###      #
    #      #    #    #  #   #   #      #        #
    #      #    #    #  ####    #####  ###### #####
    ###############################################################################

    #######################################
    # Visualize Hourly Past  5 Day Data
    #######################################

    line1_tbl1_hourly_7_day = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

    line1_tbl1_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  CONFIG_HOURLY_TBL)

    line1_tbl1_hourly_7_day.title.align = "center"

    line1_tbl1_hourly_7_day.title.text_color = "white"

    line1_tbl1_hourly_7_day.title.text_font_size = "15px"

    line1_tbl1_hourly_7_day.title.background_fill_color = "darkblue"

    if CONFIG_ROW1_COL_Y_AXIS_2:

        line1_tbl1_hourly_7_day.diamond( x=CONFIG_ROW1_COL_X_AXIS, y = CONFIG_ROW1_COL_Y_AXIS_2 , line_width = 2, alpha = 0.5, color=("red"),  source=df_hourly_7_day_tbl_1, legend_label = (CONFIG_ROW1_COL_Y_AXIS_2) )

    line1_tbl1_hourly_7_day.circle( x=CONFIG_ROW1_COL_X_AXIS, y = CONFIG_ROW1_COL_Y_AXIS_1 , line_width = 1.5, alpha = 0.5, color=("blue"), source=df_hourly_7_day_tbl_1, legend_label = (CONFIG_ROW1_COL_Y_AXIS_1))

    line1_tbl1_hourly_7_day.legend.location = legend_location #legend_location

    line1_tbl1_hourly_7_day.legend.label_text_font_size = legend_font_size

    line1_tbl1_hourly_7_day.yaxis[0].formatter = NumeralTickFormatter(format="1,000") 

#######################################
# Calculate the BEST_FIT line against _MAX
#######################################

    if CONFIG_ROW1_COL_Y_AXIS_2:

        int_list = []

        for mydate in df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_X_AXIS]:

           try:

               int_list.append(date_to_seconds(mydate))

           except:

               int_list.append(date_to_seconds(str(mydate)[:19]))

           int_list = sorted(int_list)

        xs = np.array(int_list, dtype = float)

        ys = np.array(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2], dtype = float)

        m, b = best_fit(xs, ys)

        regression_line = [ (m * x) + b  for x in xs]

        XYZ = line1_tbl1_hourly_7_day.line(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_X_AXIS], regression_line, color = '#1EB913', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + CONFIG_ROW1_COL_Y_AXIS_2)

        picker = ColorPicker(title = 'Best Fit ROW 1')
        
        picker.js_link('color', XYZ.glyph, 'line_color')

    #######################################
    # Calculate the OUTLIERS
    #######################################

        my_mean = np.mean(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2])

        my_std  = np.std(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2])

        for count, i in enumerate(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2]):

            try:

                if my_std != 0:

                    if ( ( i - my_mean ) / my_std ) > outlier_threshold:

                        line1_tbl1_hourly_7_day.circle( x=df_hourly_7_day_tbl_1.iloc[count:count+1,0], y = df_hourly_7_day_tbl_1.iloc[count:count+1,2] , line_width = 7, alpha = 0.5, color=("#CCC000"), legend_label = CONFIG_ROW1_COL_Y_AXIS_2 + " Outlier")
                        

            except Exception as e:

                    log_and_print("#--------------------------------------#")

                    log_and_print("Unable to calculate the outlier_threshold using i: " + str(i) + " my_mean " + str(my_mean) + " my_std " + str(my_std))

                    log_and_print("#--------------------------------------#")
    else:

        int_list = []

        for mydate in df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_X_AXIS]:

            int_list.append(date_to_seconds(mydate))

            int_list = sorted(int_list)

        xs = np.array(int_list, dtype = float)

        ys = np.array(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1], dtype = float)

        m, b = best_fit(xs, ys)

        regression_line = [ (m * x) + b  for x in xs]

        XYZ = line1_tbl1_hourly_7_day.line(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_X_AXIS], regression_line, color = '#1EB913', alpha = 0.1, line_width = 6, legend_label = 'BEST_FIT of ' + CONFIG_ROW1_COL_Y_AXIS_1)

        picker = ColorPicker(title = 'Best Fit ROW 1')
        
        picker.js_link('color', XYZ.glyph, 'line_color')

    #######################################
    # Calculate the OUTLIERS
    #######################################

        my_mean = np.mean(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1])

        my_std  = np.std(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1])

        for count, i in enumerate(df_hourly_7_day_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1]):

            try:

                if my_std != 0:

                    if ( ( i - my_mean ) / my_std ) > outlier_threshold:

                        line1_tbl1_hourly_7_day.circle( x=df_hourly_7_day_tbl_1.iloc[count:count+1,0], y = df_hourly_7_day_tbl_1.iloc[count:count+1,1] , line_width = 7, alpha = 0.3, color=("#CCC000"), legend_label = CONFIG_ROW1_COL_Y_AXIS_1 + " Outlier")


            except Exception as e:

                    log_and_print("#--------------------------------------#")

                    log_and_print("Unable to calculate the outlier_threshold using i: " + str(i) + " my_mean " + str(my_mean) + " my_std " + str(my_std))

                    log_and_print("#--------------------------------------#")

       

       

    #######################################
    # Visualized
    #######################################

    





    #######################################
    # Visualize Entire Data
    #######################################

    if CONFIG_ROW1_COL_Y_AXIS_2:

        vbar_tbl1_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[CONFIG_ROW1_COL_X_AXIS], 
                                           y1 = df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1], 
                                           y2 = df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2],
                                           ))
    else:
        
        vbar_tbl1_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[CONFIG_ROW1_COL_X_AXIS], 
                                           y1 = df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1]
                                           ))


    vbar_tbl1_tot_col1 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl1_tot_col1.title.text = (CONFIG_HOURLY_TBL)

    vbar_tbl1_tot_col1.title.align = "center"

    vbar_tbl1_tot_col1.title.text_color = "yellow" ##1EB913"

    vbar_tbl1_tot_col1.title.text_font_size = "15px"

    vbar_tbl1_tot_col1.title.background_fill_color = "darkblue"

    vbar_tbl1_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl1_source, legend_label = CONFIG_ROW1_COL_Y_AXIS_1)

    vbar_tbl1_tot_col1.legend.location = legend_location

    vbar_tbl1_tot_col1.legend.label_text_font_size = legend_font_size

    if CONFIG_ROW1_COL_Y_AXIS_2:

        varea_tbl1_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[CONFIG_ROW1_COL_X_AXIS], 
                                           y1 = df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1],
                                           y2 = df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_2],
                                           ))
    else:

        varea_tbl1_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_1[CONFIG_ROW1_COL_X_AXIS], 
                                           y1 = df_hourly_full_tbl_1[CONFIG_ROW1_COL_Y_AXIS_1]))

    vbar_tbl1_tot_col2 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

    vbar_tbl1_tot_col2.title.text = (CONFIG_HOURLY_TBL)

    vbar_tbl1_tot_col2.title.align = "center"

    vbar_tbl1_tot_col2.title.text_color = "yellow" ##1EB913"

    vbar_tbl1_tot_col2.title.text_font_size = "15px"

    vbar_tbl1_tot_col2.title.background_fill_color = "darkblue"

    if CONFIG_ROW1_COL_Y_AXIS_2:

        vbar_tbl1_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl1_stack_source, legend_label = CONFIG_ROW1_COL_Y_AXIS_2)

        vbar_tbl1_tot_col2.legend.location = legend_location

        vbar_tbl1_tot_col2.legend.label_text_font_size = legend_font_size



    ###############################################################################
    #   #######   #     ####    #      ######  ###
    #      #     #  #   #   #   #      #      #  #
    #      #    ######  ####    #      ###      #
    #      #    #    #  #   #   #      #       #
    #      #    #    #  ####    #####  ###### #####
    ###############################################################################
    #######################################
    # Visualize Hourly Past  5 Day Data
    #######################################

    if COLS_TBL2:

        line2_tbl2_hourly_7_day = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

        line2_tbl2_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  CONFIG_HOURLY_TBL)

        line2_tbl2_hourly_7_day.title.align = "center"

        line2_tbl2_hourly_7_day.title.text_color = "white"

        line2_tbl2_hourly_7_day.title.text_font_size = "15px"

        line2_tbl2_hourly_7_day.title.background_fill_color = "darkblue"

        if CONFIG_ROW2_COL_Y_AXIS_2:

            line2_tbl2_hourly_7_day.diamond( x=CONFIG_ROW2_COL_X_AXIS, y = CONFIG_ROW2_COL_Y_AXIS_2 , line_width = 2, alpha = 0.5, color=("red"),  source=df_hourly_7_day_tbl_2, legend_label = (CONFIG_ROW2_COL_Y_AXIS_2) )

        line2_tbl2_hourly_7_day.circle( x=CONFIG_ROW2_COL_X_AXIS, y = CONFIG_ROW2_COL_Y_AXIS_1 , line_width = 1.5, alpha = 0.5, color=("blue"), source=df_hourly_7_day_tbl_2, legend_label = (CONFIG_ROW2_COL_Y_AXIS_1))

        line2_tbl2_hourly_7_day.legend.location = legend_location #legend_location

        line2_tbl2_hourly_7_day.legend.label_text_font_size = legend_font_size

        line2_tbl2_hourly_7_day.yaxis[0].formatter = NumeralTickFormatter(format="1,000") 

    #######################################
    # Calculate the BEST_FIT line against _MAX
    #######################################

        if CONFIG_ROW2_COL_Y_AXIS_2:

            int_list = []

            for mydate in df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_X_AXIS]:

                try:

                    int_list.append(date_to_seconds(mydate))

                except:

                    int_list.append(date_to_seconds(str(mydate)[:19]))

                int_list = sorted(int_list)

            xs = np.array(int_list, dtype = float)

            ys = np.array(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2], dtype = float)

            m, b = best_fit(xs, ys)

            regression_line = [ (m * x) + b  for x in xs]

            XYZ2 = line2_tbl2_hourly_7_day.line(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_X_AXIS], regression_line, color = '#1EB913', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + CONFIG_ROW2_COL_Y_AXIS_2)

            picker2 = ColorPicker(title = 'Best Fit ROW 2')
        
            picker2.js_link('color', XYZ2.glyph, 'line_color')

        #######################################
        # Calculate the OUTLIERS
        #######################################

            my_mean = np.mean(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2])

            my_std  = np.std(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2])

            for count, i in enumerate(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2]):

                try:

                    if my_std !=0:

                        if ( ( i - my_mean ) / my_std ) > outlier_threshold:

                            line2_tbl2_hourly_7_day.circle( x=df_hourly_7_day_tbl_2.iloc[count:count+1,0], y = df_hourly_7_day_tbl_2.iloc[count:count+1,2] , line_width = 7, alpha = 0.5, color=("#CCC000"), legend_label = CONFIG_ROW2_COL_Y_AXIS_2 + " Outlier")

                except Exception as e:

                    log_and_print("#--------------------------------------#")

                    log_and_print("Unable to calculate the outlier_threshold using i: " + str(i) + " my_mean " + str(my_mean) + " my_std " + str(my_std))

                    log_and_print("#--------------------------------------#")
        else:

            int_list = []

            for mydate in df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_X_AXIS]:

                try:

                    int_list.append(date_to_seconds(mydate))

                except:

                    int_list.append(date_to_seconds(str(mydate)[:19]))

                int_list = sorted(int_list)

            xs = np.array(int_list, dtype = float)

            ys = np.array(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1], dtype = float)

            m, b = best_fit(xs, ys)

            regression_line = [ (m * x) + b  for x in xs]

            XYZ2 = line2_tbl2_hourly_7_day.line(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_X_AXIS], regression_line, color = '#1EB913', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + CONFIG_ROW2_COL_Y_AXIS_1)

            picker2 = ColorPicker(title = 'Best Fit ROW 2')
        
            picker2.js_link('color', XYZ2.glyph, 'line_color')
        #######################################
        # Calculate the OUTLIERS
        #######################################

            my_mean = np.mean(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1])

            my_std  = np.std(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1])

            for count, i in enumerate(df_hourly_7_day_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1]):

                try:

                    if my_std != 0:

                        if ( ( i - my_mean ) / my_std ) > outlier_threshold:

                            line2_tbl2_hourly_7_day.circle( x=df_hourly_7_day_tbl_2.iloc[count:count+1,0], y = df_hourly_7_day_tbl_2.iloc[count:count+1,1] , line_width = 7, alpha = 0.5, color=("#CCC000"), legend_label = CONFIG_ROW2_COL_Y_AXIS_1 + " Outlier")

                except Exception as e:

                    log_and_print("#--------------------------------------#")

                    log_and_print("Unable to calculate the outlier_threshold using i: " + str(i) + " my_mean " + str(my_mean) + " my_std " + str(my_std))

                    log_and_print("#--------------------------------------#")

           
        #######################################
        # Visualize Entire Data
        #######################################

        if CONFIG_ROW2_COL_Y_AXIS_2:

            vbar_tbl2_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_2[CONFIG_ROW2_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1], 
                                               y2 = df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2],
                                               ))
        else:
            
            vbar_tbl2_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_2[CONFIG_ROW2_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1]
                                               ))



        vbar_tbl2_tot_col1 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

        vbar_tbl2_tot_col1.title.text = (CONFIG_HOURLY_TBL)

        vbar_tbl2_tot_col1.title.align = "center"

        vbar_tbl2_tot_col1.title.text_color = "yellow" ##1EB913"

        vbar_tbl2_tot_col1.title.text_font_size = "15px"

        vbar_tbl2_tot_col1.title.background_fill_color = "darkblue"

        vbar_tbl2_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl2_source, legend_label = CONFIG_ROW2_COL_Y_AXIS_1)

        vbar_tbl2_tot_col1.legend.location = legend_location

        vbar_tbl2_tot_col1.legend.label_text_font_size = legend_font_size

        if CONFIG_ROW2_COL_Y_AXIS_2:

            varea_tbl2_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_2[CONFIG_ROW2_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1],
                                               y2 = df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_2],
                                               ))
        else:

            varea_tbl2_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_2[CONFIG_ROW2_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_2[CONFIG_ROW2_COL_Y_AXIS_1]))

        vbar_tbl2_tot_col2 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

        vbar_tbl2_tot_col2.title.text = (CONFIG_HOURLY_TBL)

        vbar_tbl2_tot_col2.title.align = "center"

        vbar_tbl2_tot_col2.title.text_color = "yellow" ##1EB913"

        vbar_tbl2_tot_col2.title.text_font_size = "15px"

        vbar_tbl2_tot_col2.title.background_fill_color = "darkblue"

        if CONFIG_ROW2_COL_Y_AXIS_2:

            vbar_tbl2_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl2_stack_source, legend_label = CONFIG_ROW2_COL_Y_AXIS_2)

            vbar_tbl2_tot_col2.legend.location = legend_location

            vbar_tbl2_tot_col2.legend.label_text_font_size = legend_font_size


    ###############################################################################
    #   #######   #     ####    #      ######  ####
    #      #     #  #   #   #   #      #         #
    #      #    ######  ####    #      ###      ####
    #      #    #    #  #   #   #      #           #
    #      #    #    #  ####    #####  ###### #####
    ###############################################################################

    #######################################
    # Visualize Hourly Past  5 Day Data
    #######################################

    if COLS_TBL3:

        line3_tbl3_hourly_7_day = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

        line3_tbl3_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  CONFIG_HOURLY_TBL)

        line3_tbl3_hourly_7_day.title.align = "center"

        line3_tbl3_hourly_7_day.title.text_color = "white"

        line3_tbl3_hourly_7_day.title.text_font_size = "15px"

        line3_tbl3_hourly_7_day.title.background_fill_color = "darkblue"

        if CONFIG_ROW3_COL_Y_AXIS_2:

            line3_tbl3_hourly_7_day.diamond( x=CONFIG_ROW3_COL_X_AXIS, y = CONFIG_ROW3_COL_Y_AXIS_2 , line_width = 2, alpha = 0.5, color=("red"),  source=df_hourly_7_day_tbl_3, legend_label = (CONFIG_ROW3_COL_Y_AXIS_2) )

        line3_tbl3_hourly_7_day.circle( x=CONFIG_ROW3_COL_X_AXIS, y = CONFIG_ROW3_COL_Y_AXIS_1 , line_width = 1.5, alpha = 0.5, color=("blue"), source=df_hourly_7_day_tbl_3, legend_label = (CONFIG_ROW3_COL_Y_AXIS_1))

        line3_tbl3_hourly_7_day.legend.location = legend_location #legend_location

        line3_tbl3_hourly_7_day.legend.label_text_font_size = legend_font_size

        line3_tbl3_hourly_7_day.yaxis[0].formatter = NumeralTickFormatter(format="1,000") 

    #######################################
    # Calculate the BEST_FIT line against _MAX
    #######################################

        if CONFIG_ROW3_COL_Y_AXIS_2:

            int_list = []

            for mydate in df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_X_AXIS]:

                try:

                    int_list.append(date_to_seconds(mydate))

                except:

                    int_list.append(date_to_seconds(str(mydate)[0:19]))

                int_list = sorted(int_list)

            xs = np.array(int_list, dtype = float)

            ys = np.array(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2], dtype = float)

            m, b = best_fit(xs, ys)

            regression_line = [ (m * x) + b  for x in xs]

            XYZ3 = line3_tbl3_hourly_7_day.line(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_X_AXIS], regression_line, color = '#1EB913', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + CONFIG_ROW3_COL_Y_AXIS_2)

            picker3 = ColorPicker(title = 'Best Fit ROW 3')
        
            picker3.js_link('color', XYZ3.glyph, 'line_color')

        #######################################
        # Calculate the OUTLIERS
        #######################################

            my_mean = np.mean(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2])

            my_std  = np.std(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2])

            for count, i in enumerate(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2]):

                try:

                    if my_std != 0:

                        if ( ( i - my_mean ) / my_std ) > outlier_threshold:

                            line3_tbl3_hourly_7_day.circle( x=df_hourly_7_day_tbl_3.iloc[count:count+1,0], y = df_hourly_7_day_tbl_3.iloc[count:count+1,2] , line_width = 7, alpha = 0.5, color=("#CCC000"), legend_label = CONFIG_ROW3_COL_Y_AXIS_2 + " Outlier")

                except Exception as e:

                    log_and_print("#--------------------------------------#")

                    log_and_print("Unable to calculate the outlier_threshold using i: " + str(i) + " my_mean " + str(my_mean) + " my_std " + str(my_std))

                    log_and_print("#--------------------------------------#")
        else:

            int_list = []

            for mydate in df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_X_AXIS]:

                try:

                    int_list.append(date_to_seconds(mydate))

                except:

                    int_list.append(date_to_seconds(str(mydate)[:19]))

                int_list = sorted(int_list)

            xs = np.array(int_list, dtype = float)

            ys = np.array(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1], dtype = float)

            m, b = best_fit(xs, ys)

            regression_line = [ (m * x) + b  for x in xs]

            XYZ3 = line3_tbl3_hourly_7_day.line(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_X_AXIS], regression_line, color = '#1EB913', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + CONFIG_ROW3_COL_Y_AXIS_1)

            picker3 = ColorPicker(title = 'Best Fit ROW 3')
        
            picker3.js_link('color', XYZ3.glyph, 'line_color')
        #######################################
        # Calculate the OUTLIERS
        #######################################

            my_mean = np.mean(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1])

            my_std  = np.std(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1])

            for count, i in enumerate(df_hourly_7_day_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1]):

                try:

                    if my_std != 0:

                        if ( ( i - my_mean ) / my_std ) > outlier_threshold:

                            line3_tbl3_hourly_7_day.circle( x=df_hourly_7_day_tbl_3.iloc[count:count+1,0], y = df_hourly_7_day_tbl_3.iloc[count:count+1,1] , line_width = 7, alpha = 0.5, color=("#CCC000"), legend_label = CONFIG_ROW3_COL_Y_AXIS_1 + " Outlier")

                except Exception as e:

                    log_and_print("#--------------------------------------#")

                    log_and_print("Unable to calculate the outlier_threshold using i: " + str(i) + " my_mean " + str(my_mean) + " my_std " + str(my_std))

                    log_and_print("#--------------------------------------#")

           
        #######################################
        # Visualize Entire Data
        #######################################

        if CONFIG_ROW3_COL_Y_AXIS_2:

            vbar_tbl3_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_3[CONFIG_ROW3_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1], 
                                               y2 = df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2],
                                               ))
        else:
            
            vbar_tbl3_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_3[CONFIG_ROW3_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1]
                                               ))



        vbar_tbl3_tot_col1 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

        vbar_tbl3_tot_col1.title.text = (CONFIG_HOURLY_TBL)

        vbar_tbl3_tot_col1.title.align = "center"

        vbar_tbl3_tot_col1.title.text_color = "yellow" ##1EB913"

        vbar_tbl3_tot_col1.title.text_font_size = "15px"

        vbar_tbl3_tot_col1.title.background_fill_color = "darkblue"

        vbar_tbl3_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl3_source, legend_label = CONFIG_ROW3_COL_Y_AXIS_1)

        vbar_tbl3_tot_col1.legend.location = legend_location

        vbar_tbl3_tot_col1.legend.label_text_font_size = legend_font_size

        if CONFIG_ROW3_COL_Y_AXIS_2:

            varea_tbl3_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_3[CONFIG_ROW3_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1],
                                               y2 = df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_2],
                                               ))
        else:

            varea_tbl3_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_3[CONFIG_ROW3_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_3[CONFIG_ROW3_COL_Y_AXIS_1]))

        vbar_tbl3_tot_col2 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

        vbar_tbl3_tot_col2.title.text = (CONFIG_HOURLY_TBL)

        vbar_tbl3_tot_col2.title.align = "center"

        vbar_tbl3_tot_col2.title.text_color = "yellow" #1EB913"

        vbar_tbl3_tot_col2.title.text_font_size = "15px"

        vbar_tbl3_tot_col2.title.background_fill_color = "darkblue"

        if CONFIG_ROW3_COL_Y_AXIS_2:

            vbar_tbl3_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl3_stack_source, legend_label = CONFIG_ROW3_COL_Y_AXIS_2)

            vbar_tbl3_tot_col2.legend.location = legend_location

            vbar_tbl3_tot_col2.legend.label_text_font_size = legend_font_size


    ###############################################################################
    #   #######   #     ####    #      ######    #
    #      #     #  #   #   #   #      #       # #
    #      #    ######  ####    #      ###    ######
    #      #    #    #  #   #   #      #         #
    #      #    #    #  ####    #####  ######  ####
    ###############################################################################

    #######################################
    # Visualize Hourly Past  5 Day Data
    #######################################

    if COLS_TBL4:

        line4_tbl4_hourly_7_day = figure(plot_width=largeplotWidth, plot_height=largeplotHeight,  x_axis_type="datetime")

        line4_tbl4_hourly_7_day.title.text = (str(N_hourly_days) + " Day " +  CONFIG_HOURLY_TBL)

        line4_tbl4_hourly_7_day.title.align = "center"

        line4_tbl4_hourly_7_day.title.text_color = "white"

        line4_tbl4_hourly_7_day.title.text_font_size = "15px"

        line4_tbl4_hourly_7_day.title.background_fill_color = "darkblue"

        if CONFIG_ROW4_COL_Y_AXIS_2:

            line4_tbl4_hourly_7_day.diamond( x=CONFIG_ROW4_COL_X_AXIS, y = CONFIG_ROW4_COL_Y_AXIS_2 , line_width = 2, alpha = 0.5, color=("red"),  source=df_hourly_7_day_tbl_4, legend_label = (CONFIG_ROW4_COL_Y_AXIS_2) )

        line4_tbl4_hourly_7_day.circle( x=CONFIG_ROW4_COL_X_AXIS, y = CONFIG_ROW4_COL_Y_AXIS_1 , line_width = 1.5, alpha = 0.5, color=("blue"), source=df_hourly_7_day_tbl_4, legend_label = (CONFIG_ROW4_COL_Y_AXIS_1))

        line4_tbl4_hourly_7_day.legend.location = legend_location #legend_location

        line4_tbl4_hourly_7_day.legend.label_text_font_size = legend_font_size

        line4_tbl4_hourly_7_day.yaxis[0].formatter = NumeralTickFormatter(format="1,000") 

    #######################################
    # Calculate the BEST_FIT line against _MAX
    #######################################

        if CONFIG_ROW4_COL_Y_AXIS_2:

            int_list = []

            for mydate in df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_X_AXIS]:

                try:

                    int_list.append(date_to_seconds(mydate))

                except:

                    int_list.append(date_to_seconds(str(mydate)[:19]))

                int_list = sorted(int_list)

            xs = np.array(int_list, dtype = float)

            ys = np.array(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2], dtype = float)

            m, b = best_fit(xs, ys)

            regression_line = [ (m * x) + b  for x in xs]

            XYZ4 = line4_tbl4_hourly_7_day.line(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_X_AXIS], regression_line, color = '#1EB913', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + CONFIG_ROW4_COL_Y_AXIS_2)

            picker4 = ColorPicker(title = 'Best Fit ROW 4')
        
            picker4.js_link('color', XYZ4.glyph, 'line_color')

        #######################################
        # Calculate the OUTLIERS
        #######################################

            my_mean = np.mean(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2])

            my_std  = np.std(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2])

            for count, i in enumerate(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2]):

                try:

                    if my_std != 0:

                        if ( ( i - my_mean ) / my_std ) > outlier_threshold:

                            line4_tbl4_hourly_7_day.circle( x=df_hourly_7_day_tbl_4.iloc[count:count+1,0], y = df_hourly_7_day_tbl_4.iloc[count:count+1,2] , line_width = 7, alpha = 0.5, color=("#CCC000"), legend_label = CONFIG_ROW4_COL_Y_AXIS_2 + " Outlier")

                except Exception as e:

                    log_and_print("#--------------------------------------#")

                    log_and_print("Unable to calculate the outlier_threshold using i: " + str(i) + " my_mean " + str(my_mean) + " my_std " + str(my_std))

                    log_and_print("#--------------------------------------#")

        else:

            int_list = []

            for mydate in df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_X_AXIS]:

                try:

                    int_list.append(date_to_seconds(mydate))

                except:

                    int_list.append(date_to_seconds(str(mydate)[0:19]))

                int_list = sorted(int_list)

            xs = np.array(int_list, dtype = float)

            ys = np.array(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1], dtype = float)

            m, b = best_fit(xs, ys)

            regression_line = [ (m * x) + b  for x in xs]

            XYZ4 = line4_tbl4_hourly_7_day.line(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_X_AXIS], regression_line, color = '#1EB913', alpha = 0.3, line_width = 6, legend_label = 'BEST_FIT of ' + CONFIG_ROW4_COL_Y_AXIS_1)

            picker4 = ColorPicker(title = 'Best Fit ROW 4')
        
            picker4.js_link('color', XYZ4.glyph, 'line_color')

        #######################################
        # Calculate the OUTLIERS
        #######################################

            my_mean = np.mean(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1])

            my_std  = np.std(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1])

            for count, i in enumerate(df_hourly_7_day_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1]):

                try:

                    if my_std != 0:

                        if ( ( i - my_mean ) / my_std ) > outlier_threshold:

                            line4_tbl4_hourly_7_day.circle( x=df_hourly_7_day_tbl_4.iloc[count:count+1,0], y = df_hourly_7_day_tbl_4.iloc[count:count+1,1] , line_width = 7, alpha = 0.5, color=("#CCC000"), legend_label = CONFIG_ROW4_COL_Y_AXIS_1 + " Outlier")

                except Exception as e:

                    log_and_print("#--------------------------------------#")

                    log_and_print("Unable to calculate the outlier_threshold using i: " + str(i) + " my_mean " + str(my_mean) + " my_std " + str(my_std))

                    log_and_print("#--------------------------------------#")

           
        #######################################
        # Visualize Entire Data
        #######################################

        if CONFIG_ROW4_COL_Y_AXIS_2:

            vbar_tbl4_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_4[CONFIG_ROW4_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1], 
                                               y2 = df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2],
                                               ))
        else:
            
            vbar_tbl4_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_4[CONFIG_ROW4_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1]
                                               ))



        vbar_tbl4_tot_col1 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

        vbar_tbl4_tot_col1.title.text = (CONFIG_HOURLY_TBL)

        vbar_tbl4_tot_col1.title.align = "center"

        vbar_tbl4_tot_col1.title.text_color = "yellow" #1EB913"

        vbar_tbl4_tot_col1.title.text_font_size = "15px"

        vbar_tbl4_tot_col1.title.background_fill_color = "darkblue"

        vbar_tbl4_tot_col1.vbar(x = 'x', top = 'y1', color= "blue",  width = 3, source=vbar_tbl4_source, legend_label = CONFIG_ROW4_COL_Y_AXIS_1)

        vbar_tbl4_tot_col1.legend.location = legend_location

        vbar_tbl4_tot_col1.legend.label_text_font_size = legend_font_size

        if CONFIG_ROW4_COL_Y_AXIS_2:

            varea_tbl4_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_4[CONFIG_ROW4_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1],
                                               y2 = df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_2],
                                               ))
        else:

            varea_tbl4_stack_source = ColumnDataSource(data=dict(x = df_hourly_full_tbl_4[CONFIG_ROW4_COL_X_AXIS], 
                                               y1 = df_hourly_full_tbl_4[CONFIG_ROW4_COL_Y_AXIS_1]))

        vbar_tbl4_tot_col2 = figure(plot_width=smallplotWidth, plot_height=smallplotHeight,  x_axis_type="datetime")

        vbar_tbl4_tot_col2.title.text = (CONFIG_HOURLY_TBL)

        vbar_tbl4_tot_col2.title.align = "center"

        vbar_tbl4_tot_col2.title.text_color = "yellow" #1EB913"

        vbar_tbl4_tot_col2.title.text_font_size = "15px"

        vbar_tbl4_tot_col2.title.background_fill_color = "darkblue"

        if CONFIG_ROW4_COL_Y_AXIS_2:

            vbar_tbl4_tot_col2.vbar(x = 'x', top = 'y2', color= "red",  width = 3, source=varea_tbl4_stack_source, legend_label = CONFIG_ROW4_COL_Y_AXIS_2)

            vbar_tbl4_tot_col2.legend.location = legend_location

            vbar_tbl4_tot_col2.legend.label_text_font_size = legend_font_size

    

###################################
# Prepare visualization by grouping charts into rows and columns
###################################

    if CONFIG_ROW1_COL_Y_AXIS_2:

        p_tbl1  = column(vbar_tbl1_tot_col1, vbar_tbl1_tot_col2)

    else:

        p_tbl1  = column(vbar_tbl1_tot_col1)


###################################
# Add Row heading
###################################

    if CONFIG_ROW1_COL_Y_AXIS_2:

        p_ctbl1 = column(Div(text = "<H3 style=\"text-align:center;\">" + CONFIG_ROW1_COL_Y_AXIS_1 + " & " + CONFIG_ROW1_COL_Y_AXIS_2 + "</H3>"), p_tbl1)

    else:

                p_ctbl1 = column(Div(text = "<H3 style=\"text-align:center;\">" + CONFIG_ROW1_COL_Y_AXIS_1 + "</H3>"), p_tbl1)


###################################
# Same again  - Prep by grouping and add row headings
###################################

    if COLS_TBL2: 

        if CONFIG_ROW2_COL_Y_AXIS_2:

            p_tbl2  = column(vbar_tbl2_tot_col1, vbar_tbl2_tot_col2)

            p_ctbl2 = column(Div(text = "<H3 style=\"text-align:center;\">" + CONFIG_ROW2_COL_Y_AXIS_1 + "\t&\t" + CONFIG_ROW2_COL_Y_AXIS_2 + "</H3>"), p_tbl2)

        else:

            p_tbl2  = column(vbar_tbl2_tot_col1)

            p_ctbl2 = column(Div(text = "<H3 style=\"text-align:center;\">" + CONFIG_ROW2_COL_Y_AXIS_1 + "</H3>"), p_tbl2)

    if COLS_TBL3:

        if CONFIG_ROW3_COL_Y_AXIS_2:

            p_tbl3  = column(vbar_tbl3_tot_col1, vbar_tbl3_tot_col2)

            p_ctbl3 = column(Div(text = "<H3 style=\"text-align:center;\">" + CONFIG_ROW3_COL_Y_AXIS_1 + "\t&\t" + CONFIG_ROW3_COL_Y_AXIS_2 + "</H3>"), p_tbl3)

        else:

            p_tbl3  = column(vbar_tbl3_tot_col1)

            p_ctbl3 = column(Div(text = "<H3 style=\"text-align:center;\">" + CONFIG_ROW3_COL_Y_AXIS_1 + "</H3>"), p_tbl3)

    if COLS_TBL4:

        if CONFIG_ROW4_COL_Y_AXIS_2:

            p_tbl4 = column(vbar_tbl4_tot_col1, vbar_tbl4_tot_col2)

            p_ctbl4 = column(Div(text = "<H3 style=\"text-align:center;\">" + CONFIG_ROW4_COL_Y_AXIS_1 + "\t&\t" + CONFIG_ROW4_COL_Y_AXIS_2 + "</H3>"), p_tbl4)

        else:

            p_tbl4 = column(vbar_tbl4_tot_col1)

            p_ctbl4 = column(Div(text = "<H3 style=\"text-align:center;\">" + CONFIG_ROW4_COL_Y_AXIS_1 + "</H3>"), p_tbl4)


    MEM_OBJECT_GRIDPLOT = gridplot([[p_ctbl1, 
        line1_tbl1_hourly_7_day]], toolbar_location='right')

    if COLS_TBL2:

        MEM_OBJECT_GRIDPLOT = gridplot([[p_ctbl1, 
            line1_tbl1_hourly_7_day], 
            [p_ctbl2, 
            line2_tbl2_hourly_7_day]], toolbar_location='right')

    if COLS_TBL3:

        MEM_OBJECT_GRIDPLOT = gridplot([[p_ctbl1, 
            line1_tbl1_hourly_7_day], 
            [p_ctbl2, 
            line2_tbl2_hourly_7_day],
            [p_ctbl3,
            line3_tbl3_hourly_7_day]], toolbar_location='right')

    if COLS_TBL4:

        MEM_OBJECT_GRIDPLOT = gridplot([[p_ctbl1, 
            line1_tbl1_hourly_7_day], 
            [p_ctbl2, 
            line2_tbl2_hourly_7_day],
            [p_ctbl3,
            line3_tbl3_hourly_7_day],
            [p_ctbl4,
            line4_tbl4_hourly_7_day]], toolbar_location='right')



    line1_tbl1_hourly_7_day.add_tools(HoverTool(tooltips = [
                                                (CONFIG_ROW1_COL_X_AXIS, "$x{%Y-%m-%d  hour:%H}")
                                               ,("value","$y" )
                                        ],
                                        formatters = {
                                                      "$x" :'datetime'
                                                     ,"$y" :'printf'
                                                      }
                                                )
                                       )
    if COLS_TBL2:
 
        line2_tbl2_hourly_7_day.add_tools(HoverTool(tooltips = [
                                                (CONFIG_ROW2_COL_X_AXIS, "$x{%Y-%m-%d  hour:%H}")
                                               ,("value","$y" )
                                        ],
                                        formatters = {
                                                      "$x" :'datetime'
                                                     ,"$y" :'printf'
                                                      }
                                                )
                                       )
    if COLS_TBL3:

         line3_tbl3_hourly_7_day.add_tools(HoverTool(tooltips = [
                                                (CONFIG_ROW3_COL_X_AXIS, "$x{%Y-%m-%d  hour:%H}")
                                               ,("value","$y" )
                                        ],
                                        formatters = {
                                                      "$x" :'datetime'
                                                     ,"$y" :'printf'
                                                      }
                                                )
                                       )

    if COLS_TBL4:


        line4_tbl4_hourly_7_day.add_tools(HoverTool(tooltips = [
                                                (CONFIG_ROW4_COL_X_AXIS, "$x{%Y-%m-%d  hour:%H}")
                                               ,("value","$y" )
                                        ],
                                        formatters = {
                                                      "$x" :'datetime'
                                                     ,"$y" :'printf'
                                                      }
                                                )
                                       )
    if COLS_TBL4:
        
        show(column(Div(text = "<H1 style=\"text-align:center;border:1px solid red;color:yellow;background-color: darkblue;\">" + CONFIG_HOURLY_TBL + "</H1>"), MEM_OBJECT_GRIDPLOT,picker, picker2, picker3, picker4))


    elif COLS_TBL3:

        show(column(Div(text = "<H1 style=\"text-align:center;border:1px solid red;color:yellow;background-color: darkblue;\">" + CONFIG_HOURLY_TBL + "</H1>"), MEM_OBJECT_GRIDPLOT,picker, picker2, picker3))

    elif COLS_TBL2:

        show(column(Div(text = "<H1 style=\"text-align:center;border:1px solid red;color:yellow;background-color: darkblue;\">" + CONFIG_HOURLY_TBL + "</H1>"), MEM_OBJECT_GRIDPLOT,picker, picker2))

    else:

        show(column(Div(text = "<H1 style=\"text-align:center;border:1px solid red;color:yellow;background-color: darkblue;\">" + CONFIG_HOURLY_TBL + "</H1>"), MEM_OBJECT_GRIDPLOT,picker))

    
    
    log_and_print("#--------------------------------------#")

    log_and_print("Exit Stats")
    
    log_and_print("Config section:\t " + config_section)

    log_and_print("with CONFIG_HOURLY_TBL:\t " + CONFIG_HOURLY_TBL)


    log_and_print("#--------------------------------------#")

    log_and_print("")

    log_and_print("#--------------------------------------#")

    log_and_print("successfully exited after processing " + config_in)

    log_and_print("#--------------------------------------#")

    if os.path.exists(output_title):

        print("HIT ON " + output_title)

    else:

        print("FAIL ON " + output_title)

    
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window_size=1368x768')
    driver = webdriver.Chrome(executable_path="C:\\Users\\joas\\Desktop\\Exasol\\IGAPA3\\chromedriver.exe", chrome_options=options)
    
    image_file = (str(save_dir + "\\" + in_ticket + "\\" + config_section + '_' + str(now) +  '.html'))
    p_tbl1
    save_path = (str(save_dir + "\\" + in_ticket + "\\" + config_section + '_' + str(now)))
    save_name = (config_section + '_' + str(now) +  '.png')

    #img1 = Image.open(StringIO(base64.decodestring(driver.get_screenshot_as_base64(image_file))))

    #print (img1)

    driver.set_window_size(1366, 2500)
    driver.get(image_file)
    driver.save_screenshot(save_name)
    driver.quit()

    if p_ctbl1:

        if CONFIG_ROW1_COL_Y_AXIS_2:

            export_png(p_ctbl1, filename = config_section + '_' + str(now) + "_" + CONFIG_ROW1_COL_Y_AXIS_1 + " & " + CONFIG_ROW1_COL_Y_AXIS_2 + ".png")

        elif CONFIG_ROW1_COL_Y_AXIS_1:

                export_png(p_ctbl1, filename = config_section + '_' + str(now) + "_" + CONFIG_ROW1_COL_Y_AXIS_1 + ".png")

        else:

                export_png(p_ctbl1, filename = config_section + '_' + str(now) +   + ".png")

    try:

        p_ctbl2

    except:

        pass

    else:

        if CONFIG_ROW2_COL_Y_AXIS_2:

            export_png(p_ctbl2, filename = config_section + '_' + str(now) + "_" + CONFIG_ROW2_COL_Y_AXIS_1 + " & " + CONFIG_ROW2_COL_Y_AXIS_2 + ".png")

        elif CONFIG_ROW2_COL_Y_AXIS_1:

            export_png(p_ctbl2, filename = config_section + '_' + str(now) + "_" + CONFIG_ROW2_COL_Y_AXIS_1 + " & "  + ".png")

        else:

            export_png(p_ctbl2, filename = config_section + '_' + str(now) +   ".png")

        try:

            p_ctbl3

        except:

            pass

        else:

            if CONFIG_ROW3_COL_Y_AXIS_2:

                export_png(p_ctbl3, filename = config_section + '_' + str(now) + "_" + CONFIG_ROW3_COL_Y_AXIS_1 + " & " + CONFIG_ROW3_COL_Y_AXIS_2 + ".png")

            elif CONFIG_ROW3_COL_Y_AXIS_1:

                export_png(p_ctbl3, filename = config_section + '_' + str(now) + "_" + CONFIG_ROW3_COL_Y_AXIS_1 + ".png")

            else:

                export_png(p_ctbl3, filename = config_section + '_' + str(now) + ".png")

        
        try:

            p_ctbl4

        except:

            pass

        else:

            if CONFIG_ROW4_COL_Y_AXIS_2:

                export_png(p_ctbl4, filename = config_section + '_' + str(now) + "_" + CONFIG_ROW4_COL_Y_AXIS_1 + " & " + CONFIG_ROW4_COL_Y_AXIS_2 + ".png")

            elif CONFIG_ROW4_COL_Y_AXIS_1:

                export_png(p_ctbl4, filename = config_section + '_' + str(now) + "_" + CONFIG_ROW4_COL_Y_AXIS_1 +  ".png")

            else:

                export_png(p_ctbl4, filename = config_section + '_' + str(now) + "_" +  ".png")



    # img = Image.open(save_path, save_name)
    # box = (1,1,1000,1000)
    # area = img.crop(box)
    # area.save('cropped_image_' + config_section + '_' + str(now), '.png')
    

# #######################################
# # Stubbed Plug-in
# #######################################
# p = Predictor(df_hourly_full_tbl_1[COLS_TBL1])

# rnn_prediction = p.forecast(df_hourly_full_tbl_1[COLS_TBL1])

# print("rnn_prediction:\n" + str(rnn_prediction))
