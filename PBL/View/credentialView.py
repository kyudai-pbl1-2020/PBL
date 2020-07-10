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
# content.pack()
content.place( x = 125, y = 50 )

id_label = tk.Label( text = "Amazon ID" )
id_label.place( x = 50, y = 100 )
id_box = tk.Entry()
id_box.place( x = 150, y = 100 )

pw_label = tk.Label( text = "Amazon PW" )
pw_label.place( x = 50, y = 150 )
pw_box = tk.Entry()
pw_box.place( x = 150, y = 150 )

def getInfo( event ):
    id_value = id_box.get()
    pw_value = pw_box.get()
    user_ctrl = UserController()
    user_ctrl.setUserInformation( id_value, pw_value )
    # print( user_ctrl.getUserInformation() )

button = tk.Button( text = "DONE" )
button.place( x = 175, y = 200 )
button.bind( "<Button-1>", getInfo )

root.mainloop()