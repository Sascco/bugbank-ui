import data
import locators
from bugbank import bugbankpage
from selenium import webdriver
from time import sleep

from tests import config
from tests.config import client_email, client_password


class bug_bank:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(config.bugBank_url)
        cls.driver.implicitly_wait(10)

    # 1 - Configurar el correo electronico en la pagina de inicio.
    def test_set_email(self, login_button=None):
        self.driver.get(config.bugBank_url)
        set_email = client_email(self.driver)
        set_password = client_password(self.driver)
        login = login_button.click_book_a_taxi_button()
