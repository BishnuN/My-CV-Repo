import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

class UserLoginLocators:
    email = 'email'
    password = 'passwd'
    Login = '//*[@id="login_form"]/div[3]/button'
    Dashboard = '//*[@id="content"]/div[1]/div/h2'
    Email_Errormsg = '//*[@id="error"]'
    Pass_Errormsg = '//*[@id="error"]/ol/li'
    Both_Errormsg = '//*[@id="error"]'

class UserLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qaecoma.bishalkarki.xyz/admin123")

    def tearDown(self):
        self.driver.close()

    def login(self, username, password):
        driver = self.driver
        nav_email = driver.find_element(By.ID, UserLoginLocators.email)
        nav_email.send_keys(username)
        time.sleep(2)
        upass = driver.find_element(By.ID, UserLoginLocators.password)
        upass.send_keys(password)
        time.sleep(2)
        nav_login = driver.find_element(By.XPATH, UserLoginLocators.Login)
        nav_login.click()
        time.sleep(5)

    # TS_01_TC_01 - Valid login testing with correct email and password
    def test_login_success(self):
        driver = self.driver
        self.login("admin@qaecoma.bishalkarki.xyz", "Test123!@#")
        expected_result ="Dashboard"
        actual_result = driver.find_element(By.XPATH, UserLoginLocators.Dashboard).text
        self.assertEqual(expected_result, actual_result, "test_login_success passed")


    # TS_02_TC_01 - Validate logging into the Application using incorrect E-mail
    def test_login_incorrect_email(self):
        self.login("121@test.com","Test123!@#")
        #assert:check result
        expected_result ="E-mail or phone no. is incorrect"
        actual_result = self.driver.find_element(By.XPATH, UserLoginLocators.Email_Errormsg).text
        self.assertEqual(expected_result, actual_result, "Error message didnot match")

    # TS-02_TC_02- Validate logging into the Application using incorrect password.
    def test_login_incorrect_password(self):
        self.login("admin@qaecoma.bishalkarki.xyz", "12345")
        # assert:check result
        expected_result = "Password doesnot match"
        actual_result = self.driver.find_element(By.XPATH, UserLoginLocators.Pass_Errormsg).text
        self.assertEqual(expected_result, actual_result, "Error message didnot match")

    # TS_02_TC_03 - Validate logging into the Application using incorrect E-mail and password
    def test_login_incorrect_Email_Password(self):
        self.login("121@test.com","12345")
        # assert:check result
        expected_result = "Email/Phone no. or password doesnot match"
        actual_result = self.driver.find_element(By.XPATH, UserLoginLocators.Both_Errormsg).text
        self.assertEqual(expected_result, actual_result, "Error message didnot match")







