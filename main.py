import pandas as pd

location = ("C:/Users/sTn/Desktop/test123.xlsx")

excel_object = pd.ExcelFile(location)
all_sheets = excel_object.sheet_names
print(all_sheets)

sheet = pd.read_excel(excel_object, "Sheet1")



a = sheet.iloc[[0], [0]]
print(a)


