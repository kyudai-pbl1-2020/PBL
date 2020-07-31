from .orderItemController import OrderItemController
from .csvController import CsvController
from PBL.client_socket import send_data_request

class SensorController:
    def __init__(self):
        self.csvController = CsvController()

    def querySensor(self,item):
        currentWeight = send_data_request()
        if currentWeight < item.weight:
            self.oic = OrderItemController()
            self.oic.orderItem(item)
            self.oic.closeDriver()

            self.csvController.updateItemStatus(item,status='Ordered')

        self.csvController.updateItemWeight(item,currentWeight)
