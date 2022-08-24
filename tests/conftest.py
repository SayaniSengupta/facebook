import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config.con import TestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption("--email", action="store", default="email")
    parser.addoption("--password", action="store", default="password")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    if browser_name == "chrome":
        service_obj = Service(TestData.chrome_executablepath)
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    driver.get(TestData.baseUrl)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


