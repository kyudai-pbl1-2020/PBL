import tkinter as tk

class ItemComponent(tk.Frame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent)
        self.parent = parent
        self.grid()

        #self.canvas = tk.Canvas(self, width=220, height=220, background="yellow")
        #self.canvas = pack()

        self.pic_frame = tk.Frame(self, background="red")
        self.pic_frame.grid(row=0, column=0, sticky="nsew")

        self.info_frame = tk.Frame(self, background="pink")
        self.info_frame.grid(row=0, column=1, sticky="nsew")

        #self.item_state = tk.Intvar()
        # self.active_contr = tk.Checkbutton(self.pic_frame, variable = self.item_state)
        # self.active_contr.grid(row=0,column=0)
        #
        self.pic_canvas = tk.Canvas(self.pic_frame, width=100, height=100, background="gray")
        self.pic_canvas.grid(row=0, column=1)
        #
        self.name_label = tk.Label(self.info_frame, text="111", borderwidth=7, font=("Arial",12))
        self.name_label.grid(row=0)
        #
        self.order_button = tk.Button(self.info_frame, text="Order", width=10, height=2, command=self.orderItem, font=("Arial",12))
        #self.order_button.grid(row=1)

    def orderItem(self):
        pass
