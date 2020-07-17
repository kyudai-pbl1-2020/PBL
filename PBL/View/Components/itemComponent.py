import tkinter as tk
from PIL import ImageTk, Image

class ItemComponent(tk.Frame):

    def __init__(self, parent,item):
        tk.LabelFrame.__init__(self, parent)
        self.parent = parent
        self.grid()
        #frame for checkbox, mage
        self.pic_frame = tk.Frame(self)#, background="light green")
        self.pic_frame.grid(row=0, column=0, sticky="nsew")
        #frame for name, weight, button
        self.info_frame = tk.Frame(self)#, background="pink")
        self.info_frame.grid(row=0, column=1, sticky="nsew")

        self.status = tk.StringVar()
        self.status.set(1)
        self.status_control = tk.Radiobutton(self.pic_frame, variable = self.status, value=0, command=self.activeItem)
        self.status_control.grid(row=0, column=0, padx=15)
        #
        #self.image_file = ImageTk.open("")
        #self.image_file.resize((100,100))
        self.canvas_width = 100
        self.canvas_height= 100
        self.pic_canvas = tk.Canvas(self.pic_frame, width=self.canvas_width, height=self.canvas_height,
                                    background="light gray")
        self.pic_canvas.grid(row=0, column=1, padx=15, pady=10)

        print(item)
        self.image = Image.open(item['imgPath'])
        self.image = self.image.resize((self.canvas_width,self.canvas_height),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.pic_canvas.create_image(0,0, anchor="nw", image=self.image)

        self.testlabel = tk.Label(self.pic_canvas)
        self.testlabel.image = self.image
        self.testlabel.configure(image=self.image)
        #self.testlabel.grid(row=1,column=1,padx=15,pady=10)
        #
        self.itemName_label = tk.StringVar()
        self.name_label = tk.Label(self.info_frame, textvariable=self.itemName_label, width=15, font=("Arial",12))
        self.name_label.grid(row=0, padx=15, pady=8, sticky="nsew")
        #
        self.progressBar = tk.Canvas(self.info_frame, width=150, height=20, background="light grey")
        self.progressBar.grid(row=1, padx=15, pady=8, sticky="nsew")

        self.current_weight = 100
        self.progressBar.create_rectangle(0,0,self.current_weight,25, fill="#00C5CD")

        self.order_button = tk.Button(self.info_frame, text="Order", width=12, height=2, command=self.orderItem, font=("Arial",12))
        self.order_button.grid(row=2, padx=15, pady=8)

    def orderItem(self): #order Button
        pass

    def activeItem(self):
        pass
