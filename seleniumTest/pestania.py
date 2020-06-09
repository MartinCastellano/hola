#! python2
import time #pertenece a python 
import unittest
from selenium import webdriver

import HtmlTestRunner


# from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options #para segundo plano
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


brave  = '/usr/bin/brave-browser'

chromedriver = '/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'

option = webdriver.ChromeOptions()
Options = Options()
Options.add_argument('--headless')
option.binary_location = brave

def change_text(text):
    return text.encode('utf-8')

class pestania(unittest.TestCase):
  


  def setUp(self):

    self.driver = webdriver.Chrome(executable_path=chromedriver) #,chrome_options=option 

  def test_buscar(self):

    self.driver.get('https://www.google.com/intl/es/gmail/about/#')
    time.sleep(4)
    self.siguiente = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/ul[1]/li/div/div/div[1]/div/div[3]/a[1]')
    time.sleep(3)
    self.siguiente.click()

    print(self.driver.current_window_handle)
    time.sleep(3)

    handless = self.driver.window_handles

    for handle in handless:

        self.driver.switch_to.window(handle)
        print(change_text(self.driver.title))#aca cambio el formato del texto a utf-8 porq sino salt aun error 
  

  
  def tearDown(self):
    self.driver.close()  
    # self.driver.quit()
    # return super().tearDown()



  



      
if __name__ == "__main__":
#   unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = 'Resultados '))#genera un reorte de los resultados de cada test
    unittest.main()
  