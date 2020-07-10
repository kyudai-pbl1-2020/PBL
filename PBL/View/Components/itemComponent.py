import tkinter as tk

class ItemComponent(tk.Frame):

    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent)
        self.parent = parent
        self.grid()

        self.pic_frame = tk.Frame(self, background="light green")
        self.pic_frame.grid(row=0, column=0, sticky="nsew")

        self.info_frame = tk.Frame(self, background="pink")
        self.info_frame.grid(row=0, column=1, sticky="nsew")

        #self.item_state = tk.Stringvar()
        self.active_contr = tk.Checkbutton(self.pic_frame)#, variable = self.item_state)
        self.active_contr.grid(row=0,column=0, padx=15)
        #
        self.pic_canvas = tk.Canvas(self.pic_frame, width=100, height=100, background="light gray")
        self.pic_canvas.grid(row=0, column=1, padx=15, pady=10)
        #
        self.name_label = tk.Label(self.info_frame, text="111", width=15, font=("Arial",12))
        self.name_label.grid(row=0, padx=15, pady=8)
        #
        self.gauge_canvas = tk.Canvas(self.info_frame, width=150, height=20, background="light grey")
        self.gauge_canvas.grid(row=1, padx=15, pady=8)

        self.order_button = tk.Button(self.info_frame, text="Order", width=9, height=1, command=self.orderItem, font=("Arial",8))
        self.order_button.grid(row=2, padx=15, pady=8)

    def orderItem(self):
        pass
