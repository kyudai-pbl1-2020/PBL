import tkinter as tk
import os
from Controller.addItemController import Controller
from Controller.csvController import CsvController
from Model.item import Item

class AddItemView(tk.Frame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent,text="Add Item",labelanchor="n",font=("Arial",18),padx=10,pady=6)#,background="white")
        self.parent = parent
        self.grid()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)# as did this

        name_frame = tk.Frame(self)#,background="red")
        name_frame.grid(row=0,column=1,pady=10,sticky="nsew")

        text_frame = tk.Frame(self)#,background="blue")
        text_frame.grid(row=1,column=1,pady=5,sticky="nswe")

        button_frame = tk.Frame(self)#,background="green")
        button_frame.grid(row=2,column=1,sticky="nsew")

        self.name_label = tk.Label(name_frame, text="Item Name", borderwidth=7,font=("Arial",12)).grid(row=0,column=0,padx=20,pady=5)
        self.name_entry = tk.Entry(name_frame, bd=2, width=20)
        self.name_entry.grid(row=0,column=1,padx=20,pady=10)

        self.weight_label = tk.Label(name_frame, text="Desired Weight", borderwidth=7, font=("Arial",12)).grid(row=1,column=0,padx=20,pady=5)
        self.weight_entry = tk.Entry(name_frame,bd=2, width=20)
        self.weight_entry.grid(row=1,column=1,padx=20,pady=10)

        self.quantity_label = tk.Label(name_frame, text="Quantity", borderwidth=7,font=("Arial",12)).grid(row=2,column=0,padx=20,pady=5)
        self.quantity_entry = tk.Entry(name_frame, bd=2, width=20)
        self.quantity_entry.grid(row=2,column=1,padx=20,pady=10)

        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.info_label = tk.Label(name_frame, textvariable=self.var1, width=15,font=("Arial",11)).grid(row=0,column=2)
        self.info_label = tk.Label(name_frame, textvariable=self.var2, width=15,font=("Arial",11)).grid(row=1,column=2)
        self.info_label = tk.Label(name_frame, textvariable=self.var3, width=15,font=("Arial",11)).grid(row=2,column=2)

        self.fetchInfo_button = tk.Button(button_frame, text="Item Info", borderwidth=7, font=("Arial", 13), width=10,height=2, command=self.fetchItemInfo)
        self.fetchInfo_button.pack(side=tk.LEFT, padx=100, pady=10)

        self.add_button = tk.Button(button_frame, text="Done", state=tk.DISABLED, borderwidth=7,font=("Arial",13), width=10,height=2, command=self.addItem)
        self.add_button.pack(side=tk.RIGHT,padx=30,pady=10)

        self.url_label = tk.Label(text_frame, text="Amazon URL", borderwidth=7,font=("Arial",12)).pack(side=tk.LEFT,padx=25)
        self.url_text = tk.Text(text_frame,borderwidth=1,width=40,height=15)
        self.url_text.pack(side=tk.RIGHT,padx=30)

        self.url_text.configure(highlightbackground="black")
        text_frame.grid_propagate(False)


    def fetchItemInfo(self):
        self.controller = Controller()
        self.product_name = self.name_entry.get()
        self.weight_goal = self.weight_entry.get()
        self.item_status = "Inactive"
        self.amazon_url = self.url_text.get("1.0","end-1c")
        self.img_url = self.controller.getImage(self.amazon_url)
        self.unit_price = self.controller.getItemPrice()
        self.quantity = self.quantity_entry.get()
        self.imgPath = os.path.join(self.controller.imagesFolder, self.product_name)
        self.var1.set("Unit Price:" + str(self.unit_price))
        self.var2.set("Quantity:" + str(self.quantity))
        self.var3.set("Total Price:" + str(self.quantity*self.unit_price))
        if self.quantity*self.unit_price >= 2000:
            self.add_button['state']=tk.NORMAL

    def addItem(self):
        self.controller.download(self.img_url,self.product_name)
        self.controller.closeDriver()

        item = Item(self.product_name,self.weight_goal,self.unit_price,self.quantity,self.item_status,self.amazon_url,
                    self.imgPath)
        self.csvController = CsvController()
        self.csvController.appendItemToCSV(item)

        self.parent.changepage("MainUI")
