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
        itemList = self.loadItemData()
        statusVariable = tk.IntVar()
        if itemList:

            for index,item in enumerate(itemList):
                itemFrame = itemComponent.ItemComponent(self.frame, itemList[index],index)
                itemFrame.status = statusVariable
                itemFrame.status_control['value']=index


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


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))