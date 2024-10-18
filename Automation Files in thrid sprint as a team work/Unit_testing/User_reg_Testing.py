import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.User_reg_page import UserPage

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qaecoma.bishalkarki.xyz/index.php")
        self.cr = UserPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_case1(self): # firstname field empty
        self.cr.registration("ps@gmail.com","", "member", "ps@gmail.com", "pass123")
        expected_result = "firstname"
        actual_result = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/div/ol/li/b').text
        self.assertEqual(expected_result,actual_result, "First test case failed!!")

    def test_case2(self): # lastname field empty
        self.cr.registration("ps@gmail.com","team", "", "ps@gmail.com", "pass123")
        expected_result = "lastname"
        actual_result = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/div/ol/li/b').text
        self.assertEqual(expected_result,actual_result, "Second test case failed!!")

    def test_case3(self): # email field empty
        self.cr.registration("ps@gmail.com","team", "member", "", "pass123")
        expected_result = "email"
        actual_result = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/div/ol/li/b').text
        self.assertEqual(expected_result,actual_result, "Third test case failed!!")

    def test_case4(self): # email not in internet standard
        self.cr.registration("ps@gmail.com", "team", "member", "ps@@gmail.com", "pass123")
        expected_result = "email"
        actual_result = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/div/ol/li/b').text
        self.assertEqual(expected_result, actual_result, "Fourth test case failed!!")

    def test_case5(self): #invalid email but in internet standard
        self.cr.registration("ps@gmail.com", "team", "member", "hgvbnbvh@gmail.com", "pass123")
        expected_result = "email"
        actual_result = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/div/ol/li/b').text
        self.assertEqual(expected_result, actual_result, "Fifth test case failed!!")

    def test_case6(self):  # Password field empty
        self.cr.registration("ps@gmail.com", "team", "member", "ps@gmail.com", "")
        expected_result = "password"
        actual_result = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/div/ol/li/b').text
        self.assertEqual(expected_result, actual_result, "Sixth test case failed!!")

    def test_case7(self): # All valid data
        self.cr.registration("pass@gmail.com", "Team", "member", "pass@gmail.com", "pass123")
        expected_result = "Team member"
        actual_result = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text
        self.assertEqual(expected_result, actual_result, "Seventh test case failed!!")

if __name__ == '__main__':
    unittest.main()
