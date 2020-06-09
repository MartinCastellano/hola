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
chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class tabla(unittest.TestCase):
  palabra_a_buscar= 'selenium '
  def setUp(self):

    self.driver = webdriver.Chrome(executable_path=chromedriver)

  def test_tabla(self):
    
    driver = self.driver
    
    
    driver.get("https://www.w3schools.com/html/html_tables.asp") 

    valor = driver.find_element_by_xpath('//*[@id="customers"]/tbody').text
    print(valor)
    
    row = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr'))

    print(row)

    col = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th'))

    print(col)

    for x in range(2,row + 1):
        for y in range(1,col +1):
            dato=driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr['+str(x)+']/td['+str(y)+']')
            print(dato.text)
        print("")    

if __name__ == "__main__":
 unittest.main()