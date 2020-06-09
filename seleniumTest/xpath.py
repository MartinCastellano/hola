import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select 

chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class xpath(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_xpath(self):
    
    driver = self.driver
    driver.get("https://google.com")
    time.sleep(1)

    self.assertIn('Google', driver.title)

    xpath = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    xpath.send_keys('hola mundo',Keys.ARROW_DOWN)
    xpath.send_keys(Keys.ENTER)

    time.sleep(3)

    
    
    assert "no se encontro la palabra " not in driver.page_source
  
  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
 unittest.main()