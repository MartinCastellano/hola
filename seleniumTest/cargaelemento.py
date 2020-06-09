#espera hasta que se carga el elemento en la pagina

import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC




chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class desplegarelemento(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_desplegarelemento(self):
    
    driver = self.driver    
    
    driver.get("https://www.google.com")       
    
    dispelemnt = driver.find_element_by_name('btnI')
    
    print(dispelemnt.is_displayed())#false si esta desplegado (mostrando) sin presionar
    print(dispelemnt.is_enabled())# true si esta habilitado
    
    time.sleep(2)
     
    dispelemnt = driver.find_element_by_name('btnK')
    if dispelemnt.is_displayed() == False: # me tira un false si esta desplegado luego de ser presionado deberia mostrar true
    
        
        print(dispelemnt.is_displayed())

    

  

if __name__ == "__main__":
 unittest.main()
