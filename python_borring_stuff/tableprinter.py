

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

#for w in range(len(tabledata)):
 #       colwith.append(max([len(col) for col in list2D[row]]))
def tableprinter(tableData):

    colwith = [0] * len(tableData)

    for w in range(len(tableData)):
        
        for z in range(len(tableData[w])):

            if len(tableData[w][z]) > colwith[w]:

                colwith[w] =  len(tableData[w][z])
                
    
    for x in range(len(tableData[0])):

         for y in range(len(tableData)):

            print(tableData[y][x].rjust(colwith[y]),end =" ")
        
         print()
                     

            

tableprinter(tableData)