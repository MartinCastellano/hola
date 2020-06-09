#! python3
import  unittest 
from selenium import  webdriver
from selenium.webdriver import ActionChains
import  time





brave = webdriver.ChromeOptions()

brave.binary_location = '/usr/bin/brave-browser'

chromedriver = '/home/martin/trainings/seleniumTest/drivers/chromedriver'





class mouse_unittest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=chromedriver,options=brave)
        
    

    def test_mouse(self):

        self.driver.get('https://nicolasalvarez.com/')
        time.sleep(3)

        mouse_move=self.driver.find_element_by_xpath('//*[@id="menu-item-68"]/a')

        mouse_move2=self.driver.find_element_by_xpath('//*[@id="menu-item-82"]/a')

        accion = ActionChains(self.driver)

        accion.move_to_element(mouse_move).move_to_element(mouse_move2).click().perform()

        time.sleep(3)


    def tearDown(self):

        self.driver.close()    



if __name__== '__main__' :

    unittest.main()