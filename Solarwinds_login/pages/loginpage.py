from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from Solarwinds_login.utilities.handy_wrappers import HandyWrappers
from Solarwinds_login.utilities.explicit_wait import ExplicitWaitType
import time

class solarwin_login():
    baseUrl = "https://solarwinds.vmware.com/"
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    global wait
    wait = ExplicitWaitType(driver)
    global hw
    hw = HandyWrappers(driver)
    driver.get(baseUrl)
    def test(self):
        login_element_state,login_username = hw.isElementPresent("//div[@id='dialog']/input[@name='ctl00$BodyContent$Username']", By.XPATH)
        if login_username == 'None found':
            print("login_element_state" + ' ' + str(login_element_state))
        else:
            login_username.send_keys('vmwarem\yc')

        password_element_state,login_password = hw.isElementPresent("//div[@id='dialog']/div[@class='sw-password-box']/input[@name='ctl00$BodyContent$Password']", By.XPATH)
        if login_password == 'None found':
            print("password_element_state" + ' ' + str(password_element_state))
        else:
            login_password.send_keys('Yasodha3@mithra')
        try:
            login_btn = driver.find_element_by_link_text("LOGIN")
            login_btn.click()
            time.sleep(2)
            driver.save_screenshot("C:\\Users\\yc\\workspace_python\\Scheduled_tests\\Solarwinds_login\\allure_reports\\login.png")
        except:
            driver.save_screenshot("C:\\Users\\yc\\workspace_python\\Scheduled_tests\\Solarwinds_login\\allure_reports\\login.png")
        return driver;

