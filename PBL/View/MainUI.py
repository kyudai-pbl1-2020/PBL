import tkinter as tk
from Controller.csvController import CsvController

class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid()
        label = tk.Label(self, text="Start Page")
        label.grid(row = 0,column = 2)
        self.csvController = CsvController()
        self.loadItemData()



    def loadItemData(self):
        itemList = self.csvController.getItemData()
        print(itemList)