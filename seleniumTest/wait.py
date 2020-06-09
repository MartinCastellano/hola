import time
import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 



chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class wait(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_wait(self):
    
    driver = self.driver
    
    driver.get("https://google.com")
    time.sleep(1)
    try :
         
        element = WebDriverWait(driver,10 ).until(EC.presence_of_element_located((By.NAME,"q")))
        

    finally:
        driver.quit()

    
  
  #def tearDown(self):
    #self.driver.close()

if __name__ == "__main__":
 unittest.main()

