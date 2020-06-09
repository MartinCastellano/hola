#! python2
import time #pertenece a python 
import unittest
from selenium import webdriver

import HtmlTestRunner


# from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options #para segundo plano
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


brave  = '/usr/bin/brave-browser'

chromedriver = '/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'

option = webdriver.ChromeOptions()
Options = Options()
Options.add_argument('--headless')
option.binary_location = brave

class suit(unittest.TestCase):
    
  def setUp(self):

    self.driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=Options) #,chrome_options=option

  
    
    

  def test_alerta(self):
    
    driver = self.driver  
        
    driver.get('https://duckduckgo.com/?q=2048&atb=v187-1&ia=answer')

    time.sleep(1)

    alerta = driver.find_element_by_xpath("//*[@id='zci-game2048']/div/div/div/div[1]/div/div[2]/button")

    alerta.click()
    
    time.sleep(2)


    cuadro = driver.find_element_by_xpath("//*[@id='game2048__area']")

  def test_buscar(self):

    self.driver.get('https://www.google.com/')
    self.busqueda = self.driver.find_element_by_name('q')
    self.busqueda.send_keys('slenium')
    self.busqueda.submit()
    time.sleep(2)

  def test_assertEqual(self):

      driver =  self.driver

      self.driver.get('https://www.google.com/')

      eltitulo = 'eeee'

      self.assertEqual('Google', eltitulo, 'el titulo es igual al desigando en la pagina web') 

  def test_assertNotEqual(self):

      driver =  self.driver

      self.driver.get('https://www.google.com/')

      eltitulo = "eloo"

      self.assertNotEqual('Google', eltitulo, 'el titulo NO es igual al desigando en la pagina web') 
  def tearDown(self):
    self.driver.close()  
    self.driver.quit()
    # return super().tearDown()



  



      
if __name__ == "__main__":
  unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = 'Resultados '))#genera un reorte de los resultados de cada test

  