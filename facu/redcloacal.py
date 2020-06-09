#!/usr/bin/env python3
#Creo la clase  Bocas de registro.
class BocaRegistro:
    def __init__(self,denominacion, x, y,z):
        self.denominacion = denominacion
        self.x = x
        self.y = y
        self.z = z

# Ahora voy a instanciar los distitntos objetos Bocasregistro de un archivo csv
datosbr=open("/home/facu/Escritorio/programacion/programas/red_cloacal/bocas.csv",'r')
linea="algo"
contador = 1
linea = datosbr.readline()
while bool(linea):  
    nombreobjeto='BR'+str(contador)
    linea = linea.strip() #con este strip saco la linea \n (salto de linea del final)
    [denominacion,x,y,z]=linea.split(",")
    denominacion = denominacion
    x = x
    y = y
    z = z
    nombreobjeto = BocaRegistro(denominacion,x,y,z)
    print(nombreobjeto.denominacion,nombreobjeto.x,nombreobjeto.y,nombreobjeto.z)
    linea = datosbr.readline()
    contador += 1
# hasta aca lo que hice fue crear la clase BocasRegistro y las cargue desde el archivo bocas.csv   