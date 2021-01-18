import xlrd

location = ("C:\Users\sTn\Desktop")

wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)


