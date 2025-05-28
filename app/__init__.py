from flask import Flask
import psycopg2 
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

# CAll the Database Zalandis, user: postgres, password: use your own PG password, host: localhost, port: 5432
conn = psycopg2.connect(
    dbname='yourdb',
    user='youruser',
    password='yourpassword', #Your password
    host='localhost', #Typical standard
    port='5432' #PGAdmin standard
)

from app import routes
