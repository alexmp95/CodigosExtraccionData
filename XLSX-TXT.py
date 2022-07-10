# Instlar las librerias panda, openpyxl
#
import pandas as pd
xl= pd.ExcelFile('C:/Users/Alexis/Desktop/Pruebas/V2/data/Analisisdedominio.xlsx')
xl.sheet_names
for sheet in xl.sheet_names:
    file = pd.read_excel(xl,sheet_name=sheet)
    file.to_csv(sheet+'.txt',header=False,index=False)

