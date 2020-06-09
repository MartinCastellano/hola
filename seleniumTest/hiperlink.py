import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC




chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class hiperlink(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_hiperlink(self):
    
    driver = self.driver    
    
    driver.get("https://www.w3schools.com/") 

    element = driver.find_element_by_link_text('Learn PHP') 

    element.click()

    time.sleep(3)
    

    
    

    

  

if __name__ == "__main__":
 unittest.main()
