#!python3

import sys
# insert i e: 
# print: 
# remove e: 
# append e: 
# sort:
# pop: 
# reverse:
lista = sys.argv[2:]


def fun(N):
    listavacia = []
    
    # comandos ={'insert':,'print':,'remove':,'append':,'sort':,'pop':,'reverse':}
   
    
    # N = int(lista[0])
    # lista.remove(lista[0])
    
    
    
    for i,j in enumerate(lista):

        if j == 'insert':            
            listavacia.insert(int(lista[i+1]),int(lista[i+2]))
        if j == 'print':
            sys.stdout.write(str(listavacia)+'\n')
            # print(listavacia)
        if j == 'remove':
            listavacia.remove(int(lista[i+1]))

        if j == 'append':
            listavacia.append(int(lista[i+1]))
        if j == 'sort':
            listavacia.sort()
        if j == 'pop':
            listavacia.pop()
        if j == 'reverse':
            listavacia.reverse()   





if __name__ == '__main__':
    # N = int(input())
    fun(sys.argv)