import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.purchase_product_page import PurchasePage

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qaecoma.bishalkarki.xyz/index.php?id_category=3&controller=category")
        self.cr = PurchasePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_purchase(self):
        self.cr.purchasefirst()
        self.cr.check_and_click_insertData("hello@gmail.com", "hello@gmail.com")
        time.sleep(2)
        self.cr.purchasesecond()
        expected_result = "Your order on Ecom A is complete."
        actual_result = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/p[1]').text
        self.assertEqual(expected_result, actual_result, "Second test case failed!!")

if __name__ == '__main__':
    unittest.main()
