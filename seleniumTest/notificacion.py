import time #pertenece a python 
import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC



opciones = Options()
chromedriver = '/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'

class alerta(unittest.TestCase):
  
  def setUp(self):

    self.driver = webdriver.Chrome(chrome_options=opciones,executable_path=chromedriver)

  def test_alerta(self):
    
    driver = self.driver   

    

    opciones.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 2})
    driver.get('https://developer.mozilla.org/en-US/docs/Web/API/notification')

    time.sleep(3)
    
  

    
    time.sleep(5)
    driver.close()
    
if __name__ == "__main__":
 unittest.main()