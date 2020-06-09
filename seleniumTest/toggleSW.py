import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC




chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class toggle(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_toggle(self):
    
    driver = self.driver
    
    
    driver.get("https://www.w3schools.com/howto/howto_css_switch.asp") 

    toggle = driver.find_element_by_xpath('//*[@id="main"]/label[3]/div') 

    toggle.click()
    time.sleep(3)
    toggle.click()
    time.sleep(3)
    toggle.click()
    time.sleep(3)
    
   

  

  

if __name__ == "__main__":
 unittest.main()