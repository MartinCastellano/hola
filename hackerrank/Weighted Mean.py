N = input()



lista1 = input().split(" ")

lista2 = input().split(" ")

lista1 = list(map(int, lista1))

lista2 = list(map(int, lista2))
#print(lista1,lista2)

sum = 0
sum2 = 0

for i in range(len(lista1)):

    sum = sum + (int(lista1[i])*int(lista2[i]))
    sum2 = sum2 + int(lista2[i])

res=sum/sum2

print(res)