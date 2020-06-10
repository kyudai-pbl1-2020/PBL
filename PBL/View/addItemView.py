import tkinter as tk
from Controller.addItemController import Controller

class AddItemView(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent,background="purple")
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=2)  # this needed to be added
        self.grid_columnconfigure(0, weight=2)  # as did this

        name_frame = tk.Frame(self)#,background="red")
        name_frame.grid(row=0,column=1,sticky="nsew")

        text_frame = tk.Frame(self)#,background="blue")
        text_frame.grid(row=2,column=1,sticky="nswe")

        button_frame = tk.Frame(self)#,background="green")
        button_frame.grid(row=3,column=1,sticky="nsew")


        self.name_label = tk.Label(name_frame, text="Item Name").grid(row=0,column=0,padx=20,pady=10)
        self.name_entry = tk.Entry(name_frame)
        self.name_entry.grid(row=0,column=1,padx=20,pady=10)

        self.weight_label = tk.Label(name_frame, text="Desired Weight").grid(row=1,column=0,padx=20,pady=10)
        self.weight_entry = tk.Entry(name_frame).grid(row=1,column=1,padx=20,pady=10)

        self.add_button = tk.Button(name_frame, text="Add Item", command=self.addItem)
        self.add_button.grid(row=1,column=3,pady=20)

        self.url_label = tk.Label(text_frame, text="Amazon URL").pack(side=tk.LEFT,padx=20)
        self.url_text = tk.Text(text_frame,borderwidth=1)
        self.url_text.pack(side=tk.RIGHT)

        self.url_text.configure(highlightbackground="black")
        text_frame.grid_propagate(False)

    def addItem(self):
        self.controller = Controller()
        amazon_url = self.url_text.get("1.0","end-1c")
        product_name = self.name_entry.get()
        img_url = self.controller.getImage(amazon_url)
        self.controller.download(img_url,product_name)
        self.controller.closeDriver()