import os
import csv
from application import resourcesFolder as resourcesPath


class CsvController():
    def __init__(self):
        self.csvfile = os.path.join(resourcesPath,'items.csv')

    def appendItemToCSV(self,item):
        if os.path.exists(self.csvfile):
            filemode = 'a'
        else:
            filemode='w'

        with open(self.csvfile, filemode, newline='') as file:
            writer = csv.writer(file, delimiter=' ')
            headers_data = item.fileData()
            if filemode == 'w':
                writer.writerow(headers_data['headers'])

            writer.writerow(headers_data['data'])