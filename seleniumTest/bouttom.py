import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC




chromedriver = '/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'

class botoncito(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_botoncito(self):
    
    driver = self.driver
    
    
    driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp") 

    select = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[3]') 

    option = select.find_elements_by_tag_name('label')# fijarse que elementS y el tag name es el nombre de la lista en este caso options
    
    
    
    
    for x in option:
        print('las opciones son : %s ' % x.text)       
        x.click()
        time.sleep(1)

    option[2].click()
    time.sleep(1)
        
    
  

if __name__ == "__main__":
 unittest.main()