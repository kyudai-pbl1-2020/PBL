from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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
            self.naviguate(one_time_purchase_div_xpath)
        except TimeoutException:
            self.naviguate(one_time_purchase_alternate_xpath)

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

        #Checkout
        checkout_button_xpath = "//*[@id='sc-buy-box-ptc-button']/span/font/font/input"
        self.naviguate(checkout_button_xpath)


    def naviguate(self,xpath):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, xpath)))
        self.driver.find_element_by_xpath(xpath).click()


from Model import item as Item
if __name__ == "__main__":
    test_url = "https://www.amazon.co.jp/%E5%92%8C%E5%85%89%E5%A0%82-FQ4-%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E9%9B%A2%E4%B9%B3%E9%A3%9F-%E8%A3%8F%E3%81%94%E3%81%97%E3%81%8A%E3%81%95%E3%81%8B%E3%81%AA-2-6g%C3%976%E5%80%8B/dp/B0052VL6RI/ref=sr_1_8?dchild=1&keywords=%E3%83%99%E3%83%93%E3%83%BC%E3%83%95%E3%83%BC%E3%83%89&qid=1591943963&sr=8-8"
    test_item = Item.Item('testItem','500',4.99,4,'inactive',test_url,"somePath")
    oic = OrderItemController()
    oic.orderItem(test_item)
    #oic.closeDriver()