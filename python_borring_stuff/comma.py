spam = ['apple','banana','tofu','cats','lelo','lalo']




def comma(spam):

    
    ultima =spam[-1]
    spam.remove(spam[-1])
    for x in spam:

        
        
        delimiter = ','
        string = delimiter.join(spam)

    return string+' y '+ultima


print(spam[-1])
print(comma(spam))