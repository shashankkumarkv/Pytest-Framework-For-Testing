from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest


#@pytest.fixture(params=["chrome", "firefox"]) ##for multiple browser
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser") ##for single browser
    #browser = request.param
    print(f"Opening {browser} browser")
    if browser == "chrome":
        myDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        myDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"expected chrome of firefox got {browser}")
    yield myDriver
    print(f"closing {browser} browser")
    myDriver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="test execute on chrome or firefox"
    )
