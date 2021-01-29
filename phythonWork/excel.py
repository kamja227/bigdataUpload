import xlrd
import pandas as pd
import sqlalchemy as db

df = pd.read_excel(io='C:/Users/Public/Documents/somexeb.xlsx',sheet_name='Sheet1')

engine = db.create_engine('mysql://jwbig:EncglsBig!!@210.179.174.151:3306/enc_bigdata?charset=utf8', convert_unicode=False)
connection = engine.connect()
metadata = db.MetaData()
table = db.Table('skx_exw2', metadata, autoload=True, autoload_with=engine)
df.to_sql('skx_exw2',con=engine, if_exists='append', index=False)



'''
def UseXlrd():
    workbook = xlrd.open_workbook(filename = 'C:/Users/Public/Documents/somexeb.xlsx',on_demand=True)
    worksheet = workbook.sheet_by_index(0)
    first_row =[]
    for col in range(worksheet.ncols):
        first_row.append(worksheet.cell_value(0,col))
    data = []
    for row in range(1, worksheet.nrows):
        record = {}
        for col in range(worksheet.ncols):
            if isinstance(worksheet.cell_value(row,col),str):
                record[first_row[col]] = worksheet.cell_value(row,col).strip()
            else:
                record[first_row[col]] = worksheet.cell_value(row,col)
            print(first_row[col])
        data.append(record)
    return data

UseXlrd()
'''