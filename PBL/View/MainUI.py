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
        testImg = os.path.join(application.resourcesFolder,'images/test3.gif')
        itemComponent.ItemComponent(self,testImg)
        self.csvController = csvController.CsvController()
        self.loadItemData()



    def loadItemData(self):
        itemList = self.csvController.getItemData()
