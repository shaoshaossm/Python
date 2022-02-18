from openpyxl.styles import Alignment
import openpyxl

wb = openpyxl.load_workbook('数据筛选表.xlsx')
sheet = wb['Sheet1']
sheet.auto_filter.ref = 'A1:D4'
# add_filter_culumn 参数1：指定列 参数2：筛选内容
sheet.auto_filter.add_filter_column(1, ['北京', '上海'])
# add_sort_condition 参数1: 指定区域 参数2：升降序
sheet.auto_filter.add_sort_condition(ref='D2:D4', descending=True)
wb.save('数据筛选表.xlsx')
