import tkinter as tk
import time
from PBL.View import addItemView as ai
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

            itemComponent.ItemComponent(self, itemList[0])

        container = tk.Frame(self)
        canvas = tk.Canvas(container, width=550, height=500)
        canvas.place(x=100, y=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        for i in range(50):
            tk.Label(scrollable_frame, text="Sample scrolling label").pack()

        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


    def loadItemData(self):
        itemList = self.csvController.getItemData()
        return itemList
