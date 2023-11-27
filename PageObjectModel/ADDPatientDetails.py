from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddDetails:
    Name_field ='//input[@name="name"]'
    email_field ='//input[@name="email"]'
    Phone_field ='//input[@name="phone"]'
    cancelbtn ='//button/span[text()="cancel"]'
    GenerlDetailbtn ='//button/span[text()="General Details"]'

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
    def SetName(self, name):
        self.driver.find_element(By.XPATH,self.Name_field).clear()
        self.driver.find_element(By.XPATH,self.Name_field).send_keys(name)
    def SetEmail(self,emailid):
        self.driver.find_element(By.XPATH,self.email_field).clear()
        self.driver.find_element(By.XPATH,self.email_field).send_keys(emailid)
    def SetPhone(self, phonenumber):
        self.driver.find_element(By.XPATH,self.Phone_field).clear()
        self.driver.find_element(By.XPATH,self.Phone_field).send_keys(phonenumber)
    def ClickCancel(self):
        self.driver.find_element(By.XPATH,self.cancelbtn).click()
    def ClickGeneralDetails(self):
        self.driver.find_element(By.XPATH,self.GenerlDetailbtn).click()