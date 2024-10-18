import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages.AddToCartPage import AddToCartPage

class AddToCartTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://qaecoma.bishalkarki.xyz/index.php?id_category=3&controller=category")
        cls.add_to_cart = AddToCartPage(cls.driver)

    def test_scroll_and_add_first_item_to_cart(self):
        # self.add_to_cart.scroll_to_first_item()
        self.add_to_cart.add_first_item_to_cart()
        # Optionally, verify the item was added successfully here

    # def test_hover_add_to_cart_icon(self):
    #     self.add_to_cart.hover_to_cart_icon()
    #     cart_details = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, AddToCartLocator.cart_detail))
    #     ).text
    #     self.assertIn("Expected Item Name", cart_details)  # Replace with actual expected item name

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
