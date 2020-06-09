#! python3 
# pw.py

PASSWORD = {'user':'btpgjttnnqx'}


import sys,pyperclip
 

if len(sys.argv) < 2:
    print(' use : python pw.py [account] - copy acc pass')

    sys.exit()

account = sys.argv[1]


if account in PASSWORD:


    pyperclip.copy(PASSWORD[account])

    print('passwor for '+account+' copied ')

else :
    print('error account')

