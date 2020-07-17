import tkinter as tk
import time
from PBL.View import addItemView as ai
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

        self.main_frame = tk.Frame(self)
        canvas = tk.Canvas(self.main_frame)
        scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

    def loadItemData(self):
        itemList = self.csvController.getItemData()
        return itemList
