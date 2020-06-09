import time #pertenece a python 
import unittest
import configparser
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




#chromedriver = '/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'

class config(unittest.TestCase):
  
  def setUp(self):
    conf = configparser.ConfigParser()
    conf.read('conf.ini')
    conf.sections()

    cargaexplorer = conf['General']['chrome']

    self.page = conf['Paginas']['page']


    self.driver = webdriver.Chrome(executable_path=cargaexplorer)

  def test_config(self):
    
    driver = self.driver

    driver.implicitly_wait(5)

    driver.get(self.page)

    busca = driver.find_element_by_name('q')


   
if __name__ == "__main__":
 unittest.main()