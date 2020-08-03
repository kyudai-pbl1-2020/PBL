from .orderItemController import OrderItemController
from .csvController import CsvController
from PBL.client_socket import send_data_request


class SensorController:
    def __init__(self):
        self.csvController = CsvController()

    def querySensor(self,item):
        currentWeight = float(send_data_request())
        #currentWeight = currentWeight.strip("0")
        print(currentWeight,item.weight,type(currentWeight))
        if float(currentWeight) < float(item.weight):
            print("In if statement")
            self.oic = OrderItemController()
            self.oic.orderItem(item)
            self.oic.closeDriver()

            self.csvController.updateItemStatus(item,status='Ordered')

        self.csvController.updateItemWeight(item,currentWeight)
        return currentWeight


    def getWeightRegularly(self):
        #active_item = self.csvController().getActiveItem()
        #currentWeight = self.querySensor(active_item)
        # self.csvController.updateItemWeight(active_item,currentWeight)
        # ↓test
        print("1[s]")
        pass