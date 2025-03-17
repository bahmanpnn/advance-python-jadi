import mysql.connector

print('connecting to database...')
cnx=mysql.connector.connect(user="root",
                            password="123",
                            host="localhost",
                            database="test_database")

print('connected successfully')

cursor=cnx.cursor()

# select query

sql = f"SELECT * FROM person;"
cursor.execute(sql)

for id,name,age,email in cursor:
    print(f"{id} -user name: {name} and user age is: {age} with this email: {email}")


# delete query
# delete_query=f"delete from person where name='ali' limit 3;"

# cursor.execute(delete_query)

# cnx.commit()
cnx.close()