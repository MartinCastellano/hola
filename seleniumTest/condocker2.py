
#! python3
import  unittest 
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import  time
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities

# sudo docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:latest

chromedriver = '/home/martin/trainings/seleniumTest/drivers/chromedriver'

driver = webdriver.Remote('http://localhost:4444/wd/hub',desired_capabilities=webdriver.DesiredCapabilities.CHROME)       


driver.get('https://www.w3schools.com/html/default.asp')  
time.sleep(2)
cookies = driver.get_cookies()
print('los cookies son: ',cookies)
     