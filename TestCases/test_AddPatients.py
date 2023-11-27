import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import allure
from  PageObjectModel import ADDPatientDetails
from PageObjectModel.ADDPatientDetails import AddDetails
from PageObjectModel.HomePage import Homepage
from PageObjectModel.LoginPage import Loginpage, invalidlogindetail
from Utilities.customLogger import logGen
from Utilities.readProperties import readConfig
from Utilities import XLutilities
from time import sleep

class Test_AddPatient:
    # baseURL= 'https://gor-pathology.web.app/'
    baseURL = readConfig.getApplicationURL()
    logger = logGen.logGen()
    path = 'Testdata/patientsDetail.xlsx'

    # def test_Patientmenubutton(self, setup):
    #     self.logger.info(" *********** Verifing Logout button *********** ")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.LP = Loginpage(self.driver)
    #     self.LP.EnterEmail()
    #     self.LP.EnterPassword()
    #     self.LP.ClickLoginbutton()
    #     sleep(5)
    #     self.HP = Homepage(self.driver)
    #     self.HP.clickPatientmenubtn()
    #     Page_title = self.driver.find_element(By.XPATH,'//div[@class="title"]').text
    #
    #     if 'Patient' in Page_title:
    #         assert True
    #         self.driver.close()
    #         self.logger.info(" *********** Patients menu button TestCase Passed *********** ")
    #     else:
    #         self.driver.save_screenshot("D:\pythonProject\Screenshots\\" + "test_loginPageURL.png")
    #         allure.attach(self.driver.get_screenshot_as_png(), name="test_loginPageURL.png",attachment_type=AttachmentType.PNG)
    #         self.driver.close()
    #         self.logger.error(" *********** Patients menu button TestCase Failed *********** ")
    #         assert False
    # def test_ADDPatientbutton(self, setup):
    #     self.logger.info(" *********** Verifing Logout button *********** ")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.LP = Loginpage(self.driver)
    #     self.LP.EnterEmail()
    #     self.LP.EnterPassword()
    #     self.LP.ClickLoginbutton()
    #     sleep(5)
    #     self.HP = Homepage(self.driver)
    #     self.HP.clickPatientmenubtn()
    #     sleep(3)
    #     self.HP.clickAddPatientbtn()
    #     sleep(2)
    #     Page_url = self.driver.current_url
    #
    #     if 'add' in Page_url:
    #         assert True
    #         self.driver.close()
    #         self.logger.info(" *********** Patients menu button TestCase Passed *********** ")
    #     else:
    #         self.driver.save_screenshot("D:\pythonProject\Screenshots\\" + "test_loginPageURL.png")
    #         allure.attach(self.driver.get_screenshot_as_png(), name="test_loginPageURL.png",attachment_type=AttachmentType.PNG)
    #         self.driver.close()
    #         self.logger.error(" *********** Patients menu button TestCase Failed *********** ")
    #         assert False
    def test_ADDPatientdetails(self, setup):
        self.logger.info(" *********** Verifing Logout button *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.LP.EnterEmail()
        self.LP.EnterPassword()
        self.LP.ClickLoginbutton()
        sleep(5)
        self.HP = Homepage(self.driver)
        self.HP.clickPatientmenubtn()
        sleep(3)
        self.HP.clickAddPatientbtn()
        sleep(2)
        self.PD = AddDetails(self.driver)
        self.rows = XLutilities.getRowCount(self.path,'Sheet1')
        status_list = []
        for r in range(2,self.rows+1):
            self.name = XLutilities.readData(self.path,'Sheet1',r,1)
            self.emailid = XLutilities.readData(self.path,'Sheet1',r,2)
            self.phonenumber = XLutilities.readData(self.path, 'Sheet1', r, 3)
            self.PD.SetName(self.name)
            sleep(1)
            self.PD.SetEmail(self.emailid)
            sleep(2)
            self.PD.SetPhone(self.phonenumber)
            user_name = self.driver.find_element(By.XPATH, '//input[@name="name"]').text

            self.PD.ClickGeneralDetails()
            sleep(3)

            added_name = self.driver.find_element(By.XPATH,'//h5[contains(text(),"Secondary details")]').text

            if user_name is added_name:
                assert True
                self.driver.close()
                self.logger.info(" *********** Add Patients TestCase Passed *********** ")
            else:
                self.driver.save_screenshot("D:\pythonProject\Screenshots\\" + "test_loginPageURL.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_loginPageURL.png",attachment_type=AttachmentType.PNG)
                self.driver.close()
                self.logger.error(" *********** Add Patients button TestCase Failed *********** ")
                assert False
