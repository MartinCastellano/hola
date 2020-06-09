
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]


lista = []

if len(nums1) < len(nums2):
    mayor = nums2
    menor = nums1
else:
    mayor = nums1
    menor = nums2



for i in range(0,len(mayor)):
    if mayor[i] in menor:
       

        lista.append(mayor[i]) 
        lista = sorted(lista)
lista = list(dict.fromkeys(lista))
print(lista)
