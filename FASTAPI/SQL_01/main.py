import uvicorn
from fastapi import FastAPI
import pyodbc
import json

import py_functions
import config

app = FastAPI()

def connect_db(pwd):
    driver = config.DRIVER

    server = config.SERVER
    database = config.DATABASE
    uid = config.UID
    pwd = pwd
    con_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'
    cnxn = pyodbc.connect(con_string)
    cnxn.autocommit = True
    cursor = cnxn.cursor()
    print("Connection with database")
    return cnxn

with open(r'C:\Users\ruchinskyo\Documents\pythonProject\GCP\FASTAPI\SQL_01\password.json') as f:
    # {"password":"xyz"}
    data = json.load(f)
pwd=data['password']

cnxn = connect_db(pwd)

@app.get('/')
def get_data():
    df = py_functions.fetch_data(cnxn)
    return df.to_dict('r')

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)

