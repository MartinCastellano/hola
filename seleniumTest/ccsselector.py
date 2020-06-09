import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC




chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class css(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_css(self):
    
    driver = self.driver    
    
    driver.get("https://www.w3schools.com/html/default.asp") 

    element = driver.find_element_by_css_selector('a.w3-blue') 

    element.click()

    time.sleep(3)
    

    
    

    

  

if __name__ == "__main__":
 unittest.main()
