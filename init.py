# New script to extract the data from SQL Server (On-Premises)

# installing the library to connect to sql server
# pip install pyodbc

# Reading data from a SQL-SERVER/Oracle database
import pyodbc

# Defining the connection string
conn = pyodbc.connect('''DRIVER={SQL Server}; Server=127.0.0.1; 
                        UID=adminUser; PWD=passWrd@123; DataBase=PROD_AZ''')

# Fetching the data from the selected table using SQL query
RawData= pd.read_sql_query('''select * from [EMP].[Employee_table]''', conn)
RawData.head()