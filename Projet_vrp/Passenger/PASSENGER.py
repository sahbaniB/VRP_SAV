import logging
from time import sleep
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



class Passenger:
    def __init__(self, passenger_ID, passenger_pickupposition, passenger_destinationposition, waitingtime):
        self.passenger_ID = passenger_ID
        self.passenger_pickupposition = passenger_pickupposition
        self.passenger_destinaationposition = passenger_destinationposition
        self.state_pickedup = False
        self.state_delevered = False
        self.waitingtime = waitingtime
        self.attributedSAV = None

    def update_state(self, pickup, delevery):
        self.state_pickedup = pickup
        self.state_delevered = delevery
    
    ### Fist part pickup
    def new_passengerrequest(self):
        self.update_state(pickup= False, delevery= False)
        logging.info("The passenger {} is ready to lunch request".format(self.passenger_ID, self.waitingtime))

    def passenger_request(self, listofSAV):
        while self.waitingtime:
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
            logging.info("The passenger {} was not affected to any available SAV")

    def createrequest(self):
        self.update_state(pickup = True, delevery = True)
        self.passenger_request

    def selectSAV(self, listofSAV):
        bestSAV = None
        bestprice = 10
        for sav in listofSAV:
            """ 
            listofsav: is a list of dictionary 
            sav[0]: is the vehicle that provide the price (an instance of sav)
            sav[1]: is the price of traveled trip
            """
            logging.info("sav ID {}, sav price {}".format(sav[0].SAV_ID,sav[1]))
            if list(sav)[1] < bestprice:
                bestprice = list(sav)[1]
                bestSAV = list(sav)[0]

            #The passenger select the SAV with the most place available
            if list(sav)[1] == bestprice:
                if list(sav)[0].availableplace > bestSAV.availableplace:
                      bestSAV = list(sav)[0]
        self.attributedSAV = bestSAV
        self.waitingtime = 0
        logging.info("The passenger {} has selected the SAV {}".format(self.passenger_ID, self.attributedSAV.SAV_ID))
        self.update_state(pickup= not self.state_pickedup, delevery= self.state_delevered) 
        self.attributedSAV.update_listofpassengers(self, pickup=self.state_pickedup, delevery=self.state_delevered)
        
    
    ### Second part delevery
    def passenger_delevery(self):
        self.state_delevered = True
        self.attributedSAV.update_listofpassengers(passenger=self, pickup=self.state_pickedup, delevery=self.state_delevered)
        logging.info("The passenger {} has successfully reached his destination".format(self.passenger_ID))