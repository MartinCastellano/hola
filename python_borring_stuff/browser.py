#! python3
# browser python browser.py 870 valencia st, san francisco, ca 94110
import webbrowser,sys,pyperclip
import requests





if len(sys.argv) > 1 :

    addres = ' '.join(sys.argv[1:]) # python browser.py 870 valencia st, san francisco, ca 94110
else:
    
    addres = pyperclip.paste() #lo que tenga en el pyperclip ej 870 valencia st, san francisco, ca 94110

webbrowser.open('https://maps.google.com/maps/place/'+ addres)





