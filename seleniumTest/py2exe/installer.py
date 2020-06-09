
#############################################################################
#
#
# 
# 
# 
# 
#               en la terminal nos vamos donde esta el archivo .py y lo installamos
#                pyinstaller archivo.py
#
# 
# 
# 
# 
#
# 
#   
#################################################################################


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select 

#firefoxdriver = '/home/martin/Downloads/python/seleniumTest/drivers/geckodriver'
chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

#driver = webdriver.Firefox(executable_path=firefoxdriver)
#driver.get("https://google.com")


#driver = webdriver.Chrome(chromedriver)
#driver.get("https:google.com")

#abre una ventana de chrome o firefox

class PythonOrgSearch(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(chromedriver)

  def test_search_in_python_org(self):
    driver = self.driver
    driver.get("https://google.com")
    
    #self.assertIn("Python", driver.title)
    
    elem = driver.find_element_by_name("q")
    
    elem.send_keys("hola lalo ",Keys.ARROW_DOWN)
    elem.send_keys(Keys.ARROW_DOWN)
    
    elem.clear()
    elem.send_keys("chau", Keys.ARROW_DOWN)
    
    time.sleep(3)
    
    
      
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    assert "No results found." not in driver.page_source


  #def tearDown(self):
    #self.driver.close()



if __name__ == "__main__":
 unittest.main()