import logging
import random
#from Passenger.PASSENGER import Passenger

import sys
sys.path.insert(0, 'C:/VRP/Projet_vrp')


#importing the module 
import logging 

#now we will Create and configure logger 
logging.basicConfig(filename="C:/VRP/Projet_vrp/std.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)

class SharedAutonomousVehicle:
    def __init__(self, SAV_ID, position, Cmax, CE=None, departuretime=None):
        self.SAV_ID = SAV_ID
        self.CE = CE
        self.Cmax = Cmax
        self.departuretime = departuretime
        self.listofpassengers = []
        self.availableplace = Cmax
        self.postion = position
    
    def update_availableplace(self,pickup,delevery):
        if (pickup and not delevery):
            self.availableplace = self.availableplace-1
        elif (not pickup and delevery):
            self.availableplace = self.availableplace+1
        else:
            pass
    
    def update_listofpassengers(self,passenger, pickup, delevery):
        if (pickup and not delevery):
            self.listofpassengers.append(passenger)
            self.postion = passenger.passenger_pickupposition
            logging.info('Passenger {} was picked-up to be deleverd to the position {}'.format(passenger.passenger_ID, passenger.passenger_destinaationposition))
        elif (not pickup and delevery):
            self.listofpassengers.pop()
            self.postion = passenger.passenger_destinationposition
            logging.info('{} passenger was delevered to the position {}'.format(passenger.passenger_ID, passenger.passenger_destinationposition))
        self.update_availableplace(pickup, delevery)

    ### The first part pickup
    def calculateprice(self):
        listofprice = [1,2,3,4,5]
        random_index = random.randint(0,len(listofprice)-1)
        return listofprice[random_index]


    def findpickupcluster(self):
        pass

    ### The second part delevery
    def finddeleverycluster(self):
        pass 

