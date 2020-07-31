import tkinter as tk
import time
from PBL.Controller import csvController
from .Components import itemComponent
import os
from PBL import application
from PBL.Controller import scaleController

class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side="top",fill="both",expand=True)

        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)


        self.csvController = csvController.CsvController()
        # self.scaleController = scaleController.ScaleController()
        itemList = self.loadItemData()
        statusVariable = tk.IntVar()
        if itemList:
            for index,item in enumerate(itemList):
                itemFrame = itemComponent.ItemComponent(self.frame, itemList[index],index)
                itemFrame.status = statusVariable
                itemFrame.status_control['value']=index
        self.getWeightRegularly()

    def loadItemData(self):
        itemList = self.csvController.getItemData()
        return itemList


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def getWeightRegularly(self):
        active_item = self.csvController.getActiveItem()
        while True:
            # new_weight = self.scaleController.getWeight()
            # self.csvController.updateItemWeight(active_item,new_weight)
            # time.sleep( 15 * 60 )
            # ↓test
            print( "1[s]" )
            self.after( 1 * 1000 )

