import mysql.connector

print('connecting')

# cnx=mysql.connector.connect(user="root",
#                             password="123",
#                             host="127.0.0.1",
#                             database="test_database")

# cnx=mysql.connector.connect(user="root",
#                             password="123",
#                             host="localhost",
#                             database="test_database")

cnx=mysql.connector.connect(user="myuser",
                            password="123",
                            host="",
                            database="test_database")

name='alii3'
age=25
email='aliizade@gmail.com'

# cnx._execute_query("insert into person values(3,'amir',26,\"bahmanpn3@gmail.com\");")
# cnx._execute_query('insert into person values(5,"%s","%i","%s");'%(name,age,email))
sql = f"INSERT INTO person VALUES (6, '{name}', {age}, '{email}')"
cnx._execute_query(sql)

cnx.commit()

print('connected successfully')

cnx.close()
