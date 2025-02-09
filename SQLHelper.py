from sqlalchemy import create_engine
import pandas as pd

# Database connection parameters
server = r'Som-PC\SQLSERVER2022'
database = 'Python-SQL Project'

# Create a SQLAlchemy engine
conn_str = f"mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(conn_str)

def run_query(query):
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df


