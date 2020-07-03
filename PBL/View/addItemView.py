import tkinter as tk
from tkinter import ttk
import os
import math

from Controller.addItemController import Controller
from Controller.csvController import CsvController
from Model.item import Item

class AddItemView(tk.Frame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent,text="Add Item",labelanchor="n",font=("Arial",18),padx=10,pady=6)#,background="white")
        self.parent = parent
        self.amazon_limit = 2000.0 #(¥)
        self.grid()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)# as did this

        self.name_frame = tk.Frame(self)#,background="red")
        self.name_frame.grid(row=0,column=1,pady=10,sticky="nsew")

        self.text_frame = tk.Frame(self)#,background="blue")
        self.text_frame.grid(row=1,column=1,pady=5,sticky="nswe")

        self.button_frame = tk.Frame(self)#,background="green")
        self.button_frame.grid(row=2,column=1,sticky="nsew")

        self.name_label = tk.Label(self.name_frame, text="Item Name", borderwidth=7,font=("Arial",12)).grid(row=0,column=0,padx=20,pady=5)
        self.name_entry = tk.Entry(self.name_frame, bd=2, width=20)
        self.name_entry.grid(row=0,column=1,padx=20,pady=10)

        self.weight_label = tk.Label(self.name_frame, text="Desired Weight", borderwidth=7, font=("Arial",12)).grid(row=1,column=0,padx=20,pady=5)
        self.weight_entry = tk.Entry(self.name_frame,bd=2, width=20)
        self.weight_entry.grid(row=1,column=1,padx=20,pady=10)

        self.strVar = tk.StringVar(self.parent)
        self.menuOptions = [""]
        self.strVar.set(self.menuOptions[0])
        self.quantity_label = tk.Label(self.name_frame, text="Quantity", borderwidth=7, font=("Arial", 12)).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=20,
                                                                                                                 pady=5)
        self.quantity_dropdown = ttk.Combobox(self.name_frame, values=self.menuOptions,textvariable=self.strVar)
        self.quantity_dropdown.grid(row=2, column=1, padx=20, pady=10)
        self.quantity_dropdown.configure(state="readonly")

        self.unitPrice_label = tk.StringVar()
        self.minQuantity_label = tk.StringVar()
        self.totalPrice_label = tk.StringVar()
        self.info_label = tk.Label(self.name_frame, textvariable=self.unitPrice_label, width=15,font=("Arial",11)).grid(row=0,column=2)
        self.info_label = tk.Label(self.name_frame, textvariable=self.minQuantity_label, width=15,font=("Arial",11)).grid(row=1,column=2)
        self.info_label = tk.Label(self.name_frame, textvariable=self.totalPrice_label, width=15,font=("Arial",11)).grid(row=2,column=2)

        self.fetchInfo_button = tk.Button(self.button_frame, text="Item Info", borderwidth=7, font=("Arial", 13), width=10,height=2, command=self.fetchItemInfo)
        self.fetchInfo_button.pack(side=tk.LEFT, padx=100, pady=10)

        self.add_button = tk.Button(self.button_frame, text="Done", state=tk.DISABLED, borderwidth=7,font=("Arial",13), width=10,height=2, command=self.addItem)
        self.add_button.pack(side=tk.RIGHT,padx=30,pady=10)

        self.url_label = tk.Label(self.text_frame, text="Amazon URL", borderwidth=7,font=("Arial",12)).pack(side=tk.LEFT,padx=25)
        self.url_text = tk.Text(self.text_frame,borderwidth=1,width=40,height=15)
        self.url_text.pack(side=tk.RIGHT,padx=30)

        self.url_text.configure(highlightbackground="black")
        self.text_frame.grid_propagate(False)


    def fetchItemInfo(self):
        self.controller = Controller()
        self.product_name = self.name_entry.get()
        self.weight_goal = self.weight_entry.get()
        self.item_status = "Inactive"
        self.amazon_url = self.url_text.get("1.0","end-1c")
        self.img_url = self.controller.getImage(self.amazon_url)
        self.unit_price = self.controller.getItemPrice()
        self.imgPath = os.path.join(self.controller.imagesFolder, self.product_name)

        #If unit_price is a float
        if ',' in self.unit_price:
            self.unit_price = self.unit_price.replace(',','')

        #Get valid quantities from amazon dropdown menu and activate dropdown menu
        dropdown_options = self.controller.getQuantities()
        self.quantity = math.ceil(self.amazon_limit / float(self.unit_price))
        self.min_quantity = self.quantity
        dropdown_options = [value for value in dropdown_options if int(value) >= self.min_quantity]
        self.menuOptions = dropdown_options

        self.updateDropDownValues()

        self.total_price = int(self.quantity) * int(self.unit_price)

        self.unitPrice_label.set("Unit Price:" + str(self.unit_price))
        self.minQuantity_label.set("Minimum Quantity:" + str(self.quantity))
        self.totalPrice_label.set("Total Price:" + str(self.total_price))

        self.strVar.trace("w",self.comboBox_SelectionEvent)

        if self.total_price >= self.amazon_limit:
            self.add_button['state']=tk.NORMAL

        else:
            self.add_button['state'] = tk.DISABLED

        self.controller.closeDriver()


    def addItem(self):
        self.updateItemFromEntry()
        self.controller.download(self.img_url,self.product_name)

        item = Item(self.product_name,self.weight_goal,self.unit_price,self.quantity,self.item_status,self.amazon_url,
                    self.imgPath)
        self.csvController = CsvController()
        self.csvController.appendItemToCSV(item)

        self.parent.changepage("MainUI")


    def updateItemFromEntry(self):
        self.product_name = self.name_entry.get()
        self.weight_goal = self.weight_entry.get()
        self.quantity = int(self.strVar.get())


    def updateDropDownValues(self):
        self.quantity_dropdown["values"] = self.menuOptions
        self.strVar.set(self.menuOptions[0])
        self.quantity_dropdown.configure(state="normal")


    def comboBox_SelectionEvent(self, *args):
            self.quantity = self.strVar.get()
            self.total_price = int(self.quantity) * int(self.unit_price)
            self.totalPrice_label.set("Total Price:" + str(self.total_price))