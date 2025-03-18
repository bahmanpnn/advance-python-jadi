"""
    CREATE DATABASE IF NOT EXISTS test_database;
    CREATE TABLE person (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        email VARCHAR(255) UNIQUE
    );
"""
import mysql.connector


try:
    print('connecting to database...')
    cnx=mysql.connector.connect(user="root",
                                password="123",
                                host="localhost",
                                database="test_database")

    print('connected successfully')

except:
    print("there is a problem with connecting to database")

finally:
    cursor=cnx.cursor()
    sql="CREATE TABLE IF NOT EXISTS employee(\
        id INT AUTO_INCREMENT PRIMARY KEY,\
        name VARCHAR(100) NOT NULL,\
        height INT,\
        weight INT\
    );"
    cursor.execute(sql)
    cnx.commit()
    # cnx.close()

# add new employee info
name="bahman"
height=75
weight=170
# insert_sql= f"INSERT INTO employee VALUES (1,'{name}', {height}, {weight})"
# insert_sql = "INSERT INTO employee (name, height, weight) VALUES (%s, %i, %i)"
# insert_sql= f"INSERT INTO employee (name, height, weight) VALUES ({name}, {height}, {weight})"

# cursor.execute(insert_sql)
# cnx.commit()

# get employees info
select_sql="select * from employee"
cursor.execute(select_sql)

# for id,name,height,weight in cursor:
#     print(f"{id} -user name: {name} and user height is: {height} with this weight: {weight}")

print("_"*75)

for row in cursor.fetchall():
    # print(row)
    print("Last Inserted ID:", cursor.lastrowid)

cnx.close()