import time

import pytest
from selenium import webdriver

from pages.lead_page import LeadPage
from pages.home_page import HomePage
from pages.login_page import LoginPage







# def launchApp():
#     driver = webdriver.Chrome()
#     driver.get("http://localhost:100")
#     return driver


def test_verify_title_TC01(driver):
   # driver = launchApp()
    lp = LoginPage(driver)
    istitle = lp.verifyTitle()
    assert "123vtiger CRM - Commercial Open Source CRM" == istitle



def test_invalid_login_TC04(driver):
    lp = LoginPage(driver)
    lp.login( "admin123", "admin23222")
    assert lp.verifyErrorMsg() == True


def test_create_lead_with_mandatory_fields(driver):
    lp = LoginPage(driver)
    lp.login("admin", "admin")
    hp = HomePage(driver)
    hp.clickNewLead()
    ldp = LeadPage(driver)
    ldp.create_lead("Kejariwal","AAP")
    assert ldp.verify_label_lastname("Kejariwal123") == True
    assert ldp.verify_label_company("AAP") == True
    hp.clickLogout()









