import tkinter as tk
from PBL.Controller import csvController
from .Components import itemComponent


class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid()
        #label = tk.Label(self, text="Start Page")
        #label.grid(row = 0,column = 2)
        itemComponent.ItemComponent(self)
        self.csvController = csvController.CsvController()
        self.loadItemData()



    def loadItemData(self):
        itemList = self.csvController.getItemData()
