import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 200
sheet['A2'] = 100
sheet['A3'] = '=SUM(A1:A2)'
wb.save('sum.xlsx')
wb = openpyxl.load_workbook('sum.xlsx',read_only=True)
sheet = wb.active
print(sheet['A3'].value)