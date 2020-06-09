#! python3
import  unittest 
from selenium import  webdriver
from selenium.webdriver import ActionChains
import  time
from selenium.webdriver.common.by import By





brave = webdriver.ChromeOptions()

brave.binary_location = '/usr/bin/brave-browser'

chromedriver = '/home/martin/trainings/seleniumTest/drivers/chromedriver'





class usando_unittest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=chromedriver,options=brave)

    def test_ipload_file(self):
        self.driver.get('https://mdbootstrap.com/plugins/jquery/')

        time.sleep(2)

        self.driver.find_element_by_id('el id donde lo quiero subir lo que quiero').send_keys('el path donde esta lo que quiero')    

    def tearDown(self):
        self.driver.tearDown()


if __name__ == "__main__":
    unittest.main()        
        
    