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
    ### This part is dedicated to all log messages of Controller class
    @staticmethod
    def starting_program(numberofsav):
        logging.info('##################### starting the program #####################')
        logging.info("This is the departure of the program, all the SAV vehicules are at thier associated warehouse")
    
    ### This part is dedicated to all log messages of WareHouse class
    @staticmethod
    def defineWareHouse(warehouses):
        logging.info('##################### This part is define the Warehouses availables #####################')
        for warehouse in warehouses:
            logging.info("len of ware house is")
            logging.info("WareHouse ID {} at the position {}".format(warehouse.warehouse_ID , warehouse.warehouse_position))
    
   ### This part is dedicated to all log messages of SAV class
    @staticmethod
    def defineSAV(numberofsav):
        logging.info('##################### This part is define the Shared Autonomous Vehicules (SAVs) availables #####################')
        logging.info("In this context we have deployed {} SAVs".format(numberofsav))

    @staticmethod
    def SAV_propositions():
        pass
    
        
    ### This part is dedicated to all log messages of Passenger class
    @staticmethod
    def passenger_request_message(passenger):
        logging.info("The passenger {} has pickup request with a waiting time {}".format(passenger.passenger_ID, passenger.waitingtime))
        logging.info("The passenger {} with a pickup position ({}, {}) and destination position \
            ({},{})".format(passenger.passenger_ID,passenger.x_passenger_pickupposition, passenger.y_passenger_pickupposition, \
                passenger.x_passenger_destinationposition, passenger.y_passenger_destinationposition))

    @staticmethod
    def passenger_selection_of_SAV(passenger,bestSAV,bestprice):
        logging.info("The passenger {} has chosen the SAV {}, the price of the trip is {}"\
            .format(passenger.passenger_ID, bestSAV.SAV_ID, bestprice))

    ### This part is dedicated to all log messages of RestAPI class
    @staticmethod
    def exception_message():
        logging.info("The coordinations of pickupp/destination is not find")





