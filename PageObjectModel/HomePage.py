from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:
    menu = '//ul[@class ="MuiList-root MuiList-padding"]/a'
    Patientmenu_btn ='//ul[@class ="MuiList-root MuiList-padding"]/a//span[text()="Patients"]'
    Addpatentbtn ='//button/span[text()="Add Patient"]'
    todo_list = '//ul[@ aria-label="completed todo"]//li'
    unchecked_todo = '//ul[@ aria-label="completed todo"]//li//input[@ type="checkbox"]'
    view_todo = '//ul[@ aria-label="completed todo"]//li//span[text()="view"]'
    todo_add_button = '//div/a//span[text()="Add"]'
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
    def clickPatientmenubtn(self):
        self.driver.find_element(By.XPATH,self.Patientmenu_btn).click()
    def clickAddPatientbtn(self):
        self.driver.find_element(By.XPATH,self.Addpatentbtn).click()
