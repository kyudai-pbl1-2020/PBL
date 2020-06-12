import os
import csv
from application import resourcesFolder as resourcesPath


class CsvController:
    def __init__(self):
        self.csvfile = os.path.join(resourcesPath,'items.csv')
        self.createCSVFile()

    def createCSVFile(self):
        if not os.path.isfile(self.csvfile):
            with open(self.csvfile,'w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Item Name","Weight goal","Status","Amazon URL","Image path"])


    def appendItemToCSV(self,item):
        with open(self.csvfile, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=' ')
            writer.writerow([item.name,item.weight,item.status,item.amazon_url,item.imgPath])