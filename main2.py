import xlrd

workbook = xlrd.open_workbook('test.xlsx')
# workbook.sheets()
# workbook.sheet_names()
worksheet = workbook.sheet_by_index(0)

print (worksheet.nrows, worksheet.ncols)

row = worksheet.row(0)
print (row[0].value)
print (worksheet.cell_value(0,0))
