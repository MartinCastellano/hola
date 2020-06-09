#! python3

import sys


number =sys.argv

number.pop(0)




for i in range(len(number)):
    if  (int(number[i])%3==0) and (int(number[i])%5==0): 
        print('fizzbuzz')
    elif  int(number[i])%5==0:
        print('buzz')    
    elif (not(int(number[i])%3==0)) and (not(int(number[i])%5==0)): 
       print(number[i])
    elif  int(number[i])%3==0:
        print('fizz')
    
    
    