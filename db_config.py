# db_config.py

import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="be9h1kqjuuxzkpadgkcc-mysql.services.clever-cloud.com",
            user="uqj0qig3bsto59oh",
            password="3OToj4A94CqH5EZgMj7P",
            database="be9h1kqjuuxzkpadgkcc",
            port=3306
        )
        if connection.is_connected():
            print("✅ Connected to Clever Cloud MySQL database")
            return connection
    except Error as e:
        print(f"❌ Error connecting to Clever Cloud database: {e}")
        return None
