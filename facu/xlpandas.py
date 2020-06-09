#! python3

import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('/home/martin/trainings/facu/bocas2.xlsx')
    sh = wb.sheet_by_name('hoja1 -1')
    csv_file = open('/home/martin/trainings/facu/aaa.csv','w',newline='')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.max_row+1):
        wr.writerow(sh.row_values(rownum))

    csv_file.close()