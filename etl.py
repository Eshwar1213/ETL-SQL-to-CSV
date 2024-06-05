import pandas as pd
from sqlalchemy import create_engine

username = 'root'
password = 'root'
host = 'localhost'
db = 'exceldata'
 
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{db}')

query = 'select * from Data_1'

data= pd.read_sql(query,con =engine)

filepath='data.csv'

data.to_csv(filepath,index=False)
print('data transfered',filepath)
