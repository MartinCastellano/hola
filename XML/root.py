import xml.etree.ElementTree as et 


archivo = et.parse('guestbook.xml')

raiz = archivo.getroot()

print(raiz.tag)


for i in raiz :

    hijo = i.find('fname')
    hijo2 = i.find('lname')
    print(hijo.text,hijo2.text)


