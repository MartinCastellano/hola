

#nums1 = [4,9,5]   
#nums2 = [9,4,9,8,4]
#nums1 = [3,1,2]
#nums2 = [1,1]
#nums1 = [1,2,2,1]
#nums2 = [2,2]
nums1 = [4,7,9,7,6,7]
nums2 = [5,0,0,6,1,6,2,2,4]
# 4,6 6,6,4
lista = []

if len(nums1) < len(nums2):
    mayor = nums2
    menor = nums1
else:
    mayor = nums1
    menor = nums2



for i in range(len(mayor)):
    if mayor[i] in menor:
       

        lista.append(mayor[i]) 
print(lista)
#print(menor)
for i in range(len(menor)):
    while menor[i] not in lista:
        del(menor[i])
        print(menor) 

if len(lista) < len(menor):
    dame = lista
else:
    dame = menor    

print(dame)