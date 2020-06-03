import tkinter as tk
from View.addItemView import *
from View.MainUI import *


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("600x500")
        self.title("PBL 1 Application")
        self.addMenu()

    def addMenu(self):
        self.menu = tk.Menu()
        self.config(menu=self.menu)
        self.subMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu)  # Main Menu
        self.subMenu.add_command(label="Main Menu", command=lambda: self.changepage("MainUI"))
        self.subMenu.add_command(label="Add Item Page", command=lambda: self.changepage("AddItem"))
        self.subMenu.add_command(label="Test Page", command=lambda: self.changepage("PageTwo"))
        self.subMenu.add_command(label="Quit", command=self.quit)

    def changepage(self,viewName):
        for widget in self.winfo_children():
            widget.destroy()
        if viewName == "MainUI":
            MainUI(self)
        elif viewName == "AddItem":
            AddItemView(self)

        self.addMenu()



def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()