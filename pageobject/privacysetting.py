from selenium.webdriver.common.by import By
from utilities.Basepage import BasePage


class Privacy(BasePage):
    PROFILE_NAME = (By.XPATH, "//span[text()='Sayani']")

    ACCOUNT = (By.XPATH, "(//div[@class='aglvbi8b om3e55n1 i8zpp7h3 g4tp4svg'])[1]")
    SETTING_PRIVACY = (By.XPATH, "//span[text()='Settings & privacy']")
    SETTING = (By.XPATH, "//span[text()='Settings']")
    PRIVACY = (By.XPATH, "//span[text()='Privacy']")
    MANAGE_PROFILE = (By.XPATH, "//div[normalize-space()='Manage your profile']")
    NUMBER = (By.XPATH, "(//div[@class='n3t5jt4f oog5qr5w k1z55t6l pbevjfx6 laatuukc'])[3]")
    BLOCKING = (By.XPATH, "//span[text()='Blocking']")
    EDIT = (By.XPATH, "(//span[normalize-space()='Edit'])[3]")
    BLOCKEDLIST = (By.XPATH, "//span[text()='See your blocked list']")
    TOTAL_NO_BLOCKS = (By.XPATH, "//div[@class='h8391g91 m0cukt09 kpwa50dg ta68dy8c b6ax4al1']")
    CLOSE_LIST = (By.XPATH, "//div[@class='b0ur3jhr facqkgn9 s8sjc6am h28iztb5']")

    def __init__(self, driver):
        self.driver = driver

    def profile_name(self):
        """
            return profile name
        """
        return self.driver.find_element(*Privacy.PROFILE_NAME)

    def click_account(self):
        """
        click on account
        """
        self.driver.find_element(*Privacy.ACCOUNT).click()

    def click_settings_privacy(self):
        """
        click on settings and privacy
        """

        self.driver.find_element(*Privacy.SETTING_PRIVACY).click()

    def click_setting(self):
        """
        click on settings
        """
        return self.driver.find_element(*Privacy.SETTING).click()

    def click_privacy(self):
        """
        click on privacy
        """
        return self.driver.find_element(*Privacy.PRIVACY).click()

    def click_manage_profile(self):
        """
        click on manage profile
        """
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])  # switch to iframe
        return self.driver.find_element(*Privacy.MANAGE_PROFILE).click()

    def click_number_verify(self):
        """
        return phone number of the profile
        """
        return self.driver.find_element(*Privacy.NUMBER)

    def click_blocking(self):
    def click_blocking(self):
        self.driver.find_element(*Privacy.BLOCKING).click()

    def click_edit(self):
        """
        click on blocking
        """
        self.driver.find_element(*Privacy.EDIT).click()

    def click_blockedList(self):
        """
         click on blocked list
        """
        self.driver.find_element(*Privacy.BLOCKEDLIST).click()

    def blocks(self):
        """
        return total number of blocked accounts
        """
        return self.driver.find_elements(*Privacy.TOTAL_NO_BLOCKS)

    def close_list(self):
        """
        close the list
        """
        return self.driver.find_element(*Privacy.CLOSE_LIST)
