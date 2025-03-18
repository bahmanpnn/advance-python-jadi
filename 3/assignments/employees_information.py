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

# way 1- fstring and direct string formating can cause sql injection and doesnt recommend
# for name,height,weight in employees:
#     # sql= f"INSERT INTO employee (name, height, weight) VALUES ('{name}', {height}, {weight})"
#     sql= f"INSERT INTO employee (name, height, weight) VALUES ({name!r}, {height}, {weight})"
#     cursor.execute(sql)

# way 2
sql = "INSERT INTO employee (name, height, weight) VALUES (%s, %s, %s)"
cursor.executemany(sql, employees)
cnx.commit()

print("Employees inserted successfully!")
print("_"*80)





class Employee:
    employee_list=[]
    
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
        Employee.employee_list.append(self)

    @classmethod
    def show_employees(cls):
        return cls.employee_list
    
    # def __str__(self):
    #     return f"{self.name} - {self.height} - {self.weight}"

    def __repr__(self):
        return f"{self.name} - {self.height} - {self.weight}"
    



# fetch employees information
cursor.execute("SELECT * FROM employee")


employee_list=cursor.fetchall() # fetch all rows

# Sort by height (ascending), then by weight (ascending)
sorted_employees=sorted(employee_list,key=lambda emp:(-emp[2],emp[3]))


# Print sorted employees
for emp in sorted_employees:
    # print(emp)  # (id, name, height, weight)
    # print(emp[1],emp[2],emp[3])
    Employee(emp[1],emp[2],emp[3])

# print(Employee.show_employees())

# Show all stored employees
for employee in Employee.show_employees():
    print(employee.name, employee.height, employee.weight)












cursor.execute("DELETE FROM employee")
cnx.commit()

print("_"*80)
print("All test data deleted.")

cnx.close()





"""
            
    # for row in cursor.fetchall():
    #     print(row)  # Prints (id, name, height, weight)


    # employee_list=[]
    # for row in cursor.fetchall():
    #     # print(row)  # Prints (id, name, height, weight)
    #     employee_list.append(row)

    # print(employee_list)

    cursor.execute("SELECT * FROM employee ORDER BY height DESC LIMIT 1")
    print("Tallest employee:", cursor.fetchone())

    cursor.execute("SELECT AVG(height), AVG(weight) FROM employee")
    print("Average Height & Weight:", cursor.fetchone())

    cursor.execute("SELECT * FROM employee WHERE weight > 70")
    for row in cursor.fetchall():
        print("Over 70kg:", row)



"""