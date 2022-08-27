from selenium.webdriver.common.by import By

from config.con import TestData


class LoginPage:
    USER_NAME = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log In']")

    def __init__(self, driver):
        self.driver = driver

    def user_name(self):
        """
          method to get the username
        """
        return self.driver.find_element(*LoginPage.USER_NAME)

    def password(self):
        """
          method to get the password
        """
        return self.driver.find_element(*LoginPage.PASSWORD)

    def login_button(self):
        """
         method to click on login button
        """
        return self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()

