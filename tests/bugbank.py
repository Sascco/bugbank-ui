import config


class BugBankPage:

  def __init__(self, driver):
    self.driver = driver

  def click_client_email(self, locators):  # click on input field client email
    self.driver.find_element(*locators.client_email_input).click()

  def client_email(self, locators):  # input field client email
    self.driver.find_element(*locators.client_email_input).send_keys(config.client_email)

  def click_client_password(self, locators):  #click on input field client password
    self.driver.find_element(*locators.client_password).click()

  def client_password(self, locators):  # input field client password
    self.driver.find_element(*locators.client_password).send_keys(config.client_password)

  def login_button(self, locators):
    self.driver.find_element(locators.login_button).click()
