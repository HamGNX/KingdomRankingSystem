import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",    # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="KingdomRanking"
    )
    return connection