import time

from selenium.webdriver.common.by import By

from Locators.Locater import UserReg

class UserPage:
    def __init__(self, driver):
        self.driver = driver
        self.location = UserReg

    def signIn_locator(self):
        signin = self.driver.find_element(By.XPATH, self.location.navSignin)
        return signin


    def signin_click(self):
        self.signIn_locator().click()


    def EntryEmail_locator(self):
        emailfirst = self.driver.find_element(By.ID, self.location.emailFirst_id)
        return emailfirst

    def emailkeys(self, femail):
        self.EntryEmail_locator().send_keys(femail)

    def createacc_Locator(self):
        createaccount = self.driver.find_element(By.ID, self.location.createAccount)
        return createaccount

    def createacc_click(self):
        self.createacc_Locator().click()
        self.driver.implicitly_wait(10)

    def firstname_Locator(self):
        firstname = self.driver.find_element(By.ID, self.location.firstName)
        return firstname

    def firstname_sendkey(self,fname):
        self.firstname_Locator().send_keys(fname)
        time.sleep(2)

    def Lastname_Locator(self):
        lastname = self.driver.find_element(By.ID, self.location.lastName)
        return lastname

    def lastname_sendkey(self, lname):
        self.Lastname_Locator().send_keys(lname)
        time.sleep(2)

    def email_locator(self):
        Email = self.driver.find_element(By.ID, self.location.email)
        Email.clear()
        return Email

    def email_sendkey(self, email):
        self.email_locator().send_keys(email)
        time.sleep(2)

    def pass_locator(self):
        passw = self.driver.find_element(By.ID, self.location.password)
        return passw

    def pass_sendkey(self, paaw):
        self.pass_locator().send_keys(paaw)
        time.sleep(2)

    def buttonRegister_locator(self):
        button_register = self.driver.find_element(By.ID, self.location.registerButton)
        return button_register

    def button_click(self):
        self.buttonRegister_locator().click()
        time.sleep(2)

    def registration(self,femail,fname,lname,email,paaw):
        driver = self.driver
        self.signin_click()
        self.emailkeys(femail)
        self.createacc_click()
        driver.implicitly_wait(10)
        self.firstname_sendkey(fname)
        time.sleep(2)
        self.lastname_sendkey(lname)
        time.sleep(2)
        self.email_sendkey(email)
        time.sleep(2)
        self.pass_sendkey(paaw)
        time.sleep(2)
        self.button_click()
        time.sleep(2)

