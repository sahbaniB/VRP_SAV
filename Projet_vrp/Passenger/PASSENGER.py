import logging
import threading
from time import sleep
import pandas as pd
#from Autonomous_vehicle.SAV import SharedAutonomousVehicle
import sys
sys.path.insert(0, 'C:/git_vrp/VRP_SAV')


#importing the module 
import logging 

#now we will Create and configure logger 
logging.basicConfig(filename="logfile.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

from Write_logfile import WriteLogMessage

class Passenger(threading.Thread):
    def __init__(self, passenger_ID, x_passenger_pickupposition=[], y_passenger_pickupposition=[], x_passenger_destinationposition=[], \
        y_passenger_destinationposition=[], waitingtime=3):
        threading.Thread.__init__(self)
        self.passenger_ID = passenger_ID
        self.x_passenger_pickupposition = x_passenger_pickupposition
        self.y_passenger_pickupposition = y_passenger_pickupposition
        self.x_passenger_destinationposition = x_passenger_destinationposition
        self.y_passenger_destinationposition = y_passenger_destinationposition
        self.state_pickedup = False
        self.state_delevered = False
        self.waitingtime = waitingtime
        self.attributedSAV = None

    def update_state(self, pickup, delevery):
        self.state_pickedup = pickup
        self.state_delevered = delevery
    
    ### This part is dedicated for the the creation of the passenger request 
    def create_passenger_request(self, listofavailableSAV):
        #Ensure that passenger is in good condition (has the right state)
        self.update_state(pickup= False, delevery= False)
        WriteLogMessage.passenger_request_message(passenger=self)
        self.passenger_listner(listofavailableSAV=listofavailableSAV)
        
        """while self.waitingtime:
            if (not self.state_pickedup and not self.state_delevered):
                logging.info("The passenger {} has pickedup request with a waiting time {}".format(self.passenger_ID, self.waitingtime))
                if len(listofSAV):
                    self.selectSAV(listofSAV= listofSAV)
            else:
                break
            sleep(0.5)
            self.waitingtime = self.waitingtime - 1
        if self.state_pickedup and not self.state_delevered:
            logging.info("The passenger {} was pickedup".format(self.passenger_ID))
        if self.state_delevered:
            logging.info("The passenger {} successfully reached his destination".format(self.passenger_ID))
        elif not self.state_pickedup and not self.state_delevered:
            logging.info("The passenger {} was not affected to any available SAV")"""

    def passenger_listner(self, listofavailableSAV):
        pricelistSAV = []
        sleep(self.waitingtime)
        for sav in listofavailableSAV:
            pricelistSAV.append([sav,sav.calculateprice()])
        self.selectSAV(pricelistSAV=pricelistSAV)

    
    def selectSAV(self, pricelistSAV):
        bestSAV = None
        bestprice = 10
        for priceSAV in pricelistSAV:

            #priceSAV: is a list of dictionary 
            #sav[0]: is the vehicle that provide the price (an instance of sav)
            #sav[1]: is the price of traveled trip
            
            if priceSAV[1] < bestprice:
                bestSAV = priceSAV[0]
                bestprice = priceSAV[1]
            #In case that various SAVs provide the same price
            #The passenger select the SAV with the most place available 
            if priceSAV[1] == bestprice:
                if priceSAV[0].availableplace > bestSAV.availableplace:
                      bestSAV = priceSAV[0]
        self.attributedSAV = bestSAV
        self.waitingtime = 0
        WriteLogMessage.passenger_selection_of_SAV(passenger=self,bestSAV=bestSAV,bestprice=bestprice)
        # logging.info("The passenger {} has selected the SAV {}".format(self.passenger_ID, self.attributedSAV.SAV_ID))
        self.update_state(pickup= not self.state_pickedup, delevery= self.state_delevered) 
        self.attributedSAV.update_listofpassengers(self, pickup=self.state_pickedup, delevery=self.state_delevered)
        
    
    ### Second part delevery
    def passenger_delevery(self):
        self.state_delevered = True
        self.attributedSAV.update_listofpassengers(passenger=self, pickup=self.state_pickedup, delevery=self.state_delevered)
        logging.info("The passenger {} has successfully reached his destination".format(self.passenger_ID))

    def run(self,listofavailableSAV):
        self.create_passenger_request(listofavailableSAV)