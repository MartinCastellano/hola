#! python3

import openpyxl,sys,os

from openpyxl.utils import get_column_letter

from openpyxl.styles import Font

from openpyxl.styles import NamedStyle

#/home/martin/Downloads/Practicas/seleniumTest/borring stuff/ejemplo.xlsx

if sys.argv[1:]:
    

    A =sys.argv[1:]
    
    path = str(A[2]+' '+A[3])
    M = int(A[1])
    N=int(A[0])

    print (path)
    print(M)
    print(N)
    



wn = openpyxl.load_workbook(path)

sheet= wn.get_active_sheet()

sheet.insert_rows(N, amount=M)

        
wn.save('/home/martin/Downloads/Practicas/seleniumTest/borring stuff/ejemplo3.xlsx')