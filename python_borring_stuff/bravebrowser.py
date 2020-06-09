import time #pertenece a python 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


brave  = '/usr/bin/brave-browser'

chromedriver = '/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'

option = webdriver.ChromeOptions()
option.binary_location = brave
class alerta(unittest.TestCase):
  
  def setUp(self):

    self.driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=option)

  def test_alerta(self):
    
    driver = self.driver
        
    driver.get('https://duckduckgo.com/?q=2048&atb=v187-1&ia=answer')

    time.sleep(1)

    alerta = driver.find_element_by_xpath("//*[@id='zci-game2048']/div/div/div/div[1]/div/div[2]/button")

    alerta.click()
    
    time.sleep(4)


    cuadro = driver.find_element_by_xpath("//*[@id='game2048__area']")


    time.sleep(1)
    cuadro.send_keys(Keys.DOWN)
    cuadro.send_keys(Keys.LEFT)
    cuadro.send_keys(Keys.RIGHT)
    cuadro.send_keys(Keys.DOWN)
    cuadro.send_keys(Keys.UP)
    cuadro.send_keys(Keys.DOWN)
    
    time.sleep(1)
    
    
    
    
if __name__ == "__main__":
 unittest.main()