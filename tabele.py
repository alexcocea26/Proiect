from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from proiect import Base  # aici sunt clasele 

# connection string 
DATABASE_URL = "mssql+pyodbc://COCEA\\SQLEXPRESS/proiect?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

engine = create_engine(DATABASE_URL)

# Creează toate tabelele
Base.metadata.create_all(engine)

print("Tabele create cu succes!")