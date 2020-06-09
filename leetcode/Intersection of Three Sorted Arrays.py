
arr1 = [1,2,3,4,5] 
arr2 = [1,2,5,7,9] 
arr3 = [1,3,4,5,8]

lista = []
for i in range(0,len(arr1)):
    if arr1[i] in arr2:
        if arr1[i] in arr3:
            print(arr1[i])
            lista.append(arr1[i]) 
    

print(lista)        