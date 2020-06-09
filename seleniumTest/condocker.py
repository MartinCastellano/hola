#! python3
import  unittest 
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import  time
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities





brave = webdriver.ChromeOptions()

brave.binary_location = '/usr/bin/brave-browser'

chromedriver = '/home/martin/trainings/seleniumTest/drivers/chromedriver'



class usando_unittest(unittest.TestCase):

    def setUp(self):

        # self.driver = webdriver.Chrome(executable_path=chromedriver,options=brave)
        # time.sleep(3)
        self.driver =webdriver.Remote('http://localhost:4444/wd/hub',desired_capabilities=webdriver.DesiredCapabilities.CHROME)
    def test_cookies(self):       


        self.driver.get('https://www.w3schools.com/html/default.asp')  
        time.sleep(2)
        cookies = driver.get_cookies()

        print(cookies)     

    
       

    def tearDown(self): 
        self.driver.tearDown()



if __name__ == "__main__":
    unittest.main()        