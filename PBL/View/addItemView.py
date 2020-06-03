import tkinter as tk

class AddItemView(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid()
        a = tk.Label(parent, text="First Name").grid(row=0, column=0)
        b = tk.Label(parent, text="Last Name").grid(row=1, column=0)
        c = tk.Label(parent, text="Email Id").grid(row=2, column=0)
        d = tk.Label(parent, text="Contact Number").grid(row=3, column=0)
        a1 = tk.Entry(parent).grid(row=0, column=1)
        b1 = tk.Entry(parent).grid(row=1, column=1)
        c1 = tk.Entry(parent).grid(row=2, column=1)
        d1 = tk.Entry(parent).grid(row=3, column=1)
