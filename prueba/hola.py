#!python3
import random
nocambio=0
sicambio=0
for i in range(1000000):
    primera_opcion = random.randint(1,3)
    ubicacion_premio = random.randint(1,3)
    bandera = 0
    while bandera == 0:   
        elimino = random.randint(1,3)
        if elimino != primera_opcion and elimino!= ubicacion_premio:   
            if primera_opcion == ubicacion_premio:
                nocambio = nocambio +1 
            else:
                sicambio = sicambio+1
            bandera = 1
print("me conviene cambiar: "+str(sicambio)+" veces, y no me conviene cambiar: "+str(nocambio)+" veces")