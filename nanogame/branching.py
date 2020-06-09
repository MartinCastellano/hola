#! python3

import sys

numbers = int(sys.argv[1])+int(sys.argv[2])


if numbers <= 0: 
    print('You have chosen the path of destitution.')
if numbers >= 100:
    print('You have chosen the path of plenty.')
if numbers > 100:
    print('You have chosen the path of excess.')
