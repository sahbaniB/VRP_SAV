#importing the module
import threading 
import logging 

import sys
sys.path.insert(0, 'C:/VRP/Projet_vrp')


#now we will Create and configure logger 
logging.basicConfig(filename="C:/VRP/Projet_vrp/logfile.log", 
					format='%(asctime)s %(message)s', 
					filemode='w',
                    level=logging.INFO) 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

class WriteLogMessage():
    def starting_program():
        pass

    def passenger_request():
        pass

    def SAV_propositions():
        pass


