from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as et

from xml.dom import minidom

raiz = Element('padre')

tree= ElementTree(raiz)

son  = Element('hijo')

raiz.append(son)
secondson = Element('segundoHijo')
raiz.append(secondson)

nieto = Element('Pnieto')

son.append(nieto)

nietoS = Element('Snieto')

secondson.append(nietoS)


son.text='julio'

raiz.set('nick','abuelito')

ele=minidom.parseString(et.tostring(raiz)).toprettyxml(indent = "   ")
with open("herencia.xml", "w") as f:


    f.write(ele)



# print(et.tostring(raiz))
