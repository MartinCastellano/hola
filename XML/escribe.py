
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup

from xml.dom import minidom

# from ElementTree_pretty import prettify

p = et.Element('padre')

c = et.SubElement(p,'hijo')

d = et.SubElement(p,'segundo')

e = et.SubElement(c,'nieto')

# et.dump(p)

tree = et.ElementTree(p)





commen = et.Comment('este comentario deberia estar en la raiz no se porq aparece aca')

p.append(commen)


raiz = tree.getroot()



elemento = raiz[1]

elemento.set('elhijo','elnombre del hijo ')

raiz.set('nombre','hola')# el primer atributo seria el nombre y el segundo su valor

raiz[0].text=' esta es otra forma de agregar un text' # asi es como se agrega texto dentro del los tags
raiz[1].text = 'aca va la info que le corresponde al segundo hijo'



ele=minidom.parseString(et.tostring(raiz)).toprettyxml(indent = "   ")

# print(ele)
with open("salida.xml", "w") as f:
    # f.write(ele)
    f.write(ele.encode('utf-8'))

print(BeautifulSoup(ele, "xml").prettify())
