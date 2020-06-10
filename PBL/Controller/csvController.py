import os
import csv

class Controller:
    def __init__(self):
        self.resourcesFolder = os.path.join(os.getcwd() + 'Resources')
        self.csvfile = os.path.join(self.resourcesFolder,'items.csv')
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