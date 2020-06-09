#! python3

import sys

lista = sys.argv[1:]

for i in range(len(lista)):

    print(str(i+1)+' : '+lista[i] )