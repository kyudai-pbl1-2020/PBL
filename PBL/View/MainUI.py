import tkinter as tk
from PBL.Controller import csvController
from .Components import itemComponent
import os
from PBL import application

class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent,background="orange")
        self.grid()
        #label = tk.Label(self, text="Start Page")
        #label.grid(row = 0,column = 2)
        self.csvController = csvController.CsvController()
        itemList = self.loadItemData()
        statusVariable = tk.IntVar()
        if itemList:
            for index,item in enumerate(itemList):
                itemFrame = itemComponent.ItemComponent(self, itemList[index])
                itemFrame.status = statusVariable
                itemFrame.status_control['value']=index
            #itemFrame.status.set(0)

    def loadItemData(self):
        itemList = self.csvController.getItemData()
        return itemList
