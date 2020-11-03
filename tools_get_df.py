import os

from tools_logger import *

try:

    import pandas as pd

except:

    os.system('pip install pandas')

    import pandas as pd

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
	from pyexasol import ExaConnection

except:

	os.system('pip install pyexasol')

	from pyexasol import ExaConnection

try:
    import ntpath

except:

    os.system('pip install ntpath')

    import ntpath



######################################
class GetDF:
#######################################
#-------------------------------------#
    def __init__(self, myconfig = 'DB_SIZE', which_config = 'config_reports.ini'):
#-------------------------------------#

        my_pgm = ntpath.basename(os.path.basename(__file__))

        logging_filename = ("./logs/" + my_pgm[0:(my_pgm.index('.py'))] + '.log')

        logging.basicConfig(filename = logging_filename, level=logging.INFO, filemode = 'a', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')
   
        self.myconfig = myconfig

        self.which_config = which_config

        log_and_print("#--------------------------------------#")

        log_and_print("# Entering " + os.path.basename(__file__))

        log_and_print("#--------------------------------------#")

        log_and_print("# " + os.path.basename(__file__) + " Class GetDF received section heading: " + self.myconfig + " using this config file: " + self.which_config)

        self.sections_df_hourly = [0]

        self.sections_df_daily = [0]

        self.sections_list = []
#-------------------------------------#
    def __repr__(self):
#-------------------------------------#

        return(f'{self.__class__.__name__}('
               
               f'{self.myconfig!r}, {self.which_config!r})')

    

#-------------------------------------#
    def run(self, path = '.', which_config = 'config_reports.ini'):
#-------------------------------------#
        config = configparser.ConfigParser()

        X = config.read(path + '/' + which_config)

        for section in config.sections():

            self.cols_list = []

            for key, item in config[section].items():

                self.cols_list.append(item)

            self.my_tbl_hourly = self.cols_list.pop(0)

            self.sections_list.append(self.my_tbl_hourly)

            self.my_tbl_daily  = self.cols_list.pop(0)

            my_cols = sorted(list(set(self.cols_list)))

            con = ExaConnection(dsn="192.168.1.158", user='sys', password='exasol')

            df =  con.export_to_pandas(self.my_tbl_hourly, export_params = {'with_column_names':True, 'columns':my_cols})

            print(df.info())

            self.sections_df_hourly.append(df)

        return self.sections_list, self.sections_df_hourly

#######################################
# FUNCTIONS
#######################################
#-------------------------------------#
def log_and_print(msg = ''):
#-------------------------------------#

    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)



#######################################
# MAIN LOGIC
#######################################

if __name__ == '__main__':

    a = GetDF('DB_SIZE', 'config_reports.ini')

    sections_list, sections_df_hourly = a.run()

    # for section in sections_list:

    #     print(section)

    for section_df in sections_df_hourly:

	    log_and_print(section_df.columns())
