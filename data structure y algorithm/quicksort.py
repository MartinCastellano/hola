


def quicksort(test):

    if len(test) <= 1:

        return test

    smaller,equal,larger=[],[],[]
    
    pivot = test[len(test)-1]

    for i in test:
       
        if i < pivot :

            smaller.append(i)

        elif i == pivot:

            equal.append(i)

        else :

            larger.append(i)

    return quicksort(smaller)+quicksort(equal)+quicksort(larger)



test=[4,1,3,9,20,25,6,21,14]
print(quicksort(test))


