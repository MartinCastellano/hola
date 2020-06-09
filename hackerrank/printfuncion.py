import sys

def printame(m):
    contador = 1
    l = ['1']
    
    for i in range(m):
        
        if contador == m:
            return sys.stdout.write(''.join(l))
        else:
            contador = contador +1
            l.append(str(contador))
        
               




if __name__ == '__main__':
    n = int(input())
    printame(n)