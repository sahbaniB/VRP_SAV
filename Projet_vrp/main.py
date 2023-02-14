import random
import pandas as pd

"""import sys
sys.path.insert(0, 'C:/git_vrp/VRP_SAV')"""
 

from Autonomous_vehicle.SAV import SharedAutonomousVehicle
from Passenger.PASSENGER import Passenger
from Write_logfile import WriteLogMessage

def createpassengerdemand(numberofdemand, passengerlist):
    #list of passenger
    listofpassenger = []
    while len(listofpassenger) < numberofdemand + 1:
        passengertrip = random.choice(passengerlist.index)
        if passengertrip not in listofpassenger:
            listofpassenger.append(passengertrip)
    listofpassengerdemand = [] 
    for i in listofpassenger:
        ag = Passenger(passenger_ID=passengerlist["person_id"][i], passenger_pickupposition=(passengerlist["origin_x"][i],passengerlist["origin_y"][i]), passenger_destinationposition=(passengerlist["destination_x"][i],passengerlist["destination_y"][i]), waitingtime=3)
        WriteLogMessage.passenger_request(ag)
        listofpassengerdemand.append(ag)
    return listofpassengerdemand
    """ag_id = 0
    while len(listofpassengerdemand) < numberofdemand:
        ag_id = ag_id+1
        ag_pickuppostion = (ag_id, ag_id+1)
        ag_destinationpostion = (ag_id+1, ag_id+2)
        ag_waitingtime = 3
        ag = Passenger(passenger_ID=ag_id, passenger_pickupposition=ag_pickuppostion, passenger_destinationposition=ag_destinationpostion, waitingtime=ag_waitingtime)
        listofpassengerdemand.append(ag)
    return listofpassengerdemand"""

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
    WriteLogMessage.starting_program(numberofsav=5)
    passengerlist = pd.read_excel("C:/GIT_VRP/VRP_SAV/cleaneddb.xlsx")
    listofsav = createSAVpopulation(5)
    listofpassengerdemand = createpassengerdemand(4,passengerlist)
    listofpassengerdemand[0].new_passengerrequest()
    listofavailableSAV = []
    for sav in listofsav:
        listofavailableSAV.append((sav, sav.calculateprice()))
    listofpassengerdemand[0].passenger_request(listofavailableSAV)


if __name__ == "__main__":
    main()