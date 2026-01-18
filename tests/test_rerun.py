import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.flaky(reruns=2)
def test_unstable(setup):
    assert 2==3



def test_verify_logo_TC02(driver):
    #driver = launchApp()
    lp = LoginPage(driver)
    islogo = lp.verifyLogo()
    assert islogo == True


def test_valid_login_TC03(driver):
    #driver = launchApp()
    lp = LoginPage(driver)
    lp.login("admin","admin")
    hp = HomePage(driver)
    assert hp.verifyLogout() == True

