import threading
import time
from PBL.Controller import csvController

class TimerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while True:
            self.getWeightRegularly()

    def getWeightRegularly(self):
        active_item = csvController.CsvController().getActiveItem()
        # new_weight = self.scaleController.getWeight()
        # self.csvController.updateItemWeight(active_item,new_weight)
        time.sleep( 5)
        # ↓test
        print("1[s]")