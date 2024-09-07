from selenium.webdriver.common.by import By

class tests_bugbank:
# Landing Page
  client_email_input_box = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[1]/input')
  client_password_input_box = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[2]/div/input')
  login_button = (By.CLASS_NAME, 'login__buttons')
  register_button = (By. XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[2]')
  transfer_button = (By.ID, 'btn-TRANSFERÊNCIA')
  balance_button = (By.ID, 'btn-EXTRATO')
  balance_available = (By. ID, 'textBalance')
# Sign Up Page
  email_input_box = (By. XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input')
  customers_name = (By. XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[3]/input')
  customers_password = (By. XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input')
  customers_password_confirmation = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[5]/div/input')
  adding_balance_toggle = (By.ID, 'toggleAddBalance')
# Transfers Page
  account_number = (By.XPATH, '//*[@id="__next"]/div/div[3]/form/div[1]/div[1]/input')
  digit_number = (By.XPATH, '//*[@id="__next"]/div/div[3]/form/div[1]/div[2]/input')
  ammount_to_transfer = (By.XPATH, '//*[@id="__next"]/div/div[3]/form/div[2]/input')
  transfer_now_button = (By. XPATH, '//*[@id="__next"]/div/div[3]/form/button')
  go_back_button = (By. ID, 'btnBack')
# Balance Page
  go_back_button_balance_page = (By.ID, 'btnBack')
