import sqlite3

# Function to get a database connection
def get_connection():

    conn = sqlite3.connect("company.db")

    return conn