from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from Locators.AddToCartLocator import CartLocator


class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver

    def find_cart_icon(self):
        return self.driver.find_element(By.XPATH, CartLocator.cart_icon)

    def hover_to_cart_icon(self):
        icon = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, CartLocator.cart_icon))
        )
        ActionChains(self.driver).move_to_element(icon).perform()

    def get_cart_details(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, CartLocator.cart_detail))
        ).text

    def get_first_item(self):
        # return WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, AddToCartLocator.first_Item_Xpath))
        # )
        first_item = self.driver.find_element(By.XPATH, CartLocator.first_Item_Xpath)
        return first_item

    def get_cart_count(self):
        return self.driver.find_element(By.XPATH, CartLocator.cart_count)

    def scroll_to_first_item(self):
        # first_item = self.get_first_item()
        # self.driver.execute_script("arguments[0].scrollIntoView();", first_item)
        self.driver.execute_script("window.scrollTo(0,1000)")
        time.sleep(2)
        print("Trying to locate the first item...")
        first_item = self.driver.find_element(By.XPATH, CartLocator.first_Item_Xpath)
        time.sleep(2)
        print("First item found: ", first_item)
        return first_item

    def get_add_to_cart_button(self):
        return self.driver.find_element(By.XPATH, CartLocator.add_To_Cart_button)

    def add_first_item_to_cart(self):
        self.scroll_to_first_item()
        first_item = self.get_first_item()
        add_to_cart_button = self.get_add_to_cart_button()
        close_cart = self.driver.find_element(By.XPATH, CartLocator.close_cart)
        button_click = ActionChains(self.driver)
        button_click.move_to_element(first_item).click(add_to_cart_button).perform()
        time.sleep(2)
        button_click.move_to_element(first_item).perform()
        time.sleep(2)
        button_click.click(close_cart).perform()
        time.sleep(2)

