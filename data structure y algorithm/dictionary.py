import logging
"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {}

country =  {}

continente = 'North America' #input('Indique el continente: ').capitalize() 

pais = 'USA'  #input('Indique el pais: ').capitalize() 

ciudad = ['Mountain View','Atlanta'] #[input('Indique la ciudad: ').capitalize()]


country.update({pais : ciudad})


locations.update({ continente : country})



print(locations)

def sumar(a ,b):
    return a + b

console.log(sumar(10,10)) == 20 
