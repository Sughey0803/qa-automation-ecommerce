from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    def is_product_in_cart(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")) > 0