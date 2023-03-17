import logging
import random

#from Passenger.PASSENGER import Passenger
from requestAPI import requestAPI

import sys
import threading
from time import sleep
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

class SharedAutonomousVehicle(threading.Thread):
    def __init__(self, SAV_ID, x_position, y_position, CMAX, warehouse=None, CE=None, departuretime=None):
        self.SAV_ID = SAV_ID
        self.CE = CE
        self.CMAX = CMAX
        self.departuretime = departuretime
        self.listofpassengers = []
        self.listofpassengerdelevery = []
        self.availableplace = CMAX
        self.x_postion = x_position
        self.y_postion = y_position
        # The atribute state indicate if the SAV is available or not available
        self.state = True
        self.warehouse = warehouse
    
    def update_availableplace(self,pickup,delevery):
        if (pickup and not delevery):
            self.availableplace = self.availableplace - 1
        elif (not pickup and delevery):
            self.availableplace = self.availableplace + 1
        else:
            pass

    def update_state(self):
        pass
    
    def update_listofpassengers(self,passenger, pickup, delevery):
        if (pickup and not delevery):
            self.listofpassengers.append(passenger)
            self.postion = (passenger.x_passenger_pickupposition, passenger.y_passenger_pickupposition)
            logging.info('Passenger {} was picked-up to be deleverd to the position {}'.format(passenger.passenger_ID, passenger.x_passenger_destinationposition))
        elif (not pickup and delevery):
            self.listofpassengers.pop()
            self.postion = (passenger.x_passenger_destinationposition, passenger.y_passenger_destinationposition)
            logging.info('{} passenger was delevered to the position {}'.format(passenger.passenger_ID, passenger.x_passenger_destinationposition))
        self.update_availableplace(pickup, delevery)

    #TODO: Need to add the clustering algorithm to calculate the price
    def calculateprice(self):
        listofprice = [1,2,3,4,5]
        random_index = random.randint(0,len(listofprice)-1)
        return listofprice[random_index]

    ### This part is dedicated to the dynamic routing of the SAV
    def routingsav(self):
        lastlistofpassenger=[]
        while True:
            while len(self.listofpassengers) and self.listofpassengers !=  lastlistofpassenger:
                # If the Sav had only one passenger => the passenger wil define the cluster
                if len(self.listofpassengers)==1:
                    self.create_pickup_cluster(passenger=self.listofpassengers[0])
                    self.create_destination_cluster(passenger=self.listofpassengers[0])
                else:
                    self.optimazed_liste()

                
            sleep(3)

            
    def define_the_travel_time(self, x_origin, y_origin, x_desitinationn, y_destination):
        # Create the array to define the passengers and  
        pass

    def create_pickup_cluster(self,passenger):
        pass

    def create_destination_cluster(self, passenger):
        pass

    def optimazed_liste(self):
        array_of_passennger_duration = []
        i=0 
        for passenger in self.listofpassengers:
            duration=requestAPI.calculate_time_travel(x_origin=self.x_postion, y_origin=self.y_postion, x_destination=passenger.x_passenger_pickupposition,\
                 y_destination= passenger.y_passenger_pickupposition)
            array_of_passennger_duration.append([passenger,duration])
            pass

    
    ### This part is dedicated for the reaserch for passengers (customers) 
    """def listnerthread(self,newlistofpassengerdemand):
        #Try to catch client
        lastlistofpassengerdemand = []
        while True:
            try:
                #Add the condition that we have available place    
                if newlistofpassengerdemand != lastlistofpassengerdemand:
                    newpassenger = [x for x in newlistofpassengerdemand]
                    prices = []
                    for i in newpassenger:
                        prices.append(self.calculateprice())
                        lastlistofpassengerdemand = newlistofpassengerdemand
            except Exception:
                logging.info("Verify the list of passenger demand")"""

    def schedular(self,passenger):
        self.update_listofpassengers(passenger=passenger, \
            pickup= passenger.passenger_pickupposition, delevery= passenger.passenger_destinationposition)
                


    def findpickupcluster(self):
        pass

    ### The second part delevery
    def finddeleverycluster(self):
        pass 

