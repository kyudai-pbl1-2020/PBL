import os

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,ElementNotInteractableException
from selenium.webdriver.support.select import Select


class OrderItemController:
    def __init__(self):
        self.createDriver()

    def createDriver(self):
        # self.driver = webdriver.Chrome(os.path.join(self.resourcesFolder,'chromedriver'))
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def closeDriver(self):
        self.driver.close()


    def orderItem(self,item):
        self.driver.get(item.amazon_url)
        #Click on one time purchase box
        one_time_purchase_div_xpath = "//*[@id='newAccordionRow']"
        one_time_purchase_alternate_xpath = "//*[@id='oneTimeBuyBox']"

        try:
            self.naviguate(one_time_purchase_div_xpath,one_time_purchase_alternate_xpath)
        except TimeoutException:
            one_time_purchase_button = self.driver.find_element_by_id("oneTimeBuyBox").click()

        #Select quantity from dropdown menu
        quantity_dropdown_menu_xpath = "//*[@id='quantity']"
        dropdown_menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, quantity_dropdown_menu_xpath)))
        dropdown_menu = Select(dropdown_menu)
        dropdown_menu.select_by_value(str(item.quantity))

        #Add to Cart
        add_to_cart_button_xpath = "//*[@id='add-to-cart-button']"
        self.naviguate(add_to_cart_button_xpath)

        #Go to Cart
        nav_bar_cart_xpath = "//*[@id='nav-cart']"
        self.naviguate((nav_bar_cart_xpath))

        #Proceed to checkout
        checkout_button_xpath = "//*[@id='sc-buy-box-ptc-button']/span/font/font/input"
        alternate_xpath = '//input[@type="submit" and @value="Proceed to checkout" and @class="a-button-input"]'
        try:
            self.naviguate_by_id("sc-buy-box-ptc-button")
        except TimeoutException:
            self.naviguate(checkout_button_xpath,alternate_xpath)

        self.login()

        standard_shipping_radio_button = "//*[@id='spc-orders']/div/div/div[3]/div/div/div[2]/div[2]/div[1]/fieldset/div[1]/input"
        self.naviguate(standard_shipping_radio_button)


    def naviguate(self,xpath,alternative_xpath=None):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, xpath)))
            self.driver.find_element_by_xpath(xpath).click()
        except TimeoutException:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, xpath)))
            self.driver.find_element_by_xpath(alternative_xpath).click()


    def naviguate_by_id(self,id):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.ID, id)))
        self.driver.find_element_by_id(id).click()

    def login(self):
        email_entry_xpath = "//*[@id='ap_email']"
        #amazon_id = os.environ.get('AMAZON_ID')
        amazon_id = "pblunit1@gmail.com"

        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,email_entry_xpath)))
        email_entry = self.driver.find_element_by_xpath(email_entry_xpath).send_keys(amazon_id)

        continue_button_xpath = "//*[@id='continue']"
        self.naviguate(continue_button_xpath)

        password_entry_xpath = "//*[@id='ap_password']"
        #amazon_pw = os.environ.get('AMAZON_PW')
        amazon_pw = "2020pbl1"

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, password_entry_xpath)))
            password_entry = self.driver.find_element_by_xpath(email_entry_xpath).send_keys(amazon_pw)
        except ElementNotInteractableException:
            password_entry = self.driver.find_element_by_id("ap_password").send_keys(amazon_pw)

        login_button_xpath = "//*[@id='signInSubmit']"
        self.naviguate(login_button_xpath)


if __name__ == "__main__":
    from PBL.Model import item
    test_url = "https://www.amazon.co.jp/%E5%92%8C%E5%85%89%E5%A0%82-FQ4-%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E9%9B%A2%E4%B9%B3%E9%A3%9F-%E8%A3%8F%E3%81%94%E3%81%97%E3%81%8A%E3%81%95%E3%81%8B%E3%81%AA-2-6g%C3%976%E5%80%8B/dp/B0052VL6RI/ref=sr_1_8?dchild=1&keywords=%E3%83%99%E3%83%93%E3%83%BC%E3%83%95%E3%83%BC%E3%83%89&qid=1591943963&sr=8-8"
    test_item = item.Item('testItem', '500', 4.99, 4, 'inactive', test_url, "somePath", )
    oic = OrderItemController()
    oic.orderItem(test_item)
    oic.closeDriver()