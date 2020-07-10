import tkinter as tk
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PBL.View import addItemView
from PBL.View import MainUI

resourcesFolder = os.path.join(os.getcwd(), 'Resources')


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.makeResourcesFolder()

        self.geometry("600x500")
        self.grid_rowconfigure(0, weight=1)  # this needed to be added
        self.grid_columnconfigure(0, weight=1)  # as did this
        #self.resizable(width=False,height=False)
        self.title("PBL 1 Application")
        self.addMenu()
        #MainUI(self)
        addItemView.AddItemView(self)

    def addMenu(self):
        self.menu = tk.Menu()
        self.config(menu=self.menu)
        self.subMenu = tk.Menu(self.menu,tearoff=False)
        self.menu.add_cascade(label="File", menu=self.subMenu)  # Main Menu
        self.subMenu.add_command(label="Main Menu", command=lambda: self.changepage("MainUI"))
        self.subMenu.add_command(label="Add Item Page", command=lambda: self.changepage("AddItem"))
        self.subMenu.add_command(label="Quit", command=self.quit)

    def changepage(self,viewName):
        for widget in self.winfo_children():
            widget.destroy()
        if viewName == "MainUI":
            MainUI.MainUI(self)
        elif viewName == "AddItem":
            addItemView.AddItemView(self)

        self.addMenu()

    def makeResourcesFolder(self):
        if not os.path.isdir(resourcesFolder):
            os.mkdir(resourcesFolder)

def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()
