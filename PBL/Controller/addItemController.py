import os
import requests

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

from selenium.webdriver.chrome.options import Options
#https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-background

from application import resourcesFolder as resourcesPath

class Controller:
    def __init__(self):
        self.imagesFolder = os.path.join(resourcesPath, 'images')#PBL/Resources/images
        self.createDriver()

    def createDriver(self):
        #self.driver = webdriver.Chrome(os.path.join(self.resourcesFolder,'chromedriver'))
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def closeDriver(self):
         self.driver.close()


    def makeImagesFolder(self):
        if not os.path.isdir(self.imagesFolder):
            os.makedirs(self.imagesFolder)


    def getImage(self,url):
        self.driver.get(url)
        xpath2 = """//li[@class='image item itemNo0 maintain-height selected']//img"""
        xpath = """//li[@class='a-spacing-small item imageThumbnail a-declarative']//img"""
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(
            (By.XPATH, xpath2)))
        img = self.driver.find_elements_by_xpath(xpath2)[0]
        print(img)
        src = img.get_attribute('src')
        return src


    def download(self,url,productName):
        self.makeImagesFolder()
        response = requests.get(url, stream=True)
        filename = os.path.join(self.imagesFolder, productName)
        progress = response.iter_content(1024)
        with open(filename, "wb") as f:
            for data in progress:
                # write data read to the file
                f.write(data)


    def getItemPrice(self):
        price_xpath = "//*[@id='priceblock_ourprice']"
        item_price = self.driver.find_element_by_xpath(price_xpath).text
        #item starts with currency symbol $,¥,...
        item_price = item_price[1:]
        print(item_price)
        return item_price


    def getQuantities(self):
        # Click on one time purchase box
        one_time_purchase_div_xpath = "//*[@id='newAccordionRow']"
        one_time_purchase_alternate_xpath = "//*[@id='oneTimeBuyBox']"
        dropdown_menu = None
        try:
            self.naviguate(one_time_purchase_div_xpath, one_time_purchase_alternate_xpath)
        except TimeoutException:
            try:
                one_time_purchase_button = self.driver.find_element_by_id("oneTimeBuyBox").click()
            except:
                #Sometimes there are no boxes to click, the menu is already visible
                quantity_dropdown_menu_xpath = "//*[@id='quantity']"
                dropdown_menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, quantity_dropdown_menu_xpath)))


        if not dropdown_menu:
            # Select quantity from dropdown menu
            quantity_dropdown_menu_xpath = "//*[@id='quantity']"
            dropdown_menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, quantity_dropdown_menu_xpath)))

        options_element = [x for x in dropdown_menu.find_elements_by_tag_name("option")]
        options = []
        for element in options_element:
            options.append(element.get_attribute("value"))

        return options


    def naviguate(self,xpath,alternative_xpath=None):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath).click()
        except TimeoutException:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, xpath)))
            self.driver.find_element_by_xpath(alternative_xpath).click()


# if __name__ == "__main__":
#     c = Controller()
#     url = "https://www.amazon.co.jp/%E5%92%8C%E5%85%89%E5%A0%82-FQ4-%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E9%9B%A2%E4%B9%B3%E9%A3%9F-%E8%A3%8F%E3%81%94%E3%81%97%E3%81%8A%E3%81%95%E3%81%8B%E3%81%AA-2-6g%C3%976%E5%80%8B/dp/B0052VL6RI/ref=sr_1_12?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=baby+food&qid=1592376143&sr=8-12"
#     c.getImage(url)
#
#     c.closeDriver()

