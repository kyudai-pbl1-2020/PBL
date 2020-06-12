import tkinter as tk
import os
from Controller.addItemController import Controller
from Controller.csvController import CsvController
from Model.item import Item

class AddItemView(tk.Frame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent,text="Add Item",labelanchor="n",font=("Arial",18),padx=10,pady=6)#,background="white")
        self.grid()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)# as did this

        name_frame = tk.Frame(self)#,background="red")
        name_frame.grid(row=0,column=1,pady=10,sticky="nsew")

        text_frame = tk.Frame(self)#,background="blue")
        text_frame.grid(row=1,column=1,pady=5,sticky="nswe")

        button_frame = tk.Frame(self)#,background="green")
        button_frame.grid(row=2,column=1,sticky="nsew")


        self.name_label = tk.Label(name_frame, text="Item Name", borderwidth=7,font=("Arial",12)).grid(row=0,column=0,padx=20,pady=10)
        self.name_entry = tk.Entry(name_frame, bd=2, width=40)
        self.name_entry.grid(row=0,column=1,padx=20,pady=10)

        self.weight_label = tk.Label(name_frame, text="Desired Weight", borderwidth=7, font=("Arial",12)).grid(row=1,column=0,padx=20,pady=10)
        self.weight_entry = tk.Entry(name_frame,bd=2, width=40)
        self.weight.grid(row=1,column=1,padx=20,pady=10)

        self.add_button = tk.Button(button_frame, text="Done", borderwidth=7,font=("Arial",13), width=10,height=2, command=self.addItem)
        self.add_button.pack(side=tk.RIGHT,padx=30,pady=10)

        self.url_label = tk.Label(text_frame, text="Amazon URL", borderwidth=7,font=("Arial",12)).pack(side=tk.LEFT,padx=25)
        self.url_text = tk.Text(text_frame,borderwidth=1,width=40,height=15)
        self.url_text.pack(side=tk.RIGHT,padx=30)

        self.url_text.configure(highlightbackground="black")
        text_frame.grid_propagate(False)

    def addItem(self):
        self.controller = Controller()
        product_name = self.name_entry.get()
        weight_goal = self.weight_entry.get()
        item_status = "Inactive"
        amazon_url = self.url_text.get("1.0","end-1c")
        img_url = self.controller.getImage(amazon_url)

        self.controller.download(img_url,product_name)

        imgPath = os.path.join(self.controller.imagesFolder, product_name)
        self.controller.closeDriver()

        item = Item(product_name,weight_goal,item_status,amazon_url,imgPath)
        self.csvController = CsvController()
        self.csvController.appendItemToCSV(item)

        self.parent.changepage("MainUI")
