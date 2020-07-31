import tkinter as tk
from PBL.Controller.userController import UserController

class CredentialView(tk.Frame):
    def __init__( self, parent ):
        tk.LabelFrame.__init__(self, parent,text="Add Item",labelanchor="n",font=("Arial",18),padx=10,pady=6)#,background="white")
        self.parent = parent
        self.grid()

        self.main_label = tk.Label(text="Enter your Amazon ID/PW")
        self.main_label.place(x=125, y=50)

        self.id_label = tk.Label(text="Amazon ID")
        self.id_label.place(x=50, y=100)
        self.id_box = tk.Entry()
        self.id_box.place(x=150, y=100)

        self.pw_label = tk.Label(text="Amazon PW")
        self.pw_label.place(x=50, y=150)
        self.pw_box = tk.Entry()
        self.pw_box.place(x=150, y=150)

        self.button = tk.Button(text="DONE", command=self.getInfo)
        self.button.place(x=175, y=200)


    def getInfo(self):
        id_value = self.id_box.get()
        pw_value = self.pw_box.get()
        user_ctrl = UserController()
        user_ctrl.setUserInformation( id_value, pw_value )
        #print( user_ctrl.getUserInformation() ) # for test
        self.parent.changepage("MainUI")
