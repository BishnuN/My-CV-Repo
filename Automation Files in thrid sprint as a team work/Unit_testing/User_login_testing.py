import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

class UserLoginLocators:
    signin = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    signout = '//*[@id="header"]/div[2]/div/div/nav/div[2]/a'
    email = 'email'
    password = 'passwd'
    Login_Button = 'SubmitLogin'
    UsernameText = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span'
    ErrorMsg = '//*[@id="center_column"]/div[1]/p'

class UserLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qaecoma.bishalkarki.xyz/")

    def tearDown(self):
        self.driver.close()

    def login(self, username, password):
        driver = self.driver
        nav_signin = driver.find_element(By.XPATH, UserLoginLocators.signin)
        nav_signin.click()
        time.sleep(2)
        nav_email = driver.find_element(By.ID, UserLoginLocators.email)
        nav_email.send_keys(username)
        time.sleep(2)
        upass = driver.find_element(By.ID, UserLoginLocators.password)
        upass.send_keys(password)
        time.sleep(2)
        nav_signin1 = driver.find_element(By.ID, UserLoginLocators.Login_Button)
        nav_signin1.click()
        time.sleep(5)

    # TS_01_TC_01 - Valid login testing with correct email and password
    def test_login_success(self):
        driver = self.driver
        self.login("saru73@yopmail.com", "12345")
        expected_result ="Sign out"
        actual_result = driver.find_element(By.XPATH, UserLoginLocators.signout).text
        self.assertEqual(expected_result, actual_result, "test_login_success passed")

    # TS_o4_TC_01- Verify that the user profile (image and username) is displayed in the right corner after successful login
    def test_User_profile(self):
        driver = self.driver
        self.login("saru73@yopmail.com", "12345")
        # assert:check result
        expected_result = "Saru gyawali"
        actual_result = driver.find_element(By.XPATH, UserLoginLocators.UsernameText).text
        self.assertEqual(expected_result, actual_result, "test_User_profile passed")

    # TS_02_TC_01 - Validate logging into the Application using incorrect credentials by using E-mail
    def test_login_invalid_email(self):
        self.login("121@test.com","12345")
        #assert:check result
        expected_result ="There is 1 error"
        actual_result = self.driver.find_element(By.XPATH, UserLoginLocators.ErrorMsg).text
        self.assertEqual(expected_result, actual_result, "test_login_invalid_email passed")

    # TS_03_TC_01 - Validate login button  when the E-mail field is left empty
    def test_login_empty_email(self):
        self.login("", "12345")
        # assert:check result
        expected_result = "There is 1 error"
        actual_result = self.driver.find_element(By.XPATH, UserLoginLocators.ErrorMsg).text
        self.assertEqual(expected_result, actual_result, "test_login_empty_email passed")

    # TS_03_TC_02 - Validate login button when the Password field is left empty
    def test_login_empty_password(self):
        self.login("saru73@yopmail.com","")
        # assert:check result
        expected_result = "There is 1 error"
        actual_result = self.driver.find_element(By.XPATH, UserLoginLocators.ErrorMsg).text
        self.assertEqual(expected_result, actual_result, "test_login_empty_password passed")

    # TS_03_TC_03- Validate login button  when Email and password both are left empty
    def test_login_empty_email_and_password(self):
        self.login("","")
        # assert:check result
        expected_result = "There is 1 error"
        actual_result = self.driver.find_element(By.XPATH, UserLoginLocators.ErrorMsg).text
        self.assertEqual(expected_result, actual_result, "test_login_empty_email_and_password passed")





