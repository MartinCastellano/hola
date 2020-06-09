import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


Options = Options()
Options.add_argument('--headless')
palabra_a_buscar= 'selenium'
chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class busca(unittest.TestCase):
  palabra_a_buscar= 'selenium '
  def setUp(self):

    self.driver = webdriver.Chrome(chrome_options=Options,executable_path=chromedriver)#con este agregado lo hago fucnionar en segundo plano

  def test_busca(self):
    
    driver = self.driver
    
    
    driver.get("https://www.google.com") 

    busqueda = driver.find_element_by_name('q')
    busqueda.send_keys(palabra_a_buscar)
    
    time.sleep(3)
  
    for i in range(1,11):

    
       element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/ul/li['+str(i)+']/div/div[2]/div/span').text
       print (element)
    
  

if __name__ == "__main__":
 unittest.main()