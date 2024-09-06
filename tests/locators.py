
from selenium.webdriver.common.by import By

class tests_bugbank:
  client_email_input = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[1]/input')
  client_password_input = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[2]/div/input')
  login_button = (By.CLASS_NAME, 'login__buttons')
