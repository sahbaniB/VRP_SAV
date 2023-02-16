#importing the module
import threading 
import logging 

import sys
sys.path.insert(0, 'C:/VRP/Projet_vrp')


#now we will Create and configure logger 
logging.basicConfig(filename="C:/GIT_VRP/VRP_SAV/Projet_vrp/logfile.log", 
					format='%(asctime)s %(message)s', 
					filemode='w',
                    level=logging.INFO) 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

class WriteLogMessage():
    @staticmethod
    def starting_program(numberofsav):
        logging.info('############# starting the programme #####################')
        logging.info("In this context we have deployed {} SAVs".format(numberofsav))
        logging.info("This is the departure of the program, all the SAV vehicules are at thier associated warehouse")
    
    @staticmethod
    def reportWareHouse(warehouses):
        logging.info('##################### This part is for repporting the Warehouses availables #####################')
        for warehouse in warehouses:
            logging.info("len of ware house is")
            logging.info("WareHouse ID {} at the position {}".format(warehouse.warehouse_ID , warehouse.warehouse_position))
        

    @staticmethod
    def passenger_request(ag):
        logging.info("ag id = {}".format(ag.passenger_ID))


    @staticmethod
    def SAV_propositions():
        pass


