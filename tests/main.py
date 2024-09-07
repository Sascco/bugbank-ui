from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from config import bugBank_url

class TestClass:
  def setUp(self):
    chrome_driver_path = r"C:\Users\Sascc\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    self.driver = webdriver.Chrome(service=service)

  def test_setting_credentials(self):
    self.driver.get(bugBank_url)
    sleep(5)  # Let the page load for 5 seconds

  def tearDown(self):
    self.driver.quit()


test_instance = TestClass()
test_instance.setUp()
test_instance.setting_credentials()
test_instance.tearDown()

