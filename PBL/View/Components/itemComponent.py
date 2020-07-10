class AddItemView(tk.Frame):
    
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent)
        self.parent = parent
        self.grid()
