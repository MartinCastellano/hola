


def quicksort(array):

    if len(array)<1:
        return array[0]
    
    smaller,larger,pivot=[],[],[]

    pivot = array[len(array)-1]

    for i in range(len(array)):

        if array[i] < pivot:

            smaller.append(array[i])
        
        else:

            larger.append(array[i])
    
    return quicksort(smaller) +quicksort(pivot) +quicksort( larger)


test = [ 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))