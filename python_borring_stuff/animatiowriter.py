#! python3
from time import sleep
import sys
from random import uniform


lines = ["You have woken up in a mysterious maze\n",
         "The building has 5 levels\n",
         "Scans show that the floors increase in size as you go down\n"]

for x in lines:
    for j in x:
        print(j,end ='')
        sys.stdout.flush()
        sleep(.05) 