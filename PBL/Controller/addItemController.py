import os
import requests

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


# if __name__ == "__main__":
#     c = Controller()
#     url = "https://www.amazon.co.uk/Autoglym-AG-035001-Interior-Shampoo/dp/B00114WOBC/ref=sr_1_1?ie=UTF8&qid=1553519250&sr=8-1&keywords=715933155337"
#     #img_urls = c.get_images(url)
#     #for img in img_urls:
#     #    c.download(img)
#     img_url = c.getImage(url)
#     c.download(img_url,"barre-tendre")

