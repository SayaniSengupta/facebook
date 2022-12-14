from selenium.webdriver.common.by import By


class LogoutPage:
    ACCOUNT = (By.XPATH, "(//div[@class='aglvbi8b om3e55n1 i8zpp7h3 g4tp4svg'])[1]")
    LOGOUT = (By.XPATH, "//span[text()='Log Out']")

    def __init__(self, driver):
        self.driver = driver

    def account(self):
        """
          click on account
        """
        self.driver.find_element(*LogoutPage.ACCOUNT).click()

    def logout(self):
        """
            click on logout
        """
        return self.driver.find_element(*LogoutPage.LOGOUT).click()
