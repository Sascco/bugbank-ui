
import config
import locators
# from locators import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class bugbankpage:

  def __init__(self, driver):
    self.driver = driver

  def client_email(self, locators):  # input field client email
    self.driver.find_element(*locators.client_email_input).send_keys(*config.client_email)

  def client_password(self, locators):  # input field client password
    self.driver.find_element(*locators.client_password).send_keys(*config.client_password)

  def login_button(self, locators):
    self.driver.find_element(*locators.login_button).click()
