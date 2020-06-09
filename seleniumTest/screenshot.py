

import time #pertenece a python 
import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2  



chromedriver = '/home/martin/Downloads/python/seleniumTest/drivers/chromedriver'

class screenshot(unittest.TestCase):
  def setUp(self):

    self.driver = webdriver.Chrome(chromedriver)

  def test_screenshot(self):
    
    driver = self.driver
    
    
    driver.get("https://google.com")

    driver.save_screenshot('img2.png')

    
    time.sleep(2)
    
    

  def test_comparar(self):
      img1 = cv2.imread('img1.png')
      img2 = cv2.imread('img2.png')

      dif = cv2.absdiff(img1, img2)

      togray = cv2.cvtColor(dif,cv2.COLOR_BGR2GRAY)

      contours,_ = cv2.findContours(togray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

      for c in contours :
          a = cv2.contourArea(c)
          if a >= 20:

              posX,posY,ancho,alto = cv2.boundingRect(c)
              cv2.rectangle(img1,(posX,posY),(posX+ancho,posY+alto),(0,0,255),2)
              
      while(1):

          cv2.imshow('imagen1',img1)
          cv2.imshow('imagen2',img2)
          cv2.imshow('diferencias',dif)
          keyboard = cv2.waitKey(5) & 0xFF
          if keyboard == 27:
              
              break
      cv2.destroyAllWindows()
        

  #def tearDown(self):
    #self.driver.close()

if __name__ == "__main__":
 unittest.main()
