from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.elm_lnk_logout =(By.LINK_TEXT, "Logout")
        self.elm_lnk_newlead = (By.LINK_TEXT, "New Lead")

    def verifyLogout(self):
        return self.driver.find_element(*self.elm_lnk_logout).is_displayed()

    def clickLogout(self):
        self.driver.find_element(*self.elm_lnk_logout).click()

    def clickNewLead(self):
        self.driver.find_element(*self.elm_lnk_newlead).click()