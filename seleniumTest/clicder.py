#! python3
import  unittest 
from selenium import  webdriver
from selenium.webdriver import ActionChains
import  time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC





brave = webdriver.ChromeOptions()

brave.binary_location = '/usr/bin/brave-browser'

chromedriver = '/home/martin/trainings/seleniumTest/drivers/chromedriver'



class usando_unittest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=chromedriver,options=brave)

    def test_clickder(self):       


        self.driver.get('')

        clickder = self.driver.find_element_by_xpath('')

        action = ActionChains(self.driver)

        action.context_click(clickder).perform

        time.sleep(3)

    def espera(self,xpath):

        
        try:
            element = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,xpath))
            
        finally:
            driver.quit()
       

    def tearDown(self): 
        self.driver.tearDown()



if __name__ == "__main__":
    unittest.main()        
        