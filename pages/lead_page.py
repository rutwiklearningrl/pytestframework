
from selenium.webdriver.common.by import By


class LeadPage:

    def __init__(self, driver):
        self.driver = driver

        self.elm_tb_lastname =(By.NAME, "lastname")
        self.elm_tb_company = (By.NAME,"company")
        self.elm_btn_save = (By.NAME,"button")
        self.elm_lbl_text_lastname = (By.XPATH, "//td[text()='Last Name:']/following::td[text()='Modi']")
        self.elm_lbl_text_company = (By.XPATH, "//td[text()='Company:']/following::td[text()='BJP']")






    def create_lead(self,lname,company):
        self.setLastname(lname)
        self.setCompany(company)
        self.clickSave()

    def setLastname(self,lname):
        self.driver.find_element(*self.elm_tb_lastname).send_keys(lname)

    def setCompany(self,company):
        self.driver.find_element(*self.elm_tb_company).send_keys(company)

    def clickSave(self):
        self.driver.find_element(*self.elm_btn_save).click()

    def verify_label_lastname(self,lname):
        return self.driver.find_element(By.XPATH,"//td[text()='Last Name:']/following::td[text()='"+lname+"']").is_displayed()

    def verify_label_company(self,comp):
        return self.driver.find_element(By.XPATH,"//td[text()='Company:']/following::td[text()='"+comp+"']").is_displayed()




