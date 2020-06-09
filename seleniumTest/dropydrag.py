import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


chromedriver = '/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'

class dropdrag(unittest.TestCase):
  
  def setUp(self):

    self.driver = webdriver.Chrome(executable_path=chromedriver)

  def test_dropdrag(self):
    driver = self.driver
        
    driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

    time.sleep(5)

    element = driver.find_element_by_id('dropContent')
    for x in range(7):
        dragelement =element.find_element_by_id('box'+str(x+1))    
        
        target = driver.find_element_by_id('box10'+str(x+1))
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(dragelement,target).perform()

    time.sleep(3)
    element =driver.find_element_by_id('countries')

    for x in range(7):
        dragelement =element.find_element_by_id('box'+str(x+1))

        target =driver.find_element_by_id('dropContent')
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(dragelement,target).perform()

    time.sleep(2)

                         
                      
            
    
    
            
            
    time.sleep(3)



    
if __name__ == "__main__":
 unittest.main()