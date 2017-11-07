# Concatenating many files
import os
import glob
import pandas as pd

# os.getcwd()

csv_files = glob.glob('.\\Data\\*.csv')

list_data = []
for file in csv_files:
    data = pd.read_csv(file)
    list_data.append(data)

list_data = pd.concat(list_data)

print(list_data.shape)
print(list_data.head())

#--------------------------------------------------------------
# Merging data
#--------------------------------------------------------------

import pyodbc
import pandas as pd
   
conn_str = ('SERVER={server};'     +
            'DATABASE={database};' +
            'TRUSTED_CONNECTION=yes')


config = dict(server=   'KRGANDHI1-W541\S2017A', 
              port=      1433,                    
              database= 'AdventureWorksDW2017',
              )


conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};' +
    conn_str.format(**config)
    )

sql = 'SELECT ProductCategoryKey, EnglishProductCategoryName FROM DimProductCategory'
DimProductCategory = pd.read_sql_query(sql, conn)
print(DimProductCategory.shape)
print(DimProductCategory)


sql = 'SELECT ProductCategoryKey, ProductSubcategoryKey, EnglishProductSubcategoryName FROM DimProductSubcategory'
DimProductSubcategory = pd.read_sql_query(sql, conn)
print(DimProductSubcategory.shape)
print(DimProductSubcategory)

Prod_SubProd = pd.merge(left=DimProductCategory, right=DimProductSubcategory, on='ProductCategoryKey')
print(Prod_SubProd.shape)
print(Prod_SubProd)


