import os
import csv
from PBL import application

class CsvController():
    def __init__(self):
        self.csvfile = os.path.join(application.resourcesFolder,'items.csv')


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


    def deleteItem(self,item):
        rows = []
        with open(self.csvfile, 'r') as file:
            reader = csv.reader(file)
            print(item.imgPath)
            for row in reader:
                rows.append(row)
                fields = row[0].split(' ')
                if fields[6] == item.imgPath:
                    rows.remove(row)

        with open(self.csvfile, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(rows)

        #remove img
        os.remove(item.imgPath)

    def getItemData(self):
        #name weight unit_price quantity status amazon_url img

        itemList = []

        if not os.path.exists(self.csvfile):
            return itemList

        with open(self.csvfile,newline='') as file:
            file.readline() #Skip Headers
            for row in file:
                item = {}
                data = row.split(' ')
                item['name'] = data[0]
                item['weight'] = data[1]
                item['unit_price'] = data[2]
                item['quantity'] = data[3]
                item['status'] = data[4]
                item['amazon_url'] = data[5]
                item['imgPath'] = data[6].rstrip()

                itemList.append(item)

        return itemList