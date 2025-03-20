import mysql.connector
import re


def email_checker(email):
    pattern = r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$"
    while not re.match(pattern, email):
        print("Invalid email format! Example: user@example.com")
        email = input("Enter a valid email: ")
    return email

def password_checker(password):
    while True:
        if not any(char.isdigit() for char in password):
            print("Password must include at least one number.")
        elif not any(char.isalpha() for char in password):
            print("Password must include at least one letter.")
        else:
            return password
        
        password = input("Enter a valid password: ")

def connect_to_database(user="root", password="123", host="localhost", database="test_database"):
    print("Connecting to MySQL server...")

    cnx = mysql.connector.connect(user=user, password=password, host=host)
    cursor = cnx.cursor()

    cursor.execute(f"SHOW DATABASES LIKE '{database}'")
    db_exists = cursor.fetchone()

    if not db_exists:
        print(f"Database '{database}' does not exist. Creating it now...")
        cursor.execute(f"CREATE DATABASE {database}")
        cnx.commit()
        print(f"Database '{database}' created successfully.")

    cursor.close()
    cnx.close()

    print(f"Connecting to database '{database}'...")
    cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
    print("Connected successfully.")
    return cnx


email = email_checker(input("Enter your email: "))
password = password_checker(input("Enter your password: "))


try:
    cnx = connect_to_database()
    cursor = cnx.cursor()

    sql = """CREATE TABLE IF NOT EXISTS User(
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );"""
    
    cursor.execute(sql)
    cnx.commit()

    cursor.execute("SELECT email FROM User WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Email already exists. Choose another email.")
    else:
        sql = "INSERT INTO User (email, password) VALUES (%s, %s)"
        cursor.execute(sql, (email, password))
        cnx.commit()
        print("User registered successfully!")

except mysql.connector.Error as err:
    print(f"Database error: {err}")
except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    if "cursor" in locals():
        cursor.close()
    if "cnx" in locals():
        cnx.close()
