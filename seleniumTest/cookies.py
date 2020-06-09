import time #pertenece a python 
import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC




chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class cookies(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_cookies(self):
    
    driver = self.driver
    
    
    driver.get("https://www.ted.com")

       
    time.sleep(2)
    # solo imprime las cookies de la pagina
    cookies = driver.get_cookies()
    # se popdran agragar cookies con driver.add_cookies(cookie) donde por ej. cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’} 
    print(cookies)

  
     
        

  

if __name__ == "__main__":
 unittest.main()
