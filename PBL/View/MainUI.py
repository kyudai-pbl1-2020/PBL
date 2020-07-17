import tkinter as tk
from PBL.Controller import csvController
from .Components import itemComponent
import os
from PBL import application

class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid()
        #label = tk.Label(self, text="Start Page")
        #label.grid(row = 0,column = 2)
        self.csvController = csvController.CsvController()
        itemList = self.loadItemData()
        if itemList:
            itemComponent.ItemComponent(self, itemList[0])


    def loadItemData(self):
        itemList = self.csvController.getItemData()
        return itemList
