#! python3
import  unittest 
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import  time




brave = webdriver.ChromeOptions()

brave.binary_location = '/usr/bin/brave-browser'

chromedriver = '/home/martin/trainings/seleniumTest/drivers/chromedriver'



class usando_unittest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=chromedriver,options=brave)
        time.sleep(3)
        
    def test_search_frame(self):       


        self.driver.get('https://www.google.com/')  
        time.sleep(2)
        frame = driver.find_element_by_id('gbwa')

        frame.click()
        time.sleep(3)

        driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[3]/iframe'))
        #para buscar un fram hay q buscar la terminacion iframe
        
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div/ul[1]/li[4]/a/div[5]/span')
        time.sleep(2)

             

    
       

    def tearDown(self): 
        self.driver.tearDown()



if __name__ == "__main__":
    unittest.main()        