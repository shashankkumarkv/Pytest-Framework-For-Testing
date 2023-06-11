import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Page_Objects.BasePage import BasePage


class LoginPage(BasePage):
    url = "https://practicetestautomation.com/practice-test-login/"
    username_locator = (By.XPATH, "//*[@id='username']")
    password_locator = (By.XPATH, "//*[@id='password']")
    submit_button = (By.XPATH, "//*[@id='submit']")
    expectedTitle = "Logged In Successfully | Practice Test Automation"

    def __init__(self, driver=WebDriver):
        super().__init__(driver)

    def openUrl(self):
        self.driverGet(self.url)

    def login(self, username, password):
        self.findElementBy(self.username_locator).send_keys(username)
        time.sleep(2)
        self.findElementBy(self.password_locator).send_keys(password)
        time.sleep(2)
        self.findElementBy(self.submit_button).click()

    def verifyTitle(self):
        self.verifyLogin(expectedTitle=self.expectedTitle)



