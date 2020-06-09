import time #pertenece a python 
import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC



palabra_a_buscar= 'selenium'
chromedriver = '/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'

class sshot(unittest.TestCase):
  palabra_a_buscar= 'selenium '
  def setUp(self):

    self.driver = webdriver.Chrome(executable_path=chromedriver)

  def test_sshot(self):
    
    driver = self.driver
        
    driver.get('file:///home/martin/Downloads/Practicas/html/prompt.html')

    
    
if __name__ == "__main__":
 unittest.main()