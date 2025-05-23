from flask import Flask
import psycopg2 
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

# DATABASE CONNECTION (SQLite -> psycopg2 needs PostgreSQL!)
conn = psycopg2.connect(
    dbname='Zalandis',
    user='postgres',
    password='Sqngfn3a',
    host='localhost',
    port='5432'
)

from app import routes
