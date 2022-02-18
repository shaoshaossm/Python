import openpyxl
wb = openpyxl.load_workbook('行和列.xlsx')
sheet = wb['Sheet1']
print(sheet.row_dimensions)
print(sheet.column_dimensions)
# 设置行高
sheet.row_dimensions[2].height = 50
# 设置列宽
sheet.column_dimensions['A'].width = 80
wb.save('行和列.xlsx')