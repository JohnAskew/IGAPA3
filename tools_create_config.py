'''
name: tools_create_config.py
desc: Read user sql-generated CSV
      and create config file based
      on the CSV Columns
usage: None, this is called.
'''
import os

import sys

try:

	import configparser

except:

	os.system('pip install configparser')

	import configparser


#######################################
# FUNCTIONS
#######################################


#######################################
# MAIN LOGIC
#######################################

dummy = ''

count = 0

x_axis = ""

x_axis2 = ""

x_axis3 = ""

x_axis4 = ""

y1 = ""

y2 = ""

y3 = ""

y4 = ""

y5 = ""

y6 = ""

y7 = ""

y8 = ""

if len(sys.argv) == 1:

	myPath = './demodb.exasol.com'

	saveFile = ('hdd_write.sql.csv')

else:

	myPath = sys.argv[1]

	saveFile = sys.argv[2]

configRec = saveFile[0:(saveFile.index('.csv'))]

configFile = configRec + '.ini'

with open((myPath + "/" + saveFile), 'r') as in_csv:

    worklist  = (in_csv.readline()[1:])

    x_axis  = worklist[:worklist.index(',')]

    y1 = worklist[(worklist.index(',') + 1):].strip()

    for i in y1:

    	if i == ',':

    		count +=1

    if count == 7:

        y1, y2, y3, y4, y5, y6, y7, y8 = y1.split(',')

        x_axis4 = x_axis

        x_axis3 = x_axis

        x_axis2 = x_axis

    elif count == 6:

        y1, y2, y3, y4, y5, y6, y7 = y1.split(',')

        x_axis4 = x_axis

        x_axis3 = x_axis

        x_axis2 = x_axis


    elif count == 5:

    	y1, y2, y3, y4, y5, y6 = y1.split(',')

    	x_axis3 = x_axis

    	x_axis2 = x_axis

    elif count == 4:

    	y1, y2, y3, y4, y5 = y1.split(',')

    	x_axis3 = x_axis

    	x_axis2 = x_axis

    elif count == 3:

    	y1, y2, y3, y4 = y1.split(',')

    	x_axis2 = x_axis

    if count == 2:

    	y1, y2, y3 = y1.split(',')

    	x_axis2 = x_axis

    elif y1.find(',') != -1:

        y1, y2 = y1.split(',')

config = configparser.ConfigParser()

config.optionxform=str

config[configRec] = {}

config[configRec]['CONFIG_HOURLY_TBL'] = configRec #saveFile

config[configRec]['CONFIG_ROW1_COL_X_AXIS'] = x_axis

config[configRec]['CONFIG_ROW1_COL_Y_AXIS_1'] = y1

config[configRec]['CONFIG_ROW1_COL_Y_AXIS_2'] = y2

config[configRec]['CONFIG_ROW2_COL_X_AXIS']   = x_axis2

config[configRec]['CONFIG_ROW2_COL_Y_AXIS_1'] = y3

config[configRec]['CONFIG_ROW2_COL_Y_AXIS_2'] = y4

config[configRec]['CONFIG_ROW3_COL_X_AXIS']   = x_axis3

config[configRec]['CONFIG_ROW3_COL_Y_AXIS_1'] = y5

config[configRec]['CONFIG_ROW3_COL_Y_AXIS_2'] = y6

config[configRec]['CONFIG_ROW4_COL_X_AXIS']   = x_axis4

config[configRec]['CONFIG_ROW4_COL_Y_AXIS_1'] = y7

config[configRec]['CONFIG_ROW4_COL_Y_AXIS_2'] = y8

with open((myPath + '/' + configFile), 'w') as configfile:

	config.write(configfile)

sys.exit(0)