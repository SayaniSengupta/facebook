import time
from config.con import TestData
from pageobject.login import LoginPage
from pageobject.logout import LogoutPage
from pageobject.privacysetting import Privacy
from utilities.Basepage import BasePage


class Test_e2e(BasePage):

    def test_verify_LoginPage_title(self):
        """
        verify login page title is matched or not

        """
        self.driver.implicitly_wait(10)
        login_page_title = self.driver.title
        # to verify loginPage title
        assert login_page_title == TestData.LOGIN_PAGE_TITLE
        self.message_logging("title verified succesfully")

    def test_login(self, param):
        """
        login in facebook

        """
        # creating object of method
        login_page = LoginPage(self.driver)
        # to enter username and password
        login_page.user_name().send_keys(param['email'])
        login_page.password().send_keys(param['password'])
        login_page.login_button()
        self.message_logging("login successfully")

    def test_verify_profilePage_title(self):
        """
        verify title of profile page
        """
        profile_page_title = self.driver.title
        # to verify profile page title after login
        assert profile_page_title == TestData.PROFILE_PAGE_TITLE
        self.message_logging("profile page title verified")

    def test_verify_profile_name(self):
        """
        verify profile name is matched or not
        """
        # creating object of method
        profilePage = Privacy(self.driver)
        # to verify profile name
        time.sleep(2)
        name = profilePage.profile_name().text
        assert name == TestData.PROFILE_NAME
        self.message_logging("profile name verified successfully")

    def test_settings(self):
        """
           going to settings page to get total blocked account number
           going to manage profile and get the number then checked the number
           matched or not
        """
        # creating object of method
        setting_page = Privacy(self.driver)
        setting_page.click_account()
        self.wait_clickable(Privacy.SETTING_PRIVACY)
        setting_page.click_settings_privacy()
        self.wait_clickable(Privacy.SETTING)
        setting_page.click_setting()
        setting_page.click_privacy()
        time.sleep(2)
        setting_page.click_manage_profile()
        time.sleep(2)
        ph = setting_page.click_number_verify()  # get the phone number
        self.message_logging(ph.text)
        assert ph.text == '079981 62391'
        self.message_logging(ph.text)
        self.message_logging("mobile number verified successfully")
        self.driver.back()
        setting_page.click_blocking()
        setting_page.click_edit()
        setting_page.click_blockedList()
        # to get list of blocked user
        total_no_blocks = setting_page.blocks()
        blocks = len(total_no_blocks)
        self.message_logging(f"total number of blocked users {blocks}")
        setting_page.close_list().click()  # to close block page list
        self.message_logging("successfully got the total number of blocked users")

    def test_logout(self):
        """ logout from facebook """
        # creating object of method
        logout_obj = LogoutPage(self.driver)
        logout_obj.account()
        logout_obj.logout()
        self.message_logging("logout successfully")
