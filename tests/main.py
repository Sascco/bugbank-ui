from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from config import bugBank_url

class TestClass:
  def setUp(self):
    # Correct the path to your ChromeDriver
    chrome_driver_path = r"C:\Users\Sascc\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"

    # Create a Service object to pass the path to ChromeDriver
    service = Service(executable_path=chrome_driver_path)

    # Initialize the Chrome driver with the Service object
    self.driver = webdriver.Chrome(service=service)

  def test_set_route(self):
    # Open the website
    self.driver.get(bugBank_url)  # Replace with your desired URL
    sleep(5)  # Let the page load for 5 seconds

  def tearDown(self):
    # Once the tests are done, the browser shuts down
    self.driver.quit()


# Instantiate and run the test
test_instance = TestClass()
test_instance.setUp()
test_instance.test_set_route()
test_instance.tearDown()

