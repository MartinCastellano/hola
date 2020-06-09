
#espera cierto tiempo para q se cargue un contenido con un tiempo especifico similar a usar time
import time #pertenece a python 
import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 



chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class implicitwait(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_implicitwait(self):
    
    driver = self.driver
    driver.implicitly_wait(10)
    
    driver.get("https://google.com")

    myDinamicelement = driver.find_element_by_name('q')
    
    

    
  
  #def tearDown(self):
    #self.driver.close()

if __name__ == "__main__":
 unittest.main()

