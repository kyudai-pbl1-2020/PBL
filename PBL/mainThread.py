import threading
import time
from PBL.Controller import csvController

class TimerThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(TimerThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()
        self.start()

    def run(self):
        while not self.stopped():
            self.getWeightRegularly()

    def getWeightRegularly(self):
        #active_item = csvController.CsvController().getActiveItem()
        # new_weight = self.scaleController.getWeight()
        # self.csvController.updateItemWeight(active_item,new_weight)
        print("1[s]")
        time.sleep(5)
        # ↓test
        pass


    def stop(self):
        self._stop_event.set()


    def stopped(self):
        return self._stop_event.is_set()