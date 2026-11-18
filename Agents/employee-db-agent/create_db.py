import sqlite3

#  create a database connection
def get_connection():

    conn = sqlite3.connect("company.db")

    return conn