                        #WELCOME TO TECH DREAMS STORE
         #(BASIC INSTALLATION OF DATABASE AND TABLES FOR FURHTER USES)

#==>Source Code related to establishing connection between Python & MySQL Server
import mysql.connector as ms
import time
import csv
class TechDreamsStore:
    def __init__(self):
        self.con=None
        self.cur=None
        self.pwd=None

    def establish_connection(self):
        print('=======================================================================')
        print('WELCOME TECH DREAMS STORE')
        print('BASIC INSTALLATION OF DATABASE & TABLES')
        time.sleep(1)
        print('=======================================================================')
        name = str(input('Enter Your Name: '))
        print("Hello", name, '!')
        time.sleep(0.8)

        while True:
            pwd = input("Please Enter Your SQL Password here: ")
            try:
                self.con = ms.connect(host='localhost', user='root', password=pwd)
                self.cur = self.con.cursor()
                if self.con.is_connected:
                    print("Establishing Connection", end='')
                    for i in range(0, 3):
                        time.sleep(0.8)
                        print(".", end='')
                    print()
                    time.sleep(1.2)
                    print("Connection Successful!")
                    self.pwd=pwd
                    break
            except:
                print("Checking Password", end='')
                for i in range(0, 3):
                    time.sleep(0.8)
                    print(".", end='')
                print()
                time.sleep(1.2)
                print('Password Is Wrong!')
                continue
#Source Code containing modules to create databases and tables 
tech_store=TechDreamsStore()
tech_store.establish_connection()
pwd=tech_store.pwd
con=tech_store.con
cur=tech_store.cur
def create():
    print('=======================================================================')
    print("Creating New Database",end='')
    for i in range(0,3):
        time.sleep(0.8)
        print(".",end='')
    print()
    time.sleep(1.15)
    cur.execute("Create database techdreams")
    print("Database Created Successfully!")

    con=ms.connect(host='localhost',user='root',password=pwd,database='techdreams')
    mycur=con.cursor()
    
    print("Creating Required Tables",end='')
    for i in range(0,3):
        time.sleep(0.8)
        print(".",end='')
    print()
    
    mycur.execute("Create table admin(Admin_Name varchar(100)\
                  ,Admin_Password varchar(100));")  #TABLE NAME> admin

    mycur.execute("Create table id(id varchar(100)\
                  ,password varchar(100));")  #TABLE NAME> id

    mycur.execute("Create table login(Username varchar(100)\
                  ,DateTime datetime);")  #TABLE NAME> login

    mycur.execute("Create table customer(Customer_Name varchar(100)\
                  ,Customer_PhoneNo char(100)\
                  ,Customer_Email varchar(100)\
                  ,Customer_Address varchar(500));")  #TABLE NAME> customer

    mycur.execute("Create table gpu(ItemID varchar(10)\
                  ,Brand varchar(100)\
                  ,ProductName varchar(500)\
                  ,VRAM varchar(10)\
                  ,Type varchar(100)\
                  ,Qnt varchar(10)\
                  ,Price_Per_Unit varchar(100));")  #TABLE NAME> gpu

    mycur.execute("Create table motherboard(ItemID varchar(10)\
                  ,Brand varchar(100)\
                  ,ProductName varchar(500)\
                  ,Type varchar(100)\
                  ,Socket varchar(50)\
                  ,Qnt varchar(10)\
                  ,Price_Per_Unit varchar(100));")  #TABLE NAME> motherboard

    mycur.execute("Create table ram(ItemID varchar(10)\
                  ,Brand varchar(100)\
                  ,ProductName varchar(500)\
                  ,Type varchar(100)\
                  ,Memory varchar(100)\
                  ,Clocked varchar(50)\
                  ,Qnt varchar(10)\
                  ,Price_Per_Unit varchar(100));")  #TABLE NAME> ram

    mycur.execute("Create table cpu(ItemID varchar(10)\
                  ,Brand varchar(100)\
                  ,ProductName varchar(500)\
                  ,Type varchar(100)\
                  ,Qnt varchar(10)\
                  ,Price_Per_Unit varchar(100));")  #TABLE NAME> cpu

    mycur.execute("Create table storagedevice(ItemID varchar(10)\
                  ,Brand varchar(100)\
                  ,ProductName varchar(500)\
                  ,Type varchar(100)\
                  ,Capacity varchar(50)\
                  ,Qnt varchar(10)\
                  ,Price_Per_Unit varchar(100));")
                  #TABLE NAME> storagedevice

    mycur.execute("Create table cooler(ItemID varchar(10)\
                  ,Brand varchar(100)\
                  ,ProductName varchar(500)\
                  ,Type varchar(100)\
                  ,Size varchar(50)\
                  ,Qnt varchar(10)\
                  ,Price_Per_Unit varchar(100));")  #TABLE NAME> cooler

    mycur.execute("Create table powersupply(ItemID varchar(10)\
                  ,Brand varchar(100)\
                  ,ProductName varchar(500)\
                  ,Power varchar(50)\
                  ,Qnt varchar(10)\
                  ,Price_Per_Unit varchar(100));")  #TABLE NAME> powersupply

    mycur.execute("Create table otherperipherals(ItemID varchar(10)\
                  ,Brand varchar(100)\
                  ,ProductName varchar(500)\
                  ,Type varchar(100)\
                  ,Comments varchar(500)\
                  ,Qnt varchar(10)\
                  ,Price_Per_Unit varchar(100));")  #TABLE NAME> otherperipherals

    print("Tables Created Successfully!")
    time.sleep(1.15)

    print("Inserting Data in Tables",end='')
    for i in range(0,3):
        time.sleep(0.8)
        print(".",end='')
    print()
#==============================
    f=open('adminTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into admin values(%s,%s)",tup)
        con.commit()

    f=open('idTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into id values(%s,%s)",tup)
        con.commit()

    f=open('gpuTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into gpu values(%s,%s,%s,%s,%s,%s,%s)",tup)
        con.commit()

    f=open('ramTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into ram values(%s,%s,%s,%s,%s,%s,%s,%s)",tup)
        con.commit()

    f=open('motherboardTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into motherboard values(%s,%s,%s,%s,%s,%s,%s)",tup)
        con.commit()

    f=open('cpuTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into cpu values(%s,%s,%s,%s,%s,%s)",tup)
        con.commit()

    f=open('storagedeviceTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into storagedevice values(%s,%s,%s,%s,%s,%s,%s)",tup)
        con.commit()

    f=open('powersupplyTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into powersupply values(%s,%s,%s,%s,%s,%s)",tup)
        con.commit()

    f=open('coolerTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into cooler values(%s,%s,%s,%s,%s,%s,%s)",tup)
        con.commit()

    f=open('otherperipheralsTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into otherperipherals values(%s,%s,%s,%s,%s,%s,%s)",tup)
        con.commit()

    f=open('customerTABLE.csv','r')
    csvread=csv.reader(f,delimiter=',')
    for i in csvread:
        tup=tuple(i)
        mycur.execute("insert into customer values(%s,%s,%s,%s)",tup)
        con.commit()
    
    print("Data Inserted Successfully!")
    time.sleep(1.15)

#FINAL EXECUTION OF MODULE CREATED FOR CREATING DATABASE AND TABLES
create()
print('INSTALLATION COMPLETE!')
print('=======================================================================')
exit=input("Press Any Key to Exit Installer: ")

#SQL Password(stored)
f=open('files\sqlpwd.txt','w')
f.write(pwd)
f.close()

