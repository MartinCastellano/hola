
import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC




chromedriver = '/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'

class select(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_select(self):
    
    driver = self.driver
    
    
    driver.get("https://www.w3schools.com/howto/howto_custom_select.asp") 

    select = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select') 

    option = select.find_elements_by_tag_name('option')# fijarse que elementS y el tag name es el nombre de la lista en este caso options
    
    
    
    for x in option:
        print('los valores son : %s' % x.get_attribute('value'))            
        
        print(x.text)

    
    
    seleccionar = Select(driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select'))
    sel = seleccionar.select_by_value('10') #selecciono cual quiero 
    time.sleep(3)
    sel = seleccionar.select_by_visible_text('Mini')
    time.sleep(3)

    print(driver.title)
        
    #find_element_by_id
    #find_element_by_name
    #find_element_by_xpath
    #find_element_by_link_text
    #find_element_by_partial_link_text
    #find_element_by_tag_name
    #find_element_by_class_name
    #find_element_by_css_selector

    #Para encontrar multiples elementos (estos metodos devolveran una lista):

    #find_elements_by_name
    #find_elements_by_xpath
    #find_elements_by_link_text
    #find_elements_by_partial_link_text
    #find_elements_by_tag_name
    #find_elements_by_class_name
    #find_elements_by_css_selector
   

  

  

if __name__ == "__main__":
 unittest.main()