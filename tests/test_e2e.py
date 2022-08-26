import time
from config.con import TestData
from pageobject.login import LoginPage
from pageobject.logout import LogoutPage
from pageobject.privacysetting import Privacy
from utilities.Basepage import BasePage


class Test_e2e(BasePage):

    def test_verify_LoginPage_title(self):
        """verify login page title is matched or not"""
        self.driver.implicitly_wait(10)
        login_page_title = self.driver.title
        # to verify loginPage title
        assert login_page_title == TestData.LOGIN_PAGE_TITLE
        self.message_logging("title verified succesfully")

    def test_login(self, param):
        """ login in facebook """
        login_page = LoginPage(self.driver)
        # to enter username and password
        login_page.user_name().send_keys(param['email'])
        login_page.password().send_keys(param['password'])
        login_page.login_button()
        self.message_logging("login successfully")

    def test_verify_profilePage_title(self):
        profile_page_title = self.driver.title
        # to verify profile page title after login
        assert profile_page_title == TestData.PROFILE_PAGE_TITLE
        self.message_logging("profile page title verified")

    def test_verify_profile_name(self):
        """ verify profile name is matched or not"""
        profilePage = Privacy(self.driver)
        # to verify profile name
        name = profilePage.profile_name().text
        assert name == TestData.PROFILE_NAME
        self.message_logging("profile name verified successfully")

    def test_settings(self):
        """going to settings page to get total blocked account number
           going to manage profile
        """
        setting_page = Privacy(self.driver)
        # to click on account
        setting_page.click_account().click()
        # to click on settings and privacy
        self.wait_clickable(Privacy.SETTING_PRIVACY)
        setting_page.click_settings_privacy().click()
        # to click on settings
        self.wait_clickable(Privacy.SETTING)
        setting_page.click_setting().click()
        setting_page.click_privacy().click()  # to click on privacy
        time.sleep(2)
        setting_page.click_manage_profile().click()  # click on manage profile
        time.sleep(2)
        ph = setting_page.click_number_verify()  # get the phone number
        self.message_logging(ph.text)
        assert ph.text == '079981 62391'
        # assert ph.text == '076765 99764'
        self.message_logging("mobile number verified successfully")
        self.driver.back()
        setting_page.click_blocking().click()  # to click blocking
        setting_page.click_edit().click()  # to click on edit button
        # to click on blocked list
        setting_page.click_blockedList().click()
        # to get list of blocked user
        total_no_blocks = setting_page.blocks()
        blocks = len(total_no_blocks)
        self.message_logging(f"total number of blocked users {blocks}")
        setting_page.close_list().click()  # to close block page list
        self.message_logging("successfully got the total number of blocked users")

    def test_logout(self):
        """ logout from facebook """
        logout_obj = LogoutPage(self.driver)
        logout_obj.account().click()  # click on account
        logout_obj.logout().click()  # click on logout
        self.message_logging("logout successfully")
