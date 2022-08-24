from selenium.webdriver.common.by import By
from utilities.Basepage import BasePage


class Privacy(BasePage):
    PROFILE_NAME = (By.XPATH, "//span[text()='Sayani']")

    ACCOUNT = (By.XPATH, "(//div[@class='aglvbi8b om3e55n1 i8zpp7h3 g4tp4svg'])[1]")
    SETTING_PRIVACY = (By.XPATH, "//span[text()='Settings & privacy']")
    SETTING = (By.XPATH, "//span[text()='Settings']")
    PRIVACY = (By.XPATH, "//span[text()='Privacy']")
    MANAGE_PROFILE = (By.XPATH, "//div[normalize-space()='Manage your profile']")
    NUMBER_VERIFY = (By.XPATH, "(//div[@class='n3t5jt4f oog5qr5w k1z55t6l pbevjfx6 laatuukc'])[3]")
    BLOCKING = (By.XPATH, "//span[text()='Blocking']")
    EDIT = (By.XPATH, "(//span[normalize-space()='Edit'])[3]")
    BLOCKEDLIST = (By.XPATH, "//span[text()='See your blocked list']")
    TOTAL_NO_BLOCKS = (By.XPATH, "//div[@class='h8391g91 m0cukt09 kpwa50dg ta68dy8c b6ax4al1']")
    CLOSE_LIST = (By.XPATH, "//div[@class='b0ur3jhr facqkgn9 s8sjc6am h28iztb5']")

    def __init__(self, driver):
        self.driver = driver

    def profile_name(self):
        return self.driver.find_element(*Privacy.PROFILE_NAME)

    def __init__(self, driver):
        self.driver = driver

    def click_account(self):
        return self.driver.find_element(*Privacy.ACCOUNT)

    def click_settings_privacy(self):
        return self.driver.find_element(*Privacy.SETTING_PRIVACY)

    def click_setting(self):
        return self.driver.find_element(*Privacy.SETTING)

    def click_privacy(self):
        return self.driver.find_element(*Privacy.PRIVACY)

    def click_manage_profile(self):
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])
        return self.driver.find_element(*Privacy.MANAGE_PROFILE)

    def click_number_verify(self):
        return self.driver.find_element(*Privacy.NUMBER_VERIFY)

    def click_blocking(self):
        return self.driver.find_element(*Privacy.BLOCKING)

    def click_edit(self):
        return self.driver.find_element(*Privacy.EDIT)

    def click_blockedList(self):
        return self.driver.find_element(*Privacy.BLOCKEDLIST)

    def blocks(self):
        count = self.driver.find_elements(*Privacy.TOTAL_NO_BLOCKS)
        return count

    def close_list(self):
        return self.driver.find_element(*Privacy.CLOSE_LIST)
