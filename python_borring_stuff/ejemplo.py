#! python3

import bs4
import requests

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,"html.parser")
print(type(noStarchSoup))


examplF = open('/home/martin/Downloads/Practicas/seleniumTest/borring stuff/ejemplo.html')
examplS = bs4.BeautifulSoup(examplF,"html.parser")
print(type(examplS))

element = examplS.select('#author')

print(element[0].getText())


pelement = examplS.select('p')

print(pelement[0].getText())
print(pelement[1].getText())
print(pelement[2].getText())



spnelement = examplS.select('span')[0]

print(spnelement.get('id'))

print(spnelement.attrs)
