import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MainUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.grid()
        label = tk.Label(self, text="Start Page")
        label.grid(row = 0,column = 2)
        self.GoogleSearch( "九大" )

    def GoogleSearch( self, key_word ):
        driver = webdriver.Chrome( executable_path = "./View/chromedriver" )
        # get chromedriver from 
        # https://sites.google.com/a/chromium.org/chromedriver/downloads
        driver.get( "https://www.google.co.jp" )

        elem = driver.find_element_by_name( "q" )
        elem.send_keys( key_word )
        elem.send_keys( Keys.ENTER )
        driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3').click()