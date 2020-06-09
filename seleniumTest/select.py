###############################no lo entendi bucar :)


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC 



chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class select(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_select(self):
    
    driver = self.driver
    
    driver.get("https://google.com")
    time.sleep(1)
    
    element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]')
    all_options = element.find_elements_by_tag_name("name")
    for x in all_options:
        print('Valor es: %s' % x.get_attribute("q"))
        

    select = Select(driver.find_element_by_name('name'))
    select.select_by_index(index)
    select.select_by_visible_text("text")
    select.select_by_value(value)
  
  #def tearDown(self):
    #self.driver.close()

if __name__ == "__main__":
 unittest.main()

