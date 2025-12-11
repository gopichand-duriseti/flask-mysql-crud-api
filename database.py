from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv('/home/gopichand/Documents/password.env')

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')

db=mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
    )
cursor=db.cursor()