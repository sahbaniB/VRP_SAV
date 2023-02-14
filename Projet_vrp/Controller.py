import random
import pandas as pd
import json
import threading
import sys
sys.path.insert(0, 'C:/git_vrp/VRP_SAV')


from Autonomous_vehicle.SAV import SharedAutonomousVehicle
from Passenger.PASSENGER import Passenger
from Write_logfile import WriteLogMessage
from Autonomous_vehicle.Warehouses import WareHouse

#class Controller(threading.Thread):
class Controller():
    
    def __init__(self, listofWareHouse=[], listofSAV=[], listofpassengerdemand=[]):
        threading.Thread.__init__(self)
        self.listeofWareHouse = listofWareHouse
        self.listofSAV = listofSAV
        self.listofpassengerdemand = listofpassengerdemand
    
    #Create The warehouses
    def createWarehouses(self):
        #Read the coordination of warehouse from file WareHouses.xlsx
        WareHouses = pd.read_excel("C:/GIT_VRP/VRP_SAV/WareHouse.xlsx",index_col=0)
        for k in WareHouses.index:
            warehouse = WareHouse(warehouse_ID=WareHouses['warehouse_id'][k], warehouse_position=(WareHouses['position_x'][k],WareHouses['position_y'][k]), \
                numberofSAV=WareHouses['number of SAV'][k], listofSAV=json.loads(WareHouses['attributed SAV'][k]))
            warehouse.update_warehouse(self.createSAVs(listofSAV=warehouse.listofSAV, warehouse=warehouse))
            #Update the list of warehouse for the controller 
            self.listeofWareHouse.append(warehouse)
        WriteLogMessage.reportWareHouse(warehouses=self.listeofWareHouse)

    #Create the SAVs for each warehouse
    #The creation of the SAV is directly related to the creation of warehouses
    def createSAVs(self, listofSAV, warehouse):
        for id in listofSAV:
            sav_id = id
            warehouseid = warehouse.warehouse_ID
            position = warehouse.warehouse_position
            #For the moment Cmax is a constant 
            #Need to chage the Cmax to an input defined at the beginning of the program
            #Please you need to chage the capacity of SAV 
            Cmax = 3
            sav = SharedAutonomousVehicle(SAV_ID=sav_id, position=position, Cmax=Cmax,warehouse_ID= warehouseid,warehouse_position=position)
            listofSAV.append(sav)
            self.listofSAV.append(sav)
        return listofSAV

    #Create the profile for demands
    def createpassengerdemand(self,numberofdemand):
        passengerlist = pd.read_excel("C:/GIT_VRP/VRP_SAV/cleaneddb.xlsx")
        #list of passenger
        listofprofileofdemand = []
        while len(listofprofileofdemand) < numberofdemand + 1:
            passengertrip = random.choice(passengerlist.index)
            if passengertrip not in listofprofileofdemand:
                listofprofileofdemand.append(passengertrip)
        listofpassengerdemand = [] 
        for i in listofprofileofdemand:
            ag = Passenger(passenger_ID=passengerlist["person_id"][i], passenger_pickupposition=(passengerlist["origin_x"][i],\
                passengerlist["origin_y"][i]), passenger_destinationposition=(passengerlist["destination_x"][i],\
                    passengerlist["destination_y"][i]), waitingtime=3)
            WriteLogMessage.passenger_request(ag)
            listofpassengerdemand.append(ag)
            self.listofpassengerdemand.append(ag) 
        return listofpassengerdemand

    def run(self):
        WriteLogMessage.starting_program(numberofsav=5)
        #Create the Warehouses and the SAVs
        self.createWarehouses()
        #Create the demande of passenger 
        self.createpassengerdemand(17)

controller1 = Controller()
controller1.run()


