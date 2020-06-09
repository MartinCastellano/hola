#! python3
from xml.etree.ElementTree import Element 
from xml.etree.ElementTree import tostring


def dict_to_xml(etiqueta ,diccionario):

    ele = Element(etiqueta)


    for k , v in diccionario.items():

        nodo = Element(k)

        nodo.text = str(v)

        ele.append(nodo)

#datos
 
datos ={
    'nombre':'jose',
    'mail':'jose.perez@gmail.com',
    'edad':'30',
    'pais':'mexico'
    }

xml = dict_to_xml('persona',datos)

# print(xm)

print(tostring(xml))



