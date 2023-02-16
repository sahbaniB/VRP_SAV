import logging 

#now we will Create and configure logger 
logging.basicConfig(filename="C:/GIT_VRP/VRP_SAV/Projet_vrp/logfile.log", 
					format='%(asctime)s %(message)s', 
					filemode='w',
                    level=logging.INFO) 


#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
    
class WareHouse:
    def __init__(self, warehouse_ID, warehouse_position, numberofSAV, listofSAV) -> None:
        self.warehouse_ID = warehouse_ID
        self.warehouse_position = warehouse_position
        self.numberofSAV = numberofSAV
        self.listofSAV = listofSAV

    def update_warehouse(self, listofSAV):
        for SAV in listofSAV:
            #self.listofSAV.append(SAV)
            logging.info("SAV {} is added to the Warehouse {} with the position {}".format(SAV.SAV_ID, self.warehouse_ID, self.warehouse_position))

    