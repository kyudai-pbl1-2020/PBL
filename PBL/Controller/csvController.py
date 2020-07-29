import os
import csv
from PBL import application
from PBL.Model import item

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
                data = row.split(' ')
                newItem = item.Item(name=data[0], weight=data[1], unit_price=data[2], quantity=data[3],
                                    status=data[4], amazon_url=data[5], imgPath=data[6].rstrip())

                itemList.append(newItem)

        return itemList


    def updateItemStatus(self,item):
        rows = []
        with open(self.csvfile, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                fields = row[0].split(" ")
                if fields[6] == item.imgPath:
                    fields[4] = 'Active'
                else:
                    fields[4] = 'Inactive'

                row = fields
                rows.append(row)

        with open(self.csvfile, 'w') as writeFile:
            writer = csv.writer(writeFile,delimiter=" ",quoting=csv.QUOTE_MINIMAL)
            writer.writerows(rows)


    def updateItemWeight(self,item, weight):
        rows = []
        with open(self.csvfile, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                fields = row[0].split(' ')
                if fields[6] == item.imgPath:
                    fields[1] = str(weight)
                    row = ' '.join(fields)

                rows.append(row)

        with open(self.csvfile, 'w') as writeFile:
            writer = csv.writer(writeFile,delimiter=" ",quoting=csv.QUOTE_MINIMAL)
            writer.writerows(rows)
