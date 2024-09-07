import locators
from selenium import webdriver
from tests import config
from tests.bugbank import BugBankPage
from tests.config import client_email, client_password


class BugBank:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(config.bugBank_url)
        cls.driver.implicitly_wait(15)

    # 1 - Setting up client information on landing page.
    def setting_credentials(self):
        self.driver.get(config.bugBank_url)           #Open website on browser
        bank_page = BugBankPage(self.driver)          #
        set_email = client_email(self.driver)         #Add customers email
        set_password = client_password(self.driver)   #Add customers password
        #login = login_button (self.driver)           #Click on Login

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()
