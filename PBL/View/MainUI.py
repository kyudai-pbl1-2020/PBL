import tkinter as tk

class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid()
        label = tk.Label(self, text="Start Page")
        label.grid(row = 0,column = 2)

        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: None)
        button.grid(row = 0,column = 0)

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda:None)
        button2.grid(row = 1,column = 0)