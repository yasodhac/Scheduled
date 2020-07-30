import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Solarwinds_login.utilities.handy_wrappers import HandyWrappers
from Solarwinds_login.utilities.explicit_wait import ExplicitWaitType
from Solarwinds_login.pages.loginpage import solarwin_login
import allure
import time

@allure.severity(allure.severity_level.NORMAL)
class TestClassDemo():
    ff = solarwin_login()
    global driver
    driver = ff.test()
    driver.implicitly_wait(2)
    hw = HandyWrappers(driver)
    wait = ExplicitWaitType(driver)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        allure.attach.file('C:\\Users\\yc\\workspace_python\\Scheduled_tests\\Solarwinds_login\\allure_reports\\login.png', name='Login Status', attachment_type=allure.attachment_type.PNG)
        logo_check = (self.wait).waitForElement("img[alt='Go To Orion Home']",locatorType="css")
        logo_check_state = logo_check.is_displayed()
        print(logo_check_state)
        assert logo_check_state == True
        driver.close()

