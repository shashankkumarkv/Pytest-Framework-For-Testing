import time
import pytest
from Page_Objects.LoginPage import LoginPage


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.parametrize("username, password", [("student", "Password123")])
    def testLogins(self, driver, username, password):
        loginPage = LoginPage(driver)
        loginPage.openUrl()
        time.sleep(2)
        loginPage.login(username=username, password=password)
        time.sleep(5)
        loginPage.verifyTitle()
