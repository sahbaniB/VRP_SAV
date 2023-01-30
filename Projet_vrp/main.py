import sys
sys.path.insert(0, 'C:/VRP/Projet_vrp')

#importing the module 
import logging 

#now we will Create and configure logger 
logging.basicConfig(filename="std.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 


from Autonomous_vehicle.SAV import SharedAutonomousVehicle
from Passenger.PASSENGER import Passenger
import logging

def createpassengerdemand(numberofdemand):
    #list of passenger
    listofpassengerdemand = [] 
    ag_id = 0
    while len(listofpassengerdemand) < numberofdemand:
        ag_id = ag_id+1
        ag_pickuppostion = (ag_id, ag_id+1)
        ag_destinationpostion = (ag_id+1, ag_id+2)
        ag_waitingtime = 3
        ag = Passenger(passenger_ID=ag_id, passenger_pickupposition=ag_pickuppostion, passenger_destinationposition=ag_destinationpostion, waitingtime=ag_waitingtime)
        listofpassengerdemand.append(ag)
    return listofpassengerdemand

def createSAVpopulation(numberofvehicle):
    listofSAV = []
    position = []
    sav_id = 0
    while len(listofSAV) < numberofvehicle:
        sav_id = sav_id + 1
        position = [sav_id, sav_id+1]
        Cmax = 3
        sav = SharedAutonomousVehicle(SAV_ID=sav_id, position=[], Cmax=Cmax)
        listofSAV.append(sav)
    return listofSAV

def main():
    logging.info('############# starting the programme #####################')
    listofsav = createSAVpopulation(5)
    listofpassengerdemand = createpassengerdemand(4)
    listofpassengerdemand[0].new_passengerrequest()
    listofavailableSAV = []
    for sav in listofsav:
        listofavailableSAV.append((sav, sav.calculateprice()))
    listofpassengerdemand[0].passenger_request(listofavailableSAV)


if __name__ == "__main__":
    main()