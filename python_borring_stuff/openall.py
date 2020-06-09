import os,re 

palabra = raw_input('coloque la palabra a buscar: ')



lista=os.listdir('/home/martin/Downloads/Practicas/seleniumTest/borring stuff')

lista2=[]


for i in range(len(lista)):

    if re.compile(r'(\.txt)$').findall(lista[i]):
        
       lista2.append(lista[i])



for j in range(len(lista2)):

    texto = open(r'/home/martin/Downloads/Practicas/seleniumTest/borring stuff/'+lista2[j]).read()

    lea= re.compile(palabra,re.IGNORECASE).search(texto)

    if palabra in texto:
        print('*  la plabara que busca se encuentra en: '+lista2[j])

    

    
    





# ya tendria el path y el nombre de cada archivo de texto 

# con un for recorro cada uno de los archivos y veo si se encuentra el contenido que busco en caso afirmativo 
#debor cerrar el archivo antes de salir del for
#guardo indico que el contenido esta en ese archivo 