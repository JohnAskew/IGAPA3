import os, sys

try:

    import configparser

except:

    os.system('pip install configparser')

    import configparser

try:

    import hashlib

except:

    os.system('pip install hashlib')

    import hashlib

try:

    import getpass

except:

    os.system('pip install getpass')

    import getpass

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

now = dt.today().strftime('%Y-%m-%d-%H:%M:%S')

from tools_logger import *

from igapa2_linkage import *

try:
    import ntpath

except:

    os.system('pip install ntpath')

    import ntpath




#######################################
class ParseConfig:
#######################################
#-------------------------------------#
    def __init__(self, myconfig = 'USAGE', which_config = 'config_report4.ini'):
#-------------------------------------#

        my_pgm = ntpath.basename(os.path.basename(__file__))

        self.myconfig = myconfig

        self.which_config = which_config

        self.logging_filename = ("./logs/" + my_pgm[0:(my_pgm.index('.py'))] + '.log')

        logging.basicConfig(filename = self.logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

        log_and_print("#--------------------------------------#")

        log_and_print("# Entering " + os.path.basename(__file__))

        log_and_print("#--------------------------------------#")

        log_and_print("Class ParseConfig received section heading: " + self.myconfig + " using this config file: " + self.which_config)

#-------------------------------------#
    def __repr__(self):
#-------------------------------------#

        return(f'{self.__class__.__name__}('
               
               f'{self.myconfig!r}, {self.which_config!r})')

#-------------------------------------#
    def read_config_admin_admin(self, path = '.', config_admin = 'config_admin.ini'):
#-------------------------------------#

        self.path = path

        self.config_admin = config_admin

        log_and_print("#-------------------------------------#")

        log_and_print("# Entering: read_config_admin_admin with path: " + self.path + " using this config file: " + self.config_admin)

        log_and_print("#-------------------------------------#")

        config = configparser.ConfigParser()

        x = (self.path + '/' + self.config_admin)

        y = config.read(x)

        if len(y) == 0:

            log_and_print("#######################################")

            log_and_print("# FATAL: " + os.path.basename(__file__))

            log_and_print("# config_admin.ini not found or is not readable.")

            log_and_print("# This program was looking for:", x)

            log_and_print("#")

            log_and_print("# Ensure config_admin.ini exists in this directory: " + os.getcwd())

            log_and_print("# ---> Does config_admin.ini exist?")

            log_and_print("# ---> Is config_admin.ini a readable file?")

            log_and_print("# Here is the output from attempted config file read: " +  y)

            log_and_print("# Aborting with no action taken.")

            log_and_print("#######################################")

            print("#######################################")

            print("# FATAL:", os.path.basename(__file__))

            print("# config_admin.ini not found or is not readable.")

            print("# This program was looking for:", x)

            print("#")

            print("# Ensure config_admin.ini exists in this directory:", os.getcwd())

            print("# ---> Does config_admin.ini exist?")

            print("# ---> Is config_admin.ini a readable file?")

            print("# Here is the output from attempted config file read:", y)

            print("# Aborting with no action taken.")

            print("#######################################")

            sys.exit(0)
        
        try:

            user   = config.get('ADMIN', 'user')

            passwd = config.get('ADMIN', 'passwd')

            if len(user) == 0 or len(passwd) == 0:

                user = input('Enter user name for JIRA access')

                print("You are logging in as user:", user)

                passwd  = getpass.getpass(prompt='Enter password, it will NOT be displayed ')


        except Exception as e:

            log_and_print("#######################################")

            log_and_print("# ERROR:", os.path.basename(__file__) + " config_admin.ini " + self.config_admin + " missing login credentials")

            log_and_print("#######################################")

            log_and_print(e, exc_info = True)

            print("#######################################")

            print("# ERROR:", os.path.basename(__file__), "config_admin.ini", self.config_admin, "missing login credentials")

            print("#######################################")

            user = input('Enter user name for JIRA access')

            print("You are logging in as user:", user)

            log_and_print("# " + os.path.basename(__file__) + " Interactively received Jira user: " + user)

            passwd  = getpass.getpass(prompt='Enter password, it will NOT be displayed ')

        m = hashlib.sha256()

        b = bytes(passwd, 'utf-8')

        m.update(b)

        log_and_print(" is successfully returning user " + user + ' and encrypted passwd ' + str(m.hexdigest()))

        return (user, passwd)

#-------------------------------------#
    def read_config_admin_layout(self, path = '.', config_admin = 'config_admin.ini'):
#-------------------------------------#

        self.path = path

        self.config_admin = config_admin

        config = configparser.ConfigParser()

        x = (self.path + '/' + self.config_admin)

        y = config.read(x)

        if len(y) == 0:

            log_and_print("#######################################")

            log_and_print("# FATAL: " + os.path.basename(__file__))

            log_and_print("# config_admin.ini not found or is not readable.")

            log_and_print("# This program was looking for: " + x)

            log_and_print("#")

            log_and_print("# Ensure config_admin.ini exists in this directory: " + os.getcwd())

            log_and_print("# ---> Does config_admin.ini exist?")

            log_and_print("# ---> Is config_admin.ini a readable file?")

            log_and_print("# Here is the output from attempted config file read: " +  y)

            log_and_print("# Aborting with no action taken.")

            log_and_print("#######################################")

            sys.exit(12)
        
        try:

            legend_font_size   = config.get('MASTER-LAYOUT', 'legend_font_size')

            legend_location    = config.get('MASTER-LAYOUT', 'legend_location')

            plotWidth          = config.get('MASTER-LAYOUT', 'plotWidth')

            plotHeight         = config.get('MASTER-LAYOUT', 'plotHeight')

            smallplotWidth     = config.get('MASTER-LAYOUT', 'smallplotWidth')

            smallplotHeight    = config.get('MASTER-LAYOUT', 'smallplotHeight')

            largeplotWidth     = config.get('MASTER-LAYOUT', 'largeplotWidth')

            largeplotHeight    = config.get('MASTER-LAYOUT', 'largeplotHeight')
   
        except Exception as e:

            log_and_print("#######################################")

            log_and_print("# " + os.path.basename(__file__) + " config_admin.ini " + self.config_admin + "")

            log_and_print(e, exc_info = True)

            log_and_print("#######################################")

            pass_fail = False

            log_and_print(str(e))

            sys.exit(12)

        return (legend_font_size, legend_location, plotWidth, plotHeight, smallplotWidth, smallplotHeight, largeplotWidth, largeplotHeight)

#-------------------------------------#
    def read_config_admin_reporting(self, path = '.', config_admin = 'config_admin.ini'):
#-------------------------------------#

        self.path = path

        self.config_admin = config_admin

        config = configparser.ConfigParser()

        x = (self.path + '/' + self.config_admin)

        y = config.read(x)

        if len(y) == 0:

            log_and_print("#######################################")

            log_and_print("# FATAL: " + os.path.basename(__file__))

            log_and_print("# config_admin.ini not found or is not readable.")

            log_and_print("# This program was looking for: " + x)

            log_and_print("#")

            log_and_print("# Ensure config_admin.ini exists in this directory: " + os.getcwd())

            log_and_print("# ---> Does config_admin.ini exist?")

            log_and_print("# ---> Is config_admin.ini a readable file?")

            log_and_print("# Here is the output from attempted config file read: " +  y)

            log_and_print("# Aborting with no action taken.")

            log_and_print("#######################################")

            sys.exit(12)
        
        try:

            log_level          = config.get('REPORTING', 'log_level')

            outlier_threshold  = config.get('REPORTING', 'outlier_threshold')

            reports_hourly = config.get('REPORTING', 'reports_hourly')

            reports_daily  = config.get('REPORTING', 'reports_daily')

            return log_level, outlier_threshold, reports_hourly, reports_daily

               
        except Exception as e:

            log_and_print("#######################################")

            log_and_print("# " + os.path.basename(__file__) + " config_admin.ini " + self.config_admin + "")

            log_and_print(e, exc_info = True)

            log_and_print("#######################################")

            print("#######################################")

            print("# ERROR:", os.path.basename(__file__), "config_admin.ini", self.config_admin, "")

            pass_fail = False

            print("#######################################")

            print(e)

            sys.exit(0)

#-------------------------------------#
    def read_config_sections(self, path = '.'):
#-------------------------------------#

        self.path = path

        config = configparser.ConfigParser()

        x = (self.path + '\\' + self.which_config)

        y = config.read(x)

        if len(y) == 0:

            log_and_print("#######################################")

            log_and_print("# " + os.path.basename(__file__))

            log_and_print("# config file " + self.which_config + " not found or is not readable.")

            log_and_print("# This program was looking for config file: " + x)

            log_and_print("# Ensure ini files exists in this directory: " +  save_dir)

            log_and_print("# ---> Does " +  self.which_config + " exist?")

            log_and_print("# ---> Is " +  self.which_config + " a readable file?")

            log_and_print("# Aborting with no action taken.")

            log_and_print("#######################################")

            sys.exit(-1)


        try:

            z = config.sections()

            for item in z:

                log_and_print("found " + self.which_config + " with these sections: " +  item)

            return z

        except Exception as e:

            log_and_print("#######################################")

            log_and_print("# " + os.path.basename(__file__))

            log_and_print("#Unable to parse config file " + self.which_config)

            log_and_print("# Aborting with no action taken")

            log_and_print(e, exc_info = True)

            log_and_print("#######################################")

            log_and_print(str(e))

            sys.exit(0)

        

#-------------------------------------#
    def run(self, path = '.'):
#-------------------------------------#

        self.path = path

        myConfig = self.myconfig

        pass_fail = True
        
        config = configparser.ConfigParser()

        q = (self.path + '\\' + self.which_config)

        try:

            config.read(q)

        except Exception as e:

            log_and_print("#######################################")

            log_and_print("FATAL: " + os.path.basename(__file__))

            log_and_print("# Unable to config.read " + self.which_config)

            log_and_print("# in section run with config.read: " +  config.read(self.which_config))

            log_and_print("# Aborting with no action taken.")

            log_and_print(e, exc_info = True)

            log_and_print("#######################################")

            log_and_print(str(e))

            sys.exit(12)

        for item in ['CONFIG_HOURLY_TBL','CONFIG_ROW1_COL_X_AXIS','CONFIG_ROW1_COL_Y_AXIS_1','CONFIG_ROW1_COL_Y_AXIS_2','CONFIG_ROW2_COL_X_AXIS','CONFIG_ROW2_COL_Y_AXIS_1','CONFIG_ROW2_COL_Y_AXIS_2','CONFIG_ROW3_COL_X_AXIS','CONFIG_ROW3_COL_Y_AXIS_1','CONFIG_ROW3_COL_Y_AXIS_2','CONFIG_ROW4_COL_X_AXIS','CONFIG_ROW4_COL_Y_AXIS_1','CONFIG_ROW4_COL_Y_AXIS_2']:

            try:

                config.get(myConfig, item)

            except Exception as e:

                log_and_print("# " + os.path.basename(__file__) + " config:  " + self.myConfig + " missing -->\t" + item)

                log_and_print(str(e))

                pass_fail = False

        log_and_print()

        assert(pass_fail)

            #quit(0)

        log_and_print("#--------------------------------------#")
                  
        log_and_print(" successfully exit.")

        log_and_print("#--------------------------------------#")

        return config[myConfig]['CONFIG_HOURLY_TBL'] \
        ,config[myConfig]['CONFIG_ROW1_COL_X_AXIS']       \
        ,config[myConfig]['CONFIG_ROW1_COL_Y_AXIS_1']     \
        ,config[myConfig]['CONFIG_ROW1_COL_Y_AXIS_2']     \
        ,config[myConfig]['CONFIG_ROW2_COL_X_AXIS']       \
        ,config[myConfig]['CONFIG_ROW2_COL_Y_AXIS_1']     \
        ,config[myConfig]['CONFIG_ROW2_COL_Y_AXIS_2']     \
        ,config[myConfig]['CONFIG_ROW3_COL_X_AXIS']       \
        ,config[myConfig]['CONFIG_ROW3_COL_Y_AXIS_1']     \
        ,config[myConfig]['CONFIG_ROW3_COL_Y_AXIS_2']     \
        ,config[myConfig]['CONFIG_ROW4_COL_X_AXIS']       \
        ,config[myConfig]['CONFIG_ROW4_COL_Y_AXIS_1']     \
        ,config[myConfig]['CONFIG_ROW4_COL_Y_AXIS_2']     

#######################################
# FUNCTIONS
#######################################
#--------------------------------------
def log_and_print(msg = ""):

    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)

#######################################
# M A I N   L O G I C
#######################################



if __name__ == '__main__':

    log_and_print("--> is accessing ParseConfig with ParseConfig('USAGE', 'config_reports.ini'")

    a = ParseConfig('USAGE', 'config_reports.ini')

    log_and_print(" __repr__ on a: " + repr(a))

    user, passwd  = a.read_config_admin_admin('.', 'config_admin.ini')

    log_and_print("config_admin.ini has section ADMIN user: " + user +  " password: <secret>")

    legend_font_size, legend_location, plotWidth, plotHeight, smallplotWidth, smallplotHeight, largeplotWidth, largeplotHeight = a.read_config_admin_layout('.', 'config_admin.ini')

    log_and_print("config_admin.ini has section MASTER-LAYOUT with " + legend_font_size 
                                                                     + " " + legend_location
                                                                     + " " + plotWidth
                                                                     + " " + plotHeight
                                                                     + " " + smallplotWidth 
                                                                     + " " + smallplotHeight
                                                                     + " " + largeplotWidth 
                                                                     + " " + largeplotHeight)

    log_level, outlier_threshold, reports_hourly, reports_daily = a.read_config_admin_reporting('.', 'config_admin.ini')

    log_and_print("config_admin.ini has section REPORTING with " + str(log_level) + 
                                    " AND outlier_threshold of " + outlier_threshold +
                                    " reports_hourly "       + reports_hourly + 
                                    " reports_daily  "       + reports_daily)


    a.read_config_sections('.')

    CONFIG_ROW1_HOURLY_TBL, CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2, CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2, CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2, CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2 = a.run('.')

    print("==> Returning:", CONFIG_ROW1_HOURLY_TBL, CONFIG_ROW1_COL_X_AXIS, CONFIG_ROW1_COL_Y_AXIS_1, CONFIG_ROW1_COL_Y_AXIS_2, CONFIG_ROW2_COL_X_AXIS, CONFIG_ROW2_COL_Y_AXIS_1, CONFIG_ROW2_COL_Y_AXIS_2, CONFIG_ROW3_COL_X_AXIS, CONFIG_ROW3_COL_Y_AXIS_1, CONFIG_ROW3_COL_Y_AXIS_2, CONFIG_ROW4_COL_X_AXIS, CONFIG_ROW4_COL_Y_AXIS_1, CONFIG_ROW4_COL_Y_AXIS_2)

    log_and_print("#--------------------------------------#")
    
    log_and_print(" successfully exit.")

    log_and_print("#--------------------------------------#")






