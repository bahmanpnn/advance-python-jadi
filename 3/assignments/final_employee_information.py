import mysql.connector


try:
    print('connecting to database...')
    cnx=mysql.connector.connect(user="root",
                                password="123",
                                host="localhost",
                                database="test_database")

    print('connected successfully')

    cursor=cnx.cursor()
    sql="CREATE TABLE IF NOT EXISTS employee(\
        id INT AUTO_INCREMENT PRIMARY KEY,\
        name VARCHAR(100) NOT NULL,\
        height INT,\
        weight INT\
    );"
    cursor.execute(sql)
    cnx.commit()

    # add new employees info
    employees = [
        ("Alice Brown", 165, 55),
        ("Bob Smith", 180, 80),
        ("Charlie Doe", 175, 72),
        ("David White", 190, 90),
        ("Emma Green", 160, 50),
        ("John Doe", 175, 78),
        ("Amir Zarei",180,78)
    ]


    sql = "INSERT INTO employee (name, height, weight) VALUES (%s, %s, %s)"
    cursor.executemany(sql, employees)
    cnx.commit()

    print("Employees inserted successfully!")
    print("_"*80)

    # fetch employees information
    cursor.execute("SELECT * FROM employee")


    employee_list=cursor.fetchall() # fetch all rows

    # Sort by height (ascending), then by weight (ascending)
    sorted_employees=sorted(employee_list,key=lambda emp:(-emp[2],emp[3]))


    # Print sorted employees
    for emp in sorted_employees:
        print(emp[1],emp[2],emp[3])


    cursor.execute("DELETE FROM employee")
    cnx.commit()

    print("_"*80)
    print("All test data deleted.")

except mysql.connector.Error as err:
    print(f"Database error: {err}")
except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'cnx' in locals():
        cnx.close()