from .scaleController import ScaleController
from .orderItemController import OrderItemController
from .csvController import CsvController

class SensorController:
    def __init__(self):
        self.sc = ScaleController()
        self.csvController = CsvController()

    def querySensor(self,item):
        currentWeight = self.sc.getWeight()
        if currentWeight < item.weight:
            self.oic = OrderItemController()
            self.oic.orderItem(item)
            self.oic.closeDriver()

            self.csvController.updateItemStatus(item,status='Ordered')

        self.csvController.updateItemWeight(item,currentWeight)
