""""
    DATABASE = MYSQL
    PROGRAMMING LANGUAGE = SQL-> STRUCTURED QUERY LANGUAGE

    relation database management system RDBMS
    1.create database
    database is a collection of tables
    tables can relate 2 each other:1to 1 ,1 to *,has a relation,is a relation

     2.create table in database
     ORM
     object relational mapping
     your objects attributes should be table column's name
     in table we have one additional column and when we call it as primary key and auto increment
     1 2 3 4 5......................

     create table Customer(
     cid int primary key auto_increment ,
     name varchar(200)
     phone varchar(20)
     email varchar(200)
     )

     3.INSERT DATA IN TABLE'john' ,'98774 32145'
     cRef = Customer( 'john' ,'98774 32145','john12@gmail.com')
     insert into Customer values(null,'john' ,'98774 32145','john12@gmail.com')

     4.LIBRARY SQL-CONNECTOR

     5.CREATE A DBHELPER WHICH WILL BE ACCESSING DATABASE

     """
import mysql.connector
     #DAO DATA ACCESS OBJECT
class DBHelper:
    def saveCustomerInDB(self, Customer):
        sql = "insert into Customer values(null,{},{},{})".format(Customer.name, Customer.phone, Customer.email)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="baljot")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(Customer.name, "saved!!")
"""
  #  def updateCustomerInDB(self, Customer):
        sql = "update Customer set name = '{}', phone = '{}', email = '{}'".format(Beta.name, Beta.phone, Beta.email)
        con = mysql.connector.connect()(user="root", password="", host="127.0.0.1", database="customer")
        cursor = con.cursor()
        con = cursor(sql)
        con.commit()
        print(Beta.name, "updation done!!")

   # def deleteCustomerInDB(self, cid):
        sql = "delete from  Customer where cid = {}".format(cid)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="data")
        cursor = con.cursor()
        con = cursor(sql)
        con.commit()
        print(cid, "delete!!")

  #  def fetchallCustomers(self, Customer):
        sql = "select * from Beta"
        sql = "select * from Customer by name asc"
        sql = "select * from Customer by the name des"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="data")
        cursor = con.cursor()
        con = cursor(sql)
        rows = cursor.fetchall()
        print(rows)

  #  def fetchOneCustomer(self, cid):
        sql = "select * from customer where cid = {}".format(cid)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="data")
        cursor = con.cursor()
        con = cursor(sql)
        row = cursor.fetchone()
        print(row)
"""
class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def showCustomerDetails(self):
        print("name: {}, phone: {}, email: {}".format(self.name, self.phone, self.email))

print("OPTIONS")
print("1.INSERT INTO CUSTOMER")
print("2.UPDATE DETAILS IN CUSTOMER")
print("3.DELETE FROM CUSTOMER")
print("4.FETCH DETAILS FROM CUSTOMER")

choice = int(input("enter ur choice:"))
if choice == 1:
    cRef= Customer(None, None, None)
    cRef.name = input("enter the name:")
    cRef.phone = input("enter the phone no:")
    cRef.email = input("enter the email:")
    cRef.showCustomerDetails()
    save = input("save the data or not(yes/no):")
    if save == "yes":
        db = DBHelper()
        db.saveCustomerInDB(cRef)
"""
        elif choice == 2:
            db = DBHelper()
            c1 = Beta(None, None, None)
            c1.cid = int(input("Enter Customer ID:"))  # we need to know which id has to be updated !!
            db.fetchallCustomers(c1.cid)
            c1.name = input("Enter Customer Name:")
            c1.phone = input("Enter Customer Phone:")
            c1.email = input("Enter Customer Email:")
            c1.showCustomerDetails()
            update = input("Would you like to Update Customer(yes/no)")
            if update == "yes":
                db.updateCustomerInDB(c1)

        elif choice == 3:
            cid = int(input("Enter Customer ID:"))
            delete = input("Would you like to Delete Customer(yes/no)")
            if delete == "yes":
                db = DBHelper()
                db.deleteCustomerInDB(cid)

        elif choice == 4:
            db = DBHelper()
            db.fetchallCustomer()

"""










