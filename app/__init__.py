from flask import Flask
import psycopg2 
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

# CAll the Database Zalandis, user: postgres, password: use your own PG password, host: localhost, port: 5432
conn = psycopg2.connect(
    dbname='Zalandis', # Make sure to create the database in PostgreSQL
    user='postgres',
    password='Sqngfn3a', # Write your own password
    host='localhost',
    port='5432'
)

from app import routes
