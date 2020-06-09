import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select 

chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class Loginmail(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_login_email(self):
    
    driver = self.driver
    driver.get("https://mail.google.com")
    time.sleep(1)
    user = driver.find_element_by_name('identifier')
    user.send_keys('martin.castellano@gmail.com')
    
    user.send_keys(Keys.ENTER)
    time.sleep(1)
    
    
    passw = driver.find_element_by_name('password')

    passw.send_keys('acavaelpassword')
    passw.send_keys(Keys.ENTER)

    time.sleep(3)
  
  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
 unittest.main()
