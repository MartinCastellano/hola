from statistics import median
n = input()



lista = list(map(int, input().split(" ")))
lista.sort()


q2 = median(lista)

listaq1 = []
listaq3 = []
for i  in range(len(lista)):

    if lista[i] < q2:
        listaq1.append(lista[i])
    if lista[i] > q2:
        listaq3.append(lista[i])
q1 = median(listaq1)
q3 = median(listaq3)

print (int(q1))
print (int(q2))
print (int(q3))