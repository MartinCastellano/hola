#! python3
import subprocess,time,os
import webbrowser
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



# s =subprocess.Popen(['see','/home/martin/Downloads/Automate_the_Boring_Stuff_2e_onlinematerials/automate_online-materials/alarm.wav'])
#subprocess.Popen(['display','/home/martin/Downloads/camboya.jpg'])



img=mpimg.imread('/home/martin/Downloads/Practicas/seleniumTest/img1.png')
imgplot = plt.imshow(img)
plt.show()
