import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC




chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class alerta(unittest.TestCase):
  
  def setUp(self):

    self.driver = webdriver.Chrome(executable_path=chromedriver)

  def test_alerta(self):
    
    driver = self.driver
        
    driver.get('file:///home/martin/Downloads/python/htlm/alerta.html')

    time.sleep(3)

    alerta = driver.find_element_by_name("alert")

    alerta.click()

    alerta.switch_to_alert()
    time.sleep(3)
    alerta.dismiss()

    driver.close()
    
if __name__ == "__main__":
 unittest.main()