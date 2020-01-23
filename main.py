import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({"bold": True})

worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Price', bold)

expenses = [
    ["Bed", 100],
    ["Chair", 20],
    ["Table", 50]
]

col = 0
row = 1

for item, price in expenses:
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, price)
    row += 1

worksheet.write(row, 0, "Total", bold)
worksheet.write(row, 1, "=SUM(B2:B4)")

workbook.close()
