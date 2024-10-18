import time
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Purchase_product_Locator import Purchaselocate
from Unit_testing.User_login_testing import UserLoginTest
from Pages.AddToCartPage import AddToCartPage

class PurchasePage:
    def __init__(self, driver):
        self.random = random
        self.driver = driver
        self.location = Purchaselocate
        self.cart = AddToCartPage(self.driver)
# Product adding function need to call here

    def navCart(self):
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        navCartLocation = self.driver.find_element(By.XPATH, self.location.navCart)
        time.sleep(2)
        return navCartLocation

    def cart_Click(self):
        self.navCart().click()

    def checkbtn1(self):
        checkout_locator = self.driver.find_element(By.XPATH, self.location.checkoutButton1)
        return checkout_locator

    def checkbtn1_click(self):
        self.checkbtn1().click()

    def checkbtn2(self):
        wait = WebDriverWait(self.driver, 10)
        checkout2_locator = wait.until(EC.element_to_be_clickable((By.XPATH, self.location.checkoutButton2)))
        return checkout2_locator

    def checkbtn2click(self):
        self.checkbtn2().click()

    def checkbox_nav(self):
        check_box = self.driver.find_element(By.ID, self.location.checkBox_id)
        return check_box

    def checkbox_click(self):
        self.checkbox_nav().click()

    def checkbtn3(self):
        checkout3_locator = self.driver.find_element(By.XPATH, self.location.checkoutButton3)
        return checkout3_locator

    def checkbtn3click(self):
        self.checkbtn3().click()

    def paymentMethod(self):
        payment1 = self.driver.find_element(By.XPATH, self.location.paymentOption1)
        payment2 = self.driver.find_element(By.XPATH, self.location.paymentOption2)
        return payment1, payment2

    def paymentClick(self):
        payment1, payment2 = self.paymentMethod()
        random_element = self.random.choice([payment1, payment2])  # Wrap the options in a list
        random_element.click()

    def ConfirmOrderr(self):
        confirm_order = self.driver.find_element(By.XPATH, self.location.confirmOrder)
        return confirm_order

    def ConfirmClick(self):
        self.ConfirmOrderr().click()

    def check_and_click_insertData(self, email, password):

        signin = self.driver.find_element(By.ID, 'email')
        signin.click()
        if signin:
          #  self.driver.get("https://qaecoma.bishalkarki.xyz/index.php?controller=authentication&back=https%3A%2F%2Fqaecoma.bishalkarki.xyz%2Findex.php%3Fcontroller%3Dorder%26step%3D1")
           UserLoginTest.login(self, email, password)
           time.sleep(2)
        self.driver.get("https://qaecoma.bishalkarki.xyz/index.php?controller=order&step=1")

    def check_for_empty_cart(self):
        empty = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[5]')
        if empty:
            time.sleep(1)
            self.cart.add_first_item_to_cart()
    def purchasefirst(self):
        print("Checking for empty cart...")
        self.check_for_empty_cart()
        print("Navigating to cart...")
        self.cart_Click()
        print("Clicked on the cart.")
        self.checkbtn1_click()

    def purchasesecond(self):
        self.checkbtn2click()
        self.checkbox_click()
        self.checkbtn3click()
        self.paymentClick()
        self.ConfirmClick()








