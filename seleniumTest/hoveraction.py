import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC






chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class raton(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_ratoncito(self):
    
    driver = self.driver    
    
    driver.get("https://www.google.com")

    elemento = driver.find_element_by_link_text('Privacidad')

    time.sleep(3)
    
    hover = ActionChains(driver)
    hover.move_to_element(elemento)
    hover.click().perform()
    time.sleep(3)
    driver.back()
    time.sleep(2)
     

        
   

        
    
  

if __name__ == "__main__":
 unittest.main()