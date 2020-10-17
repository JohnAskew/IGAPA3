import os

import sys

try:

    import pandas as pd

except:

    os.system('pip install pandas')

    import pandas as pd

try:

    import logging

except:

    os.system('pip install logging')

    import logging

#######################################
# C L A S S 
#######################################
class Predictor():

	def __init__(self, in_df):

		self.in_df = in_df

		my_pgm = os.path.basename(__file__)

		self.logging_filename = my_pgm[0:(my_pgm.index('.py'))] + '.log'

		logging.basicConfig(filename = self.logging_filename, level=logging.INFO, filemode = 'w', format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

		log_and_print("#--------------------------------------#")

		log_and_print("# Entering " + os.path.basename(__file__))

		log_and_print("#--------------------------------------#")

		log_and_print("Class Predictor Instatiated")


#######################################
# FUNCTIONS
#######################################
#--------------------------------------
def log_and_print(msg = ""):

    print("# " + os.path.basename(__file__) + ": " + msg)

    logging.info("# " + os.path.basename(__file__) + ": " + msg)