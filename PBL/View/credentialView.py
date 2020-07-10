import os

class UserController():
    def __init__( self, id=None, pw=None):
        self.userid = id
        self.userpw = pw


    def setUserInformation( self, id, pw ):
        self.userid = id
        self.userpw = pw

        # Set environment variables
        os.environ["AMAZON_ID"] = self.userid
        os.environ["AMAZON_PW"] = self.userpw

    def getUserInformation(self):
        # Get environment variables
        self.userid = os.getenv("AMAZON_ID")
        self.userpw = os.environ.get("AMAZON_PW")
        return (self.userid, self.userpw)

import tkinter as tk
# from Controller.userController import UserController
import matplotlib
matplotlib.use( "tkagg" )

root = tk.Tk()

root.title( "Amazon ID/PW" )
root.geometry( "400x300" )

content = tk.Label( text = "Enter your Amazon ID/PW" )
content.place( x = 0, y = 200 )
content.pack()

id_box = tk.Entry()
id_box.pack()
id_value = id_box.get()

pw_box = tk.Entry()
pw_box.pack()
pw_value = pw_box.get()

user_ctrl = UserController()
user_ctrl.setUserInformation( id_value, pw_value )

print( user_ctrl.getUserInformation() )

class AddItemView( tk.Frame ):
    def __init__( self, parent ):
        tk.LabelFrame.__init__( self, parent )
        self.parent = parent
        self.grid()

root.mainloop()

