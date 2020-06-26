import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid()
        label = tk.Label(self, text="Start Page")
        label.grid(row = 0,column = 2)