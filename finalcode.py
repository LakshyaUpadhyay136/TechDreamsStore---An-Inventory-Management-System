#=====================================================================================================================
#=====================================================================================================================
import mysql.connector as ms
import datetime
import time
import matplotlib.pyplot as plt
import numpy as nm
from prettytable import *
f=open('files/sqlpwd.txt','r')
sqlpwd=f.read()
con=ms.connect(host='localhost',user='root',password=sqlpwd,database='techdreams')
mycursor=con.cursor()
con.commit()
#=====================================================================================================================
#=====================================================================================================================

#CREATE NEW USER
def createuser():
    name=input("Create Username: ")
    password=input("Create Password: ")
    s="insert into id values(%s,%s)"
    info=(name,password)
    mycursor.execute(s,info)
    con.commit()
    print('-------------')
    print("USER CREATED!")

#=======================================================================================

#SEARCH FOR EXISTING USER
def searchuser(name,password):
    mycursor.execute("select * from id")
    x=mycursor.fetchall()
    if (name,password) in x:
        s = 'insert into login values(%s,%s)'
        dt=datetime.datetime.now()
        dt=str(dt)
        dt=dt[0:19]
        a=(name,dt)
        mycursor.execute(s,a)
        con.commit()
        print('-------------')
        print("Welcome",name,end='')
        print("!")
        return(True)
    else:
        print('-------------')
        print("Invalid Username or Password!")
        return(False)

#=======================================================================================

#SEARCH FOR EXISTING ADMIN
def searchadmin(name,password):
    mycursor.execute("select * from admin")
    x=mycursor.fetchall()
    if (name,password) in x:
        print('-------------')
        print("GREETINGS",name,end='')
        print("!")
        return(True)
    else:
        print('-------------')
        print("AUTHORIZATION REVOKED!")
        return(False)

#=======================================================================================

#LOGIN SHEET
def login():
    mycursor.execute("select * from login")
    x=mycursor.fetchall()
    y=PrettyTable(['Username','Date(YYYY-MM-DD)','Time(HH:MM:SS)'])
    for i in x:
        uname=i[0]
        datetime=i[1]
        date=datetime.date()
        time=datetime.time()
        y.add_row([uname,date,time])
    print(y)

#=======================================================================================

#BILL GENERATOR
def bill():
    while True:
        phonenumber=str(input("Enter the Customer Phone Number: "))
        print('-------------')
        digitcnt=0
        for i in phonenumber:
            digitcnt+=1
        if digitcnt!=10 or phonenumber=='':
            print("Invalid Phone Number (PhoneNo disapproves 10-Digit Format!)")
            print('-------------')
            continue
        else:
            pass
        mycursor.execute("select*from customer")
        fetch=mycursor.fetchall()
        y=PrettyTable(['Customer Name','Phone Number','Email ID','Address'])
        usercnt=0
        proceed=0
        while True:
            for x in fetch:
                if phonenumber==x[1]:
                    y.add_row([x[0],x[1],x[2],x[3]])
                    custname=x[0]
                    custphone=x[1]
                    custemail=x[2]
                    custaddress=x[3]
                    usercnt+=1
                    searchcomplete=True
                    break
                else:
                    searchcomplete=False
                    pass
            if searchcomplete==False:
                state=('''No Customer with given PhoneNo. has been found in existing database!\nYou need to add the new customer to database before proceeding!''')
                for i in state:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print('-------------')
                createcust()
                while True:
                    choice1=str(input("Want to proceed towards billing? (Y/N): "))
                    print('-------------')
                    choice1=choice1.upper()
                    if choice1=='Y':
                        proceed=1
                        break
                    elif choice1=='N':
                        proceed=2
                        break
                    else:
                        print("SELECT A VALID OPTION!")
                        print('-------------')
                if proceed==1:
                    continue
                elif proceed==2:
                    break
            elif searchcomplete==True:
                break
                        
        if proceed==2:
            break
        final=0
        if usercnt>=1:
            shoppingcart=PrettyTable(['ItemID','Brand','Product','Qnt','Price(Per Unit)'])
            while True:
                statement="Select What to Purchase!"
                for j in statement:
                    print(j,end='')
                    time.sleep(0.03)
                print()
                print('-------------')
                gpuselect=str(input("Any Graphics Card? (Y/N): "))
                gpuselect=gpuselect.upper()
                if gpuselect=='Y':
                    itemid=str(input("Enter the ItemID of GPU: "))
                    mycursor.execute("select ItemID, Brand, ProductName, Price_Per_Unit from gpu where ItemID=%s",(itemid,))
                    fetchedcart=mycursor.fetchall()
                    for v in fetchedcart:
                        shop=v
                        break
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        qnt='0'
                        pass
                    mycursor.execute("update gpu set Qnt=Qnt-%s where ItemID=%s",(qnt,itemid))
                    shoppingcart.add_row([shop[0],shop[1],shop[2],qnt,shop[3]])
                    pass
                elif gpuselect=='N':
                    pass
                else:
                    print("Please Select a Valid Option!")
                    print('-------------')
                    continue
                print('-------------')
                motselect=str(input("Any Motherboards? (Y/N): "))
                motselect=motselect.upper()
                if motselect=='Y':
                    itemid=str(input("Enter the ItemID of Motherboard: "))
                    mycursor.execute("select ItemID, Brand, ProductName, Price_Per_Unit from motherboard where ItemID=%s",(itemid,))
                    fetchedcart=mycursor.fetchall()
                    for v in fetchedcart:
                        shop=v
                        break
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        qnt='0'
                        pass
                    mycursor.execute("update motherboard set Qnt=Qnt-%s where ItemID=%s",(qnt,itemid))
                    shoppingcart.add_row([shop[0],shop[1],shop[2],qnt,shop[3]])
                    pass
                elif motselect=='N':
                    pass
                else:
                    print("Please Select a Valid Option!")
                    print('-------------')
                    continue
                print('-------------')
                cpuselect=str(input("Any Processor? (Y/N): "))
                cpuselect=cpuselect.upper()
                if cpuselect=='Y':
                    itemid=str(input("Enter the ItemID of CPU: "))
                    mycursor.execute("select ItemID, Brand, ProductName, Price_Per_Unit from cpu where ItemID=%s",(itemid,))
                    fetchedcart=mycursor.fetchall()
                    for v in fetchedcart:
                        shop=v
                        break
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        qnt='0'
                        pass
                    mycursor.execute("update cpu set Qnt=Qnt-%s where ItemID=%s",(qnt,itemid))
                    shoppingcart.add_row([shop[0],shop[1],shop[2],qnt,shop[3]])
                    pass
                elif cpuselect=='N':
                    pass
                else:
                    print("Please Select a Valid Option!")
                    print('-------------')
                    continue
                print('-------------')
                ramselect=str(input("Any RAM? (Y/N): "))
                ramselect=ramselect.upper()
                if ramselect=='Y':
                    itemid=str(input("Enter the ItemID of RAM: "))
                    mycursor.execute("select ItemID, Brand, ProductName, Price_Per_Unit from ram where ItemID=%s",(itemid,))
                    fetchedcart=mycursor.fetchall()
                    for v in fetchedcart:
                        shop=v
                        break
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        qnt='0'
                        pass
                    mycursor.execute("update ram set Qnt=Qnt-%s where ItemID=%s",(qnt,itemid))
                    shoppingcart.add_row([shop[0],shop[1],shop[2],qnt,shop[3]])
                    pass
                elif ramselect=='N':
                    pass
                else:
                    print("Please Select a Valid Option!")
                    print('-------------')
                    continue
                print('-------------')
                storageselect=str(input("Any HDD/SSD/NVME? (Y/N): "))
                storageselect=storageselect.upper()
                if storageselect=='Y':
                    itemid=str(input("Enter the ItemID of HDD/SSD/NVME: "))
                    mycursor.execute("select ItemID, Brand, ProductName, Price_Per_Unit from storagedevice where ItemID=%s",(itemid,))
                    fetchedcart=mycursor.fetchall()
                    for v in fetchedcart:
                        shop=v
                        break
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        qnt='0'
                        pass
                    mycursor.execute("update storagedevice set Qnt=Qnt-%s where ItemID=%s",(qnt,itemid))
                    shoppingcart.add_row([shop[0],shop[1],shop[2],qnt,shop[3]])
                    pass
                elif storageselect=='N':
                    pass
                else:
                    print("Please Select a Valid Option!")
                    print('-------------')
                    continue
                print('-------------')
                coolerselect=str(input("Any Cooling System? (Y/N): "))
                coolerselect=coolerselect.upper()
                if coolerselect=='Y':
                    itemid=str(input("Enter the ItemID of Cooler: "))
                    mycursor.execute("select ItemID, Brand, ProductName, Price_Per_Unit from cooler where ItemID=%s",(itemid,))
                    fetchedcart=mycursor.fetchall()
                    for v in fetchedcart:
                        shop=v
                        break
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        qnt='0'
                        pass
                    mycursor.execute("update cooler set Qnt=Qnt-%s where ItemID=%s",(qnt,itemid))
                    shoppingcart.add_row([shop[0],shop[1],shop[2],qnt,shop[3]])
                    pass
                elif coolerselect=='N':
                    pass
                else:
                    print("Please Select a Valid Option!")
                    print('-------------')
                    continue
                print('-------------')
                powerselect=str(input("Any Power Supply? (Y/N): "))
                powerselect=powerselect.upper()
                if powerselect=='Y':
                    itemid=str(input("Enter the ItemID of Power Supply: "))
                    mycursor.execute("select ItemID, Brand, ProductName, Price_Per_Unit from powersupply where ItemID=%s",(itemid,))
                    fetchedcart=mycursor.fetchall()
                    for v in fetchedcart:
                        shop=v
                        break
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        qnt='0'
                        pass
                    mycursor.execute("update powersupply set Qnt=Qnt-%s where ItemID=%s",(qnt,itemid))
                    shoppingcart.add_row([shop[0],shop[1],shop[2],qnt,shop[3]])
                    pass
                elif powerselect=='N':
                    pass
                else:
                    print("Please Select a Valid Option!")
                    print('-------------')
                    continue
                print('-------------')
                otherselect=str(input("Any Other Peripherals? (Y/N): "))
                otherselect=otherselect.upper()
                if otherselect=='Y':
                    itemid=str(input("Enter the ItemID of Other Peripherals: "))
                    mycursor.execute("select ItemID, Brand, ProductName, Price_Per_Unit from otherperipherals where ItemID=%s",(itemid,))
                    fetchedcart=mycursor.fetchall()
                    for v in fetchedcart:
                        shop=v
                        break
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        qnt='0'
                        pass
                    mycursor.execute("update otherperipherals set Qnt=Qnt-%s where ItemID=%s",(qnt,itemid))
                    shoppingcart.add_row([shop[0],shop[1],shop[2],qnt,shop[3]])
                    pass
                elif otherselect=='N':
                    pass
                else:
                    print("Please Select a Valid Option!")
                    print('-------------')
                    continue
                print('-------------')
                statementbill="'Want to Proceed' OR 'Add More': "
                for i in statementbill:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print('-------------')
                print("(1) Proceed Further")
                print("(2) Add More")
                print()
                print("ON PRESSING ANY OTHER KEY BILL PROGRAM WILL >QUIT<")
                print('-------------')
                billchoice=str(input("Select one of the options(1/2): "))
                if billchoice=='2':
                    print('-------------')
                    continue
                elif billchoice=='1':
                    print("=========================================================================================================================")
                    print("TECH DREAMS BILLING".center(120))
                    print()
                    #custname
                    print("CUSTOMER NAME: ",end='')
                    for A in custname:
                        print(A,end='')
                        time.sleep(0.02)
                    print()
                    #custphone
                    print("CUSTOMER PHONE NO.: ",end='')
                    for B in custphone:
                        print(B,end='')
                        time.sleep(0.02)
                    print()
                    #custemail
                    print("CUSTOMER EMAIL: ",end='')
                    for C in custemail:
                        print(C,end='')
                        time.sleep(0.02)
                    print()
                    #custaddress
                    print("CUSTOMER ADDRESS: ",end='')
                    for A in custaddress:
                        print(A,end='')
                        time.sleep(0.02)
                    print()
                    shoppingcart.title='ORDER'
                    print(shoppingcart)
                    price=0
                    for i in shoppingcart:
                        temp=[]
                        i.title=''
                        i.header=False
                        i.border=False
                        zp=(i.get_string(fields=['Qnt']).strip())
                        yp=(i.get_string(fields=['Price(Per Unit)']).strip())
                        temp.append(zp)
                        temp.append(yp)
                        quantity=int(temp[0])
                        priceperunit=int(temp[1])
                        amount=quantity*priceperunit
                        price=price+amount
                    print("TAXABLE VALUE: ",'₹',price)
                    cgst=price*9/100
                    sgst=price*9/100
                    print("CGST(9%): ",'₹',cgst)
                    print("SGST(9%): ",'₹',sgst)
                    print("TOTAL PAY: ",'₹',price+cgst+sgst)
                    print("=========================================================================================================================")
                    while True:
                        choiceABC=str(input("Press >Enter< to Continue: "))
                        if choiceABC=='':
                            print('-------------')
                            break
                        else:
                            print('-------------')
                            continue
                    final=1

                if final==1:
                    break

                else:
                    final=1

        if final==1:
            break

#=======================================================================================

#CREATE A NEW CUSTOMER
def createcust():
    while True:
        z=str(input("Want to add new customer? (Y/N): "))
        z=z.upper()
        print('-------------')
        if z=='N':
            break
        elif z=='Y':
            customer_name=str(input("Enter Customer Name: "))
            if customer_name=='':
                print("Please Enter a Valid Name!")
                print('-------------')
                continue
            else:
                pass
            customer_phone=str(input("Enter Customer 10-digit Phone No (without +91): "))
            cnt=0
            x=customer_phone
            for i in x:
                cnt+=1
            if cnt==10:
                pass
            elif cnt=='':
                print('-------------')
                print("Invalid PhoneNo! eg:9998887776")
                print('-------------')
                continue
            else:
                print('-------------')
                print("Invalid PhoneNo! eg:9998887776")
                print('-------------')
                continue
            customer_email=str(input("Enter Customer Email (OPTIONAL): "))
            if customer_email=='':
                customer_email="NULL"
            else:
                pass
            customer_address=str(input("Enter Customer Address: "))
            if customer_address=='':
                print('-------------')
                print("Please Enter a Valid Address!")
                print('-------------')
                continue
            else:
                pass
            print('-------------')
            a=PrettyTable(['Customer Name','Phone Number','Email ID','Address'])
            a.add_row([customer_name,customer_phone,customer_email,customer_address])
            print(a)
            print('-------------')
            while True:
                choiceX=str(input("Is Above Info. Correct and Do you want to Proceed? (Y/N): "))
                choiceX=choiceX.upper()
                if choiceX=='Y':
                    x=(customer_name,customer_phone,customer_email,customer_address)
                    s='insert into customer values(%s,%s,%s,%s)'
                    mycursor.execute(s,x)
                    con.commit()
                    print("Customer Added Successfully!")
                    print('-------------')
                    break
                elif choiceX=='N':
                    break
                else:
                    print("Invalid Option! Enter (Y/N)")
                    print('-------------')
        else:
            print("Invalid Option! Enter (Y/N)")
            print('-------------')

#=======================================================================================
            
#VIEW CUSTOMERS
def viewcust():
    while True:
        state="What would you like to perform?"
        for x in state:
            print(x,end='')
            time.sleep(0.03)
        print()
        print("(1) View all Customers")
        time.sleep(0.4)
        print("(2) View a specific Customer")
        time.sleep(0.4)
        print("(3) PREVIOUS PAGE <=")
        time.sleep(0.2)
        print('-------------')
        Statement5="Select one of the options (1/2/3): "
        for g in Statement5:
            print(g,end='')
            time.sleep(0.03)
        choiceB=str(input(""))
        if choiceB=='3':
            print('-------------')
            break
        elif choiceB=='2':
            custphone=str(input("Enter the Customer 10-digit phone number: "))
            mycursor.execute("select*from customer")
            x=mycursor.fetchall()
            y=PrettyTable(['Customer Name','Phone Number','Email ID','Address'])
            for i in x:
                if i[1]==custphone:
                    y.add_row([i[0],i[1],i[2],i[3]])
                else:
                    continue
            print('-------------')
            print(y)
            print('-------------')


        elif choiceB=='1':
            mycursor.execute("select*from customer")
            x=mycursor.fetchall()
            y=PrettyTable(['Customer Name','Phone Number','Email ID','Address'])
            for i in x:
                custname=i[0]
                custphone=i[1]
                custmail=i[2]
                custaddress=i[3]
                y.add_row([custname,custphone,custmail,custaddress])
            print('-------------')
            print(y)
            print('-------------')
        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            print('-------------')
            continue

#=======================================================================================

#MODIFY CUSTOMER RECORDS
def modifycust():
    while True:
        state="What would you like to perform?"
        for x in state:
            print(x,end='')
            time.sleep(0.03)
        print()
        print("(1) Update Customer Name")
        time.sleep(0.4)
        print("(2) Update Customer Phone Number")
        time.sleep(0.4)
        print("(3) Update Customer Email-ID")
        time.sleep(0.4)
        print("(4) Update Customer Address")
        time.sleep(0.4)
        print("(5) PREVIOUS PAGE <=")
        time.sleep(0.2)
        print('-------------')
        StatementA="Select one of the options (1/2/3/4/5): "
        for g in StatementA:
            print(g,end='')
            time.sleep(0.03)
        choiceC=str(input(""))
        if choiceC=='1':
            print('-------------')
            custphone=str(input("Enter the Customer 10-digit phone number (existing): "))
            mycursor.execute("select Customer_PhoneNo from customer where Customer_PhoneNo=(%s)",(custphone,))
            check=mycursor.fetchall()
            if(check==[]):
                print("No data with given phone number has been found!")
            elif(check[0][0]==custphone):
                newname=str(input("Enter New Name: "))
                mycursor.execute("update customer set Customer_Name=(%s) where Customer_PhoneNo=(%s)",(newname,custphone))
                con.commit()
                print("Customer Name has been Updated!")
            else:
                print("No data with given phone number has been found!")
            print('-------------')

        elif choiceC=='2':
            print('-------------')
            custphone=str(input("Enter the Customer 10-digit phone number (existing): "))
            mycursor.execute("select Customer_PhoneNo from customer where Customer_PhoneNo=(%s)",(custphone,))
            check=mycursor.fetchall()
            if(check==[]):
                print("No data with given phone number has been found!")
            elif(check[0][0]==custphone):
                newphone=str(input("Enter New Phone Number: "))
                mycursor.execute("update customer set Customer_PhoneNo=(%s) where Customer_PhoneNo=(%s)",(newphone,custphone))
                con.commit()
                print("Customer PhoneNumber has been Updated!")
            else:
                print("No data with given phone number has been found!")
            print('-------------')

        elif choiceC=='3':
            print('-------------')
            custphone=str(input("Enter the Customer 10-digit phone number (existing): "))
            mycursor.execute("select Customer_PhoneNo from customer where Customer_PhoneNo=(%s)",(custphone,))
            check=mycursor.fetchall()
            if(check==[]):
                print("No data with given phone number has been found!")
            elif(check[0][0]==custphone):
                newmail=str(input("Enter New Email: "))
                mycursor.execute("update customer set Customer_Email=(%s) where Customer_PhoneNo=(%s)",(newmail,custphone))
                con.commit()
                print("Customer Email has been Updated!")
            else:
                print("No data with given phone number has been found!")
            print('-------------')

        elif choiceC=='4':
            print('-------------')
            custphone=str(input("Enter the Customer 10-digit phone number (existing): "))
            mycursor.execute("select Customer_PhoneNo from customer where Customer_PhoneNo=(%s)",(custphone,))
            check=mycursor.fetchall()
            if(check==[]):
                print("No data with given phone number has been found!")
            elif(check[0][0]==custphone):
                newaddress=str(input("Enter New Address: "))
                mycursor.execute("update customer set Customer_Address=(%s) where Customer_PhoneNo=(%s)",(newaddress,custphone))
                con.commit()
                print("Customer Address has been Updated!")
            else:
                print("No data with given phone number has been found!")
            print('-------------')

        elif choiceC=='5':
            print('-------------')
            break
        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            print('-------------')
            continue

#=======================================================================================

#DELETE CUSTOMER
def delcust():
    while True:
        custphone=str(input("Enter the Customer 10-digit phone number: "))
        mycursor.execute("select*from customer")
        x=mycursor.fetchall()
        cnt=0
        for i in x:
            if i[1]==custphone:
                s="delete from customer where Customer_PhoneNo=(%s)"
                mycursor.execute(s,(custphone,))
                con.commit()
                cnt+=1
            else:
                continue
        if cnt==0:
            print("No record found assoicated with the phone number!")
            print('-------------')
            break
        elif cnt>=1:
            print("Record(s) Successfully Deleted!")
            print('-------------')
            break

#=======================================================================================

#CHANGE ADMIN PASSWORD
def changeadminpass():
    while True:
        adminname=str(input("Enter Admin Name: "))
        adminpassword=str(input("Enter Old Password: "))
        mycursor.execute("select*from admin")
        x=mycursor.fetchall()
        if (adminname,adminpassword) in x:
            newpassword=str(input("Enter New Password: "))
            print('-------------')
            ch=str(input("ARE YOU SURE YOU WANT TO PROCEED(Y/N): "))
            ch=ch.upper()
            if ch=='Y':
                mycursor.execute("update admin set Admin_Password=(%s) where Admin_Name=(%s)",(newpassword,adminname))
                con.commit()
                print("Password has been Updated!")
                print('-------------')
                break
            elif ch=='N':
                print('-------------')
                break
            else:
                print('-------------')
                print('PROCESS STOPPED! INVALID OPTION SELECTED!')
                break
        else:
            print("Invalid Admin Name or Password!")
            print('-------------')
            break

#=======================================================================================

#DELETE A USER
def deluser():
    username=str(input("Enter the Username: "))
    userpass=str(input("Enter the User's Password: "))
    mycursor.execute("select*from id")
    x=mycursor.fetchall()
    cnt=0
    for i in x:
        if i[1]==userpass and i[0]==username:
            print('-------------')
            statement="Are You Sure? (Y/N): "
            for i in statement:
                print(i,end='')
                time.sleep(0.03)
            ch=str(input(""))
            ch=ch.upper()
            if ch=='Y':
                s="delete from id where password=(%s)"
                mycursor.execute(s,(userpass,))
                con.commit()
                print("User(s) Successfully Deleted!")
                cnt=1
                break
            elif ch=='N':
                cnt=1
                break
            else:
                print('-------------')
                print("SELECT A VALID OPTION!")
                cnt=1
                break
        else:
            continue
    if cnt==0:
        print("No user found with given details!")
#=======================================================================================

#VIEW EXISTING USER(S)
def viewuser():
    while True:
        state="What would you like to perform?"
        for x in state:
            print(x,end='')
            time.sleep(0.03)
        print()
        print("(1) View all Users")
        time.sleep(0.4)
        print("(2) View a specific User")
        time.sleep(0.4)
        print("(3) PREVIOUS PAGE <=")
        time.sleep(0.2)
        print('-------------')
        Statement5="Select one of the options (1/2/3): "
        for g in Statement5:
            print(g,end='')
            time.sleep(0.03)
        choiceB=str(input(""))
        if choiceB=='3':
            break
        elif choiceB=='2':
            username=str(input("Enter the Username: "))
            mycursor.execute("select*from id")
            x=mycursor.fetchall()
            y=PrettyTable(['Username','Password'])
            for i in x:
                if i[0]==username:
                    y.add_row([i[0],i[1]])
                else:
                    continue
            print('-------------')
            print(y)
            print('-------------')


        elif choiceB=='1':
            mycursor.execute("select*from id")
            x=mycursor.fetchall()
            y=PrettyTable(['Username','Password'])
            for i in x:
                username=i[0]
                userpass=i[1]
                y.add_row([username,userpass])
            print('-------------')
            print(y)
            print('-------------')
        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            print('-------------')
            continue

#=======================================================================================

#EDIT USER DETAILS
def edituser():
    while True:
        print('-------------')
        state="Choose what to perform?"
        for i in state:
            print(i,end='')
            time.sleep(0.03)
        print()
        print("(1) Change Username/Password")
        time.sleep(0.2)
        print("(2) PREVIOUS PAGE <=")
        time.sleep(0.2)
        print('-------------')
        Statement="Select one of the options (1/2): "
        for j in Statement:
            print(j,end='')
            time.sleep(0.03)
        choiceB=str(input(""))
        if choiceB=='2':
            print('-------------')
            break
        elif choiceB=='1':
            oldusername=str(input("Enter Existing Username: "))
            oldpassword=str(input("Enter Existing Password: "))
            mycursor.execute("Select*from id")
            x=mycursor.fetchall()
            a=(oldusername,oldpassword)
            if a in x:
                newusername=str(input("Enter New Username: "))
                newpassword=str(input("Enter New Password: "))
                z=(newusername,newpassword)
                if z in x:
                    print("This Username is already taken!")
                    continue
                elif z not in x:
                    mycursor.execute("delete from id where id=%s",(oldusername,))
                    con.commit()
                    mycursor.execute("insert into id values(%s,%s)",(z))
                    con.commit()
                    print("User Record Successfully Edited!")
                    print('-------------')
                    break
            else:
                print("Entered Information about Username 'or' Password is Wrong!")
                continue

        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            continue
#=======================================================================================

#INVENTORY

#1. SORTED
def sortedinventory():
    while True:
        state="Choose what Category to View?"
        for x in state:
            print(x,end='')
            time.sleep(0.03)
        print()
        print("(1) Graphic Cards")
        time.sleep(0.2)
        print("(2) Motherboards")
        time.sleep(0.2)
        print("(3) Processors")
        time.sleep(0.2)
        print("(4) RAM")
        time.sleep(0.2)
        print("(5) HDD/SSD/NVME")
        time.sleep(0.2)
        print("(6) CPU Coolers")
        time.sleep(0.2)
        print("(7) Power Supply")
        time.sleep(0.2)
        print("(8) Other Peripherals")
        time.sleep(0.2)
        print("(9) PREVIOUS PAGE <=")
        time.sleep(0.2)
        print('-------------')
        Statement="Select one of the options (1/2/3/4/5/6/7/8/9): "
        for g in Statement:
            print(g,end='')
            time.sleep(0.03)
        choiceB=str(input(""))
        if choiceB=='9':
            print('-------------')
            break

        elif choiceB=='1':
            mycursor.execute("select*from GPU order by Type,Brand")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','VRAM','Type','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='2':
            mycursor.execute("select*from motherboard order by Socket,Type,Brand")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Socket','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='5':
            mycursor.execute("select*from storagedevice order by Type,Capacity,Brand")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Capacity','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='4':
            mycursor.execute("select*from RAM order by Memory,Type,Clocked")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Memory','Clock Speed','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='3':
            mycursor.execute("select*from CPU order by Brand,Type")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='6':
            mycursor.execute("select*from cooler order by Type,Size,Brand")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Size','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='7':
            mycursor.execute("select*from powersupply order by Power,Brand")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Power','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='8':
            mycursor.execute("select*from otherperipherals order by Type,Brand")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Comments','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            print('-------------')
            continue

#2. ACTUALORDERWISE
def actualinventory():
    while True:
        state="Choose what Category to View?"
        for x in state:
            print(x,end='')
            time.sleep(0.03)
        print()
        print("(1) Graphic Cards")
        time.sleep(0.2)
        print("(2) Motherboards")
        time.sleep(0.2)
        print("(3) Processors")
        time.sleep(0.2)
        print("(4) RAM")
        time.sleep(0.2)
        print("(5) HDD/SSD/NVME")
        time.sleep(0.2)
        print("(6) CPU Coolers")
        time.sleep(0.2)
        print("(7) Power Supply")
        time.sleep(0.2)
        print("(8) Other Peripherals")
        time.sleep(0.2)
        print("(9) PREVIOUS PAGE <=")
        time.sleep(0.2)
        print('-------------')
        Statement="Select one of the options (1/2/3/4/5/6/7/8/9): "
        for g in Statement:
            print(g,end='')
            time.sleep(0.03)
        choiceB=str(input(""))
        if choiceB=='9':
            print('-------------')
            break

        elif choiceB=='1':
            mycursor.execute("select*from GPU order by ItemID")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','VRAM','Type','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='2':
            mycursor.execute("select*from motherboard order by ItemID")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Socket','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='5':
            mycursor.execute("select*from storagedevice order by ItemID")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Capacity','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='4':
            mycursor.execute("select*from RAM order by ItemID")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Memory','Clock Speed','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='3':
            mycursor.execute("select*from CPU order by ItemID")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='6':
            mycursor.execute("select*from cooler order by ItemID")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Size','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='7':
            mycursor.execute("select*from powersupply order by ItemID")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Power','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
            print('-------------')
            print(y)
            print('-------------')

        elif choiceB=='8':
            mycursor.execute("select*from otherperipherals order by ItemID")
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Comments','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print('-------------')
            print(y)
            print('-------------')

        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            print('-------------')
            continue

#Visual Inventory
def visualinventory():
    while True:
        state="Choose what Category to View?"
        for x in state:
            print(x,end='')
            time.sleep(0.03)
        print()
        print("(1) Graphic Cards")
        time.sleep(0.2)
        print("(2) Motherboards")
        time.sleep(0.2)
        print("(3) Processors")
        time.sleep(0.2)
        print("(4) RAM")
        time.sleep(0.2)
        print("(5) HDD/SSD/NVME")
        time.sleep(0.2)
        print("(6) CPU Coolers")
        time.sleep(0.2)
        print("(7) Power Supply")
        time.sleep(0.2)
        print("(8) Other Peripherals")
        time.sleep(0.2)
        print("(9) PREVIOUS PAGE <=")
        time.sleep(0.2)
        print('-------------')
        Statement="Select one of the options (1/2/3/4/5/6/7/8/9): "
        for g in Statement:
            print(g,end='')
            time.sleep(0.03)
        choiceB=str(input(""))
        if choiceB=='9':
            print('-------------')
            break

        elif choiceB=='1':
            mycursor.execute("select Brand, SUM(Qnt) as Total_Units from GPU group by Brand")
            x=mycursor.fetchall()
            Qnt=[]
            Brand=[]
            chart_ex=[]
            for i in x:
                Brand.append(i[0])
                Qnt.append(int(i[1]))
                chart_ex.append(0.01)
            #plt.style.use("fivethirtyeight")
            plt.pie(Qnt,labels=Brand,autopct="%0.2f%%",shadow={'ox':-0.01,'oy':-0.01,'edgecolor':'none','shade':1},radius=1,textprops={"fontsize":10},wedgeprops=None)
            plt.title(label="GPU Units Distribution",fontsize=20)
            plt.tight_layout()
            plt.legend(title="Brands",bbox_to_anchor=(1,1),loc="upper left")
            plt.show()
            print('-------------')

        elif choiceB=='2':
            mycursor.execute("select Brand, SUM(Qnt) as Total_Units from motherboard group by Brand")
            x=mycursor.fetchall()
            Qnt=[]
            Brand=[]
            chart_ex=[]
            for i in x:
                Brand.append(i[0])
                Qnt.append(int(i[1]))
                chart_ex.append(0.01)
            #plt.style.use("fivethirtyeight")
            plt.pie(Qnt,labels=Brand,autopct="%0.2f%%",shadow={'ox':-0.01,'oy':-0.01,'edgecolor':'none','shade':1},radius=1,textprops={"fontsize":10},wedgeprops=None)
            plt.title(label="MotherBoard Units Distribution",fontsize=20)
            plt.tight_layout()
            plt.legend(title="Brands",bbox_to_anchor=(1,1),loc="upper left")
            plt.show()
            print('-------------')

        elif choiceB=='5':
            mycursor.execute("select Brand, SUM(Qnt) as Total_Units from storagedevice group by Brand")
            x=mycursor.fetchall()
            Qnt=[]
            Brand=[]
            chart_ex=[]
            for i in x:
                Brand.append(i[0])
                Qnt.append(int(i[1]))
                chart_ex.append(0.01)
            #plt.style.use("fivethirtyeight")
            plt.pie(Qnt,labels=Brand,autopct="%0.2f%%",shadow={'ox':-0.01,'oy':-0.01,'edgecolor':'none','shade':1},radius=1,textprops={"fontsize":10},wedgeprops=None)
            plt.title(label="StorageDevice Units Distribution",fontsize=20)
            plt.tight_layout()
            plt.legend(title="Brands",bbox_to_anchor=(1,1),loc="upper left")
            plt.show()
            print('-------------')

        elif choiceB=='4':
            mycursor.execute("select Brand, SUM(Qnt) as Total_Units from ram group by Brand")
            x=mycursor.fetchall()
            Qnt=[]
            Brand=[]
            chart_ex=[]
            for i in x:
                Brand.append(i[0])
                Qnt.append(int(i[1]))
                chart_ex.append(0.01)
            #plt.style.use("fivethirtyeight")
            plt.pie(Qnt,labels=Brand,autopct="%0.2f%%",shadow={'ox':-0.01,'oy':-0.01,'edgecolor':'none','shade':1},radius=1,textprops={"fontsize":10},wedgeprops=None)
            plt.title(label="MotherBoard Units Distribution",fontsize=20)
            plt.tight_layout()
            plt.legend(title="Brands",bbox_to_anchor=(1,1),loc="upper left")
            plt.show()
            print('-------------')

        elif choiceB=='3':
            mycursor.execute("select Brand, SUM(Qnt) as Total_Units from cpu group by Brand")
            x=mycursor.fetchall()
            Qnt=[]
            Brand=[]
            chart_ex=[]
            for i in x:
                Brand.append(i[0])
                Qnt.append(int(i[1]))
                chart_ex.append(0.01)
            #plt.style.use("fivethirtyeight")
            plt.pie(Qnt,labels=Brand,autopct="%0.2f%%",shadow={'ox':-0.01,'oy':-0.01,'edgecolor':'none','shade':1},radius=1,textprops={"fontsize":10},wedgeprops=None)
            plt.title(label="CPU Units Distribution",fontsize=20)
            plt.tight_layout()
            plt.legend(title="Brands",bbox_to_anchor=(1,1),loc="upper left")
            plt.show()
            print('-------------')

        elif choiceB=='6':
            mycursor.execute("select Brand, SUM(Qnt) as Total_Units from cooler group by Brand")
            x=mycursor.fetchall()
            Qnt=[]
            Brand=[]
            chart_ex=[]
            for i in x:
                Brand.append(i[0])
                Qnt.append(int(i[1]))
                chart_ex.append(0.01)
            #plt.style.use("fivethirtyeight")
            plt.pie(Qnt,labels=Brand,autopct="%0.2f%%",shadow={'ox':-0.01,'oy':-0.01,'edgecolor':'none','shade':1},radius=1,textprops={"fontsize":10},wedgeprops=None)
            plt.title(label="Cooler Units Distribution",fontsize=20)
            plt.tight_layout()
            plt.legend(title="Brands",bbox_to_anchor=(1,1),loc="upper left")
            plt.show()
            print('-------------')

        elif choiceB=='7':
            mycursor.execute("select Brand, SUM(Qnt) as Total_Units from powersupply group by Brand")
            x=mycursor.fetchall()
            Qnt=[]
            Brand=[]
            chart_ex=[]
            for i in x:
                Brand.append(i[0])
                Qnt.append(int(i[1]))
                chart_ex.append(0.01)
            #plt.style.use("fivethirtyeight")
            plt.pie(Qnt,labels=Brand,autopct="%0.2f%%",shadow={'ox':-0.01,'oy':-0.01,'edgecolor':'none','shade':1},radius=1,textprops={"fontsize":10},wedgeprops=None)
            plt.title(label="PowerSupply Units Distribution",fontsize=20)
            plt.tight_layout()
            plt.legend(title="Brands",bbox_to_anchor=(1,1),loc="upper left")
            plt.show()
            print('-------------')

        elif choiceB=='8':
            mycursor.execute("select Brand, SUM(Qnt) as Total_Units from otherperipherals group by Brand")
            x=mycursor.fetchall()
            Qnt=[]
            Brand=[]
            chart_ex=[]
            for i in x:
                Brand.append(i[0])
                Qnt.append(int(i[1]))
                chart_ex.append(0.01)
            #plt.style.use("fivethirtyeight")
            plt.pie(Qnt,labels=Brand,autopct="%0.2f%%",shadow={'ox':-0.01,'oy':-0.01,'edgecolor':'none','shade':1},radius=1,textprops={"fontsize":10},wedgeprops=None)
            plt.title(label="OtherPerihperals Units Distribution",fontsize=20)
            plt.tight_layout()
            plt.legend(title="Brands",bbox_to_anchor=(1,1),loc="upper left")
            plt.show()
            print('-------------')

        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            print('-------------')
            continue
#=======================================================================================

#ADD PRODUCT/STOCKS
def addproducts():
    while True:
        print('-------------')
        a="Choose Category of the New Product!"
        for i in a:
            print(i,end='')
            time.sleep(0.03)
        print()
        print("(1) Graphic Cards")
        time.sleep(0.2)
        print("(2) Motherboards")
        time.sleep(0.2)
        print("(3) Processors")
        time.sleep(0.2)
        print("(4) RAM")
        time.sleep(0.2)
        print("(5) HDD/SSD/NVME")
        time.sleep(0.2)
        print("(6) CPU Coolers")
        time.sleep(0.2)
        print("(7) Power Supply")
        time.sleep(0.2)
        print("(8) Other Peripherals")
        time.sleep(0.2)
        print("(9) PREVIOUS PAGE <=")
        time.sleep(0.2)
        print('-------------')
        StatementZ="Select one of the options (1/2/3/4/5/6/7/8/9): "
        for j in StatementZ:
            print(j,end='')
            time.sleep(0.03)
        choiceZ=str(input(""))
        if choiceZ=='9':
            print('-------------')
            break
        
        elif choiceZ=='1':
            print('-------------')
            itemid=str(input("Enter Item ID eg(G101,G102): "))
            if itemid=='':
                print("Please Enter a Valid Item ID!")
                continue
            else:
                pass
            brand=str(input("Enter Brand eg(ASUS,ZOTAC)): "))
            if brand=='':
                print("Please Enter a Valid Brand!")
                continue
            else:
                pass
            productname=str(input("Enter ProductName eg(MSI Ventus GeForce RTX 3080Ti OC Edition): "))
            if productname=='':
                print("Please Enter a Valid Name!")
                continue
            else:
                pass
            vram=str(input("Enter VRAM Amount eg(12 GB)): "))
            if vram=='':
                print("Please Enter a Valid VRAM Amount!")
                continue
            else:
                pass
            Type=str(input("Enter Type of Product eg(3080Ti, RX570, 3090)): "))
            if Type=='':
                print("Please Enter a Valid Product Type!")
                continue
            else:
                pass
            qnt=str(input("Enter Quantity eg(0,1,71,8): "))
            if qnt=='':
                print("Please Enter a Valid Quantity!")
                continue
            else:
                pass
            price=str(input("Enter Price(Per unit) of Product eg(145000,72000): "))
            if price=='':
                print("Please Enter a Valid Price!")
                continue
            else:
                pass
            print('-------------')
            s=(itemid,brand,productname,vram,Type,qnt,price)
            ch=str(input("Are you Sure (Y/N): "))
            ch=ch.upper()
            if ch=='Y':
                mycursor.execute("insert into gpu values((%s),(%s),(%s),(%s),(%s),(%s),(%s))",s)
                con.commit()
                print("RECORD ADDED SUCCESSFULLY!")
                print('-------------')
                break
            elif ch=='N':
                print('-------------')
                break
            
            else:
                print('-------------')
                print('SELECT A VALID OPTION!')
                continue
            
        elif choiceZ=='2':
            print('-------------')
            itemid=str(input("Enter Item ID eg(M101,M102): "))
            if itemid=='':
                print("Please Enter a Valid Item ID!")
                continue
            else:
                pass
            brand=str(input("Enter Brand eg(ASUS,MSI)): "))
            if brand=='':
                print("Please Enter a Valid Brand!")
                continue
            else:
                pass
            productname=str(input("Enter ProductName eg(MSI MAG B560M Tomahawk 'or' GigaByte B450 AORUS ELITE): "))
            if productname=='':
                print("Please Enter a Valid Name!")
                continue
            else:
                pass
            Type=str(input("Enter Type of Product eg(H410, B560, B560M): "))
            if Type=='':
                print("Please Enter a Valid Product Type!")
                continue
            else:
                pass
            socket=str(input("Enter Socket Type eg(LGA1200,LGA1700,AM4): "))
            if socket=='':
                print("Please Enter a Valid SOCKET!")
                continue
            else:
                pass
            qnt=str(input("Enter Quantity eg(0,1,71,8): "))
            if qnt=='':
                print("Please Enter a Valid Quantity!")
                continue
            else:
                pass
            price=str(input("Enter Price(Per unit) of Product eg(16000,42000): "))
            if price=='':
                print("Please Enter a Valid Price!")
                continue
            else:
                pass
            print('-------------')
            s=(itemid,brand,productname,Type,socket,qnt,price)
            ch=str(input("Are you Sure (Y/N): "))
            ch=ch.upper()
            if ch=='Y':
                mycursor.execute("insert into motherboard values((%s),(%s),(%s),(%s),(%s),(%s),(%s))",s)
                con.commit()
                print("RECORD ADDED SUCCESSFULLY!")
                print('-------------')
                break
            elif ch=='N':
                print('-------------')
                break
            
            else:
                print('-------------')
                print('SELECT A VALID OPTION!')
                continue
        elif choiceZ=='3':
            print('-------------')
            itemid=str(input("Enter Item ID eg(C101,C102): "))
            if itemid=='':
                print("Please Enter a Valid Item ID!")
                continue
            else:
                pass
            brand=str(input("Enter Brand eg(Intel or AMD)): "))
            if brand=='':
                print("Please Enter a Valid Brand!")
                continue
            else:
                pass
            productname=str(input("Enter ProductName eg(Intel Core i5 11400F 'or' AMD Ryzen 5 3600X): "))
            if productname=='':
                print("Please Enter a Valid Name!")
                continue
            else:
                pass
            Type=str(input("Enter Type of Product eg(Core i5, Ryzen 5, Core i7): "))
            if Type=='':
                print("Please Enter a Valid Product Type!")
                continue
            else:
                pass
            qnt=str(input("Enter Quantity eg(0,1,71,8): "))
            if qnt=='':
                print("Please Enter a Valid Quantity!")
                continue
            else:
                pass
            price=str(input("Enter Price(Per unit) of Product eg(15800,32000): "))
            if price=='':
                print("Please Enter a Valid Price!")
                continue
            else:
                pass
            print('-------------')
            s=(itemid,brand,productname,Type,qnt,price)
            ch=str(input("Are you Sure (Y/N): "))
            ch=ch.upper()
            if ch=='Y':
                mycursor.execute("insert into cpu values((%s),(%s),(%s),(%s),(%s),(%s))",s)
                con.commit()
                print("RECORD ADDED SUCCESSFULLY!")
                print('-------------')
                break
            elif ch=='N':
                print('-------------')
                break
            else:
                print('-------------')
                print('SELECT A VALID OPTION!')
                continue
        elif choiceZ=='4':
            print('-------------')
            itemid=str(input("Enter Item ID eg(R101,R102): "))
            if itemid=='':
                print("Please Enter a Valid Item ID!")
                continue
            else:
                pass
            brand=str(input("Enter Brand eg(Corsair or HyperX)): "))
            if brand=='':
                print("Please Enter a Valid Brand!")
                continue
            else:
                pass
            productname=str(input("Enter ProductName eg(Corsair Vengeance): "))
            if productname=='':
                print("Please Enter a Valid Name!")
                continue
            else:
                pass
            Type=str(input("Enter Type of Product eg(DDR4, DDR5): "))
            if Type=='':
                print("Please Enter a Valid Product Type!")
                continue
            else:
                pass
            memory=str(input("Enter Memory type eg(8 GB, 16 GB): "))
            if Type=='':
                print("Please Enter a Valid Memory Type!")
                continue
            else:
                pass
            clockspeed=str(input("Enter RAM Frequency eg(3600MHz): "))
            if Type=='':
                print("Please Enter a Valid Product Type!")
                continue
            else:
                pass
            qnt=str(input("Enter Quantity eg(0,1,71,8): "))
            if qnt=='':
                print("Please Enter a Valid Quantity!")
                continue
            else:
                pass
            price=str(input("Enter Price(Per unit) of Product eg(5800,3000): "))
            if price=='':
                print("Please Enter a Valid Price!")
                continue
            else:
                pass
            print('-------------')
            s=(itemid,brand,productname,Type,memory,clockspeed,qnt,price)
            ch=str(input("Are you Sure (Y/N): "))
            ch=ch.upper()
            if ch=='Y':
                mycursor.execute("insert into ram values((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))",s)
                con.commit()
                print("RECORD ADDED SUCCESSFULLY!")
                print('-------------')
                break
            elif ch=='N':
                print('-------------')
                break   
            else:
                print('-------------')
                print('SELECT A VALID OPTION!')
                continue
        elif choiceZ=='5':
            print('-------------')
            itemid=str(input("Enter Item ID eg(S101,S102): "))
            if itemid=='':
                print("Please Enter a Valid Item ID!")
                continue
            else:
                pass
            brand=str(input("Enter Brand eg(WD, Kingston)): "))
            if brand=='':
                print("Please Enter a Valid Brand!")
                continue
            else:
                pass
            productname=str(input("Enter ProductName eg(WD SN550 Blue NVME): "))
            if productname=='':
                print("Please Enter a Valid Name!")
                continue
            else:
                pass
            Type=str(input("Enter Type of Product eg(HDD/SSD/NVME): "))
            if Type=='':
                print("Please Enter a Valid Product Type!")
                continue
            else:
                pass
            capacity=str(input("Enter Capacity eg(250 GB, 1 TB): "))
            if capacity=='':
                print("Please Enter a Valid Capacity!")
                continue
            else:
                pass
            qnt=str(input("Enter Quantity eg(0,1,71,8): "))
            if qnt=='':
                print("Please Enter a Valid Quantity!")
                continue
            else:
                pass
            price=str(input("Enter Price(Per unit) of Product eg(5800,3000): "))
            if price=='':
                print("Please Enter a Valid Price!")
                continue
            else:
                pass
            print('-------------')
            s=(itemid,brand,productname,Type,capacity,qnt,price)
            ch=str(input("Are you Sure (Y/N): "))
            ch=ch.upper()
            if ch=='Y':
                mycursor.execute("insert into storagedevice values((%s),(%s),(%s),(%s),(%s),(%s),(%s))",s)
                con.commit()
                print("RECORD ADDED SUCCESSFULLY!")
                print('-------------')
                break
            elif ch=='N':
                print('-------------')
                break
            else:
                print('-------------')
                print('SELECT A VALID OPTION!')
                continue
        elif choiceZ=='6':
            print('-------------')
            itemid=str(input("Enter Item ID eg(CL101,CL102): "))
            if itemid=='':
                print("Please Enter a Valid Item ID!")
                continue
            else:
                pass
            brand=str(input("Enter Brand eg(Deepcool, LianLi, CoolerMaster)): "))
            if brand=='':
                print("Please Enter a Valid Brand!")
                continue
            else:
                pass
            productname=str(input("Enter ProductName eg(CoolerMaster ML240L RGB V2 AIO): "))
            if productname=='':
                print("Please Enter a Valid Name!")
                continue
            else:
                pass
            Type=str(input("Enter Type of Product eg(Air, AIO): "))
            if Type=='':
                print("Please Enter a Valid Product Type!")
                continue
            else:
                pass
            size=str(input("Enter Size of Cooler eg(120mm, 240mm, 360mm): "))
            if size=='':
                print("Please Enter a Valid Size!")
                continue
            else:
                pass
            qnt=str(input("Enter Quantity eg(0,1,71,8): "))
            if qnt=='':
                print("Please Enter a Valid Quantity!")
                continue
            else:
                pass
            price=str(input("Enter Price(Per unit) of Product eg(5800,13000): "))
            if price=='':
                print("Please Enter a Valid Price!")
                continue
            else:
                pass
            print('-------------')
            s=(itemid,brand,productname,Type,size,qnt,price)
            ch=str(input("Are you Sure (Y/N): "))
            ch=ch.upper()
            if ch=='Y':
                mycursor.execute("insert into cooler values((%s),(%s),(%s),(%s),(%s),(%s),(%s))",s)
                con.commit()
                print("RECORD ADDED SUCCESSFULLY!")
                print('-------------')
                break
            elif ch=='N':
                print('-------------')
                break
            else:
                print('-------------')
                print('SELECT A VALID OPTION!')
                continue
        elif choiceZ=='7':
            print('-------------')
            itemid=str(input("Enter Item ID eg(P101,P102): "))
            if itemid=='':
                print("Please Enter a Valid Item ID!")
                continue
            else:
                pass
            brand=str(input("Enter Brand eg(Antec, Cooler Master)): "))
            if brand=='':
                print("Please Enter a Valid Brand!")
                continue
            else:
                pass
            productname=str(input("Enter ProductName eg(Cooler Master MWE 550 Bronze V2 Certified): "))
            if productname=='':
                print("Please Enter a Valid Name!")
                continue
            else:
                pass
            power=str(input("Enter Power eg(550W, 650W): "))
            if power=='':
                print("Please Enter a Valid PowerWatt!")
                continue
            else:
                pass
            qnt=str(input("Enter Quantity eg(0,1,18): "))
            if qnt=='':
                print("Please Enter a Valid Quantity!")
                continue
            else:
                pass
            price=str(input("Enter Price(Per unit) of Product eg(3800,4000): "))
            if price=='':
                print("Please Enter a Valid Price!")
                continue
            else:
                pass
            print('-------------')
            s=(itemid,brand,productname,power,qnt,price)
            ch=str(input("Are you Sure (Y/N): "))
            ch=ch.upper()
            if ch=='Y':
                mycursor.execute("insert into powersupply values((%s),(%s),(%s),(%s),(%s),(%s))",s)
                con.commit()
                print("RECORD ADDED SUCCESSFULLY!")
                print('-------------')
                break
            elif ch=='N':
                print('-------------')
                break
            else:
                print('-------------')
                print('SELECT A VALID OPTION!')
                continue
        elif choiceZ=='8':
            print('-------------')
            itemid=str(input("Enter Item ID eg(OT101,OT102): "))
            if itemid=='':
                print("Please Enter a Valid Item ID!")
                continue
            else:
                pass
            brand=str(input("Enter Brand eg(Deepcool, CoolerMaster)): "))
            if brand=='':
                print("Please Enter a Valid Brand!")
                continue
            else:
                pass
            productname=str(input("Enter ProductName eg(Deepcool Maccube 110 Cabinet): "))
            if productname=='':
                print("Please Enter a Valid Name!")
                continue
            else:
                pass
            comments=str(input("Enter comments(if any 'or skip by  pressing enter'): "))
            if comments=='':
                comments='NULL'
                pass
            else:
                pass
            qnt=str(input("Enter Quantity eg(0,1,83): "))
            if qnt=='':
                print("Please Enter a Valid Quantity!")
                continue
            else:
                pass
            price=str(input("Enter Price(Per unit) of Product eg(3800,4000): "))
            if price=='':
                print("Please Enter a Valid Price!")
                continue
            else:
                pass
            print('-------------')
            s=(itemid,brand,productname,Type,comments,qnt,price)
            ch=str(input("Are you Sure (Y/N): "))
            ch=ch.upper()
            if ch=='Y':
                mycursor.execute("insert into otherperipherals values((%s),(%s),(%s),(%s),(%s),(%s),(%s))",s)
                con.commit()
                print("RECORD ADDED SUCCESSFULLY!")
                print('-------------')
                break
            elif ch=='N':
                print('-------------')
                break
            else:
                print('-------------')
                print('SELECT A VALID OPTION!')
                continue
        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            continue

#=======================================================================================

#MODIFY EXISITING PRODUCT/STOCKS
def modifyproducts():
    while True:
        print('-------------')
        a="Choose Category of the Product!"
        for i in a:
            print(i,end='')
            time.sleep(0.03)
        print()
        print("(1) Graphic Cards")
        time.sleep(0.2)
        print("(2) Motherboards")
        time.sleep(0.2)
        print("(3) Processors")
        time.sleep(0.2)
        print("(4) RAM")
        time.sleep(0.2)
        print("(5) HDD/SSD/NVME")
        time.sleep(0.2)
        print("(6) CPU Coolers")
        time.sleep(0.2)
        print("(7) Power Supply")
        time.sleep(0.2)
        print("(8) Other Peripherals")
        time.sleep(0.2)
        print("(9) PREVIOUS PAGE <=")
        time.sleep(0.2)
        print('''NOTE: YOU WILL NEED THE (ItemID) OF ANY PRODUCT THAT YOU WANT TO EDIT.\n      THE (ItemID) CAN BE FOUND THROUGH (View Inventory) OPTION.''')
        print('-------------')
        StatementZ="Select one of the options (1/2/3/4/5/6/7/8/9): "
        for j in StatementZ:
            print(j,end='')
            time.sleep(0.03)
        choiceZ=str(input(""))
        if choiceZ=='9':
            print('-------------')
            break
        elif choiceZ=='1':
            print('-------------')
            itemid=str(input("Enter the (ItemID) of the Product: "))
            if itemid=='':
                print('-------------')
                print("Invalid ItemID!")
                continue
            else:
                pass
            print('-------------')
            mycursor.execute("Select*from gpu where ItemId=(%s)",(itemid,))
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','VRAM','Type','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print(y)
            while True:
                print('-------------')
                sen=("What you want to Modify?")
                for i in sen:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print("(1) ItemID")
                time.sleep(0.2)
                print("(2) Brand")
                time.sleep(0.2)
                print("(3) Product Name")
                time.sleep(0.2)
                print("(4) VRAM Amount")
                time.sleep(0.2)
                print("(5) Type")
                time.sleep(0.2)
                print("(6) Quantity")
                time.sleep(0.2)
                print("(7) Price(Per Unit)")
                time.sleep(0.2)
                print("(8) PREVIOUS PAGE <=")
                time.sleep(0.2)
                print('-------------')
                StatementA="Select one of the options (1/2/3/4/5/6/7/8): "
                for b in StatementA:
                    print(b,end='')
                    time.sleep(0.03)
                choiceA=str(input(""))

                if choiceA=='1':
                    newitemid=str(input("Enter New ItemID: "))
                    if newitemid=='':
                        print('-------------')
                        print("Invalid ItemID!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update gpu set ItemID=(%s) where ItemID=(%s)",(newitemid,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue
                elif choiceA=='2':
                    brand=str(input("Enter New Brand Name: "))
                    if brand=='':
                        print('-------------')
                        print("Invalid Brand!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update gpu set Brand=(%s) where ItemID=(%s)",(brand,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='3':
                    productname=str(input("Enter New Product Name: "))
                    if productname=='':
                        print('-------------')
                        print("Invalid Product Name!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update gpu set ProductName=(%s) where ItemID=(%s)",(productname,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='4':
                    vram=str(input("Enter New VRAM Amount: "))
                    if vram=='':
                        print('-------------')
                        print("Invalid VRAM Amount!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update gpu set VRAM=(%s) where ItemID=(%s)",(vram,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='5':
                    Type=str(input("Enter the Updated Type: "))
                    if Type=='':
                        print('-------------')
                        print("Invalid Type of Product!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update gpu set Type=(%s) where ItemID=(%s)",(Type,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='6':
                    qnt=str(input("Enter the Updated Quantity: "))
                    if qnt=='':
                        print('-------------')
                        print("Invalid Quantity!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update gpu set Qnt=(%s) where ItemID=(%s)",(qnt,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='7':
                    ppu=str(input("Enter the Updated Price(Per Unit): "))
                    if ppu=='':
                        print('-------------')
                        print("Invalid Price!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update gpu set Price_Per_Unit=(%s) where ItemID=(%s)",(ppu,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='8':
                    break

                else:
                    print('-------------')
                    print("SELECT A VALID OPTION!")
                    continue

        elif choiceZ=='2':
            print('-------------')
            itemid=str(input("Enter the (ItemID) of the Product: "))
            if itemid=='':
                print('-------------')
                print("Invalid ItemID!")
                continue
            else:
                pass
            print('-------------')
            mycursor.execute("Select*from motherboard where ItemId=(%s)",(itemid,))
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Socket','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print(y)
            while True:
                print('-------------')
                sen=("What you want to Modify?")
                for i in sen:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print("(1) ItemID")
                time.sleep(0.2)
                print("(2) Brand")
                time.sleep(0.2)
                print("(3) Product Name")
                time.sleep(0.2)
                print("(4) Type")
                time.sleep(0.2)
                print("(5) Socket")
                time.sleep(0.2)
                print("(6) Quantity")
                time.sleep(0.2)
                print("(7) Price(Per Unit)")
                time.sleep(0.2)
                print("(8) PREVIOUS PAGE <=")
                time.sleep(0.2)
                print('-------------')
                StatementA="Select one of the options (1/2/3/4/5/6/7/8): "
                for b in StatementA:
                    print(b,end='')
                    time.sleep(0.03)
                choiceA=str(input(""))

                if choiceA=='1':
                    newitemid=str(input("Enter New ItemID: "))
                    if newitemid=='':
                        print('-------------')
                        print("Invalid ItemID!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update motherboard set ItemID=(%s) where ItemID=(%s)",(newitemid,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue
                elif choiceA=='2':
                    brand=str(input("Enter New Brand Name: "))
                    if brand=='':
                        print('-------------')
                        print("Invalid Brand!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update motherboard set Brand=(%s) where ItemID=(%s)",(brand,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='3':
                    productname=str(input("Enter New Product Name: "))
                    if productname=='':
                        print('-------------')
                        print("Invalid Product Name!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update motherboard set ProductName=(%s) where ItemID=(%s)",(productname,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='5':
                    socket=str(input("Enter Updated Socket Type: "))
                    if socket=='':
                        print('-------------')
                        print("Invalid Socket Type!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update motherboard set Socket=(%s) where ItemID=(%s)",(socket,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='4':
                    Type=str(input("Enter the Updated Type: "))
                    if Type=='':
                        print('-------------')
                        print("Invalid Type of Product!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update motherboard set Type=(%s) where ItemID=(%s)",(Type,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='6':
                    qnt=str(input("Enter the Updated Quantity: "))
                    if qnt=='':
                        print('-------------')
                        print("Invalid Quantity!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update motherboard set Qnt=(%s) where ItemID=(%s)",(qnt,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='7':
                    ppu=str(input("Enter the Updated Price(Per Unit): "))
                    if ppu=='':
                        print('-------------')
                        print("Invalid Price!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update motherboard set Price_Per_Unit=(%s) where ItemID=(%s)",(ppu,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='8':
                    break

                else:
                    print('-------------')
                    print("SELECT A VALID OPTION!")
                    continue

        elif choiceZ=='3':
            print('-------------')
            itemid=str(input("Enter the (ItemID) of the Product: "))
            if itemid=='':
                print('-------------')
                print("Invalid ItemID!")
                continue
            else:
                pass
            print('-------------')
            mycursor.execute("Select*from cpu where ItemId=(%s)",(itemid,))
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
            print(y)
            while True:
                print('-------------')
                sen=("What you want to Modify?")
                for i in sen:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print("(1) ItemID")
                time.sleep(0.2)
                print("(2) Brand")
                time.sleep(0.2)
                print("(3) Product Name")
                time.sleep(0.2)
                print("(4) Type")
                time.sleep(0.2)
                print("(5) Quantity")
                time.sleep(0.2)
                print("(6) Price(Per Unit)")
                time.sleep(0.2)
                print("(7) PREVIOUS PAGE <=")
                time.sleep(0.2)
                print('-------------')
                StatementA="Select one of the options (1/2/3/4/5/6/7): "
                for b in StatementA:
                    print(b,end='')
                    time.sleep(0.03)
                choiceA=str(input(""))

                if choiceA=='1':
                    newitemid=str(input("Enter New ItemID: "))
                    if newitemid=='':
                        print('-------------')
                        print("Invalid ItemID!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cpu set ItemID=(%s) where ItemID=(%s)",(newitemid,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue
                elif choiceA=='2':
                    brand=str(input("Enter New Brand Name: "))
                    if brand=='':
                        print('-------------')
                        print("Invalid Brand!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cpu set Brand=(%s) where ItemID=(%s)",(brand,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='3':
                    productname=str(input("Enter New Product Name: "))
                    if productname=='':
                        print('-------------')
                        print("Invalid Product Name!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cpu set ProductName=(%s) where ItemID=(%s)",(productname,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='4':
                    Type=str(input("Enter the Updated Type: "))
                    if Type=='':
                        print('-------------')
                        print("Invalid Type of Product!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cpu set Type=(%s) where ItemID=(%s)",(Type,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='5':
                    qnt=str(input("Enter the Updated Quantity: "))
                    if qnt=='':
                        print('-------------')
                        print("Invalid Quantity!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cpu set Qnt=(%s) where ItemID=(%s)",(qnt,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='6':
                    ppu=str(input("Enter the Updated Price(Per Unit): "))
                    if ppu=='':
                        print('-------------')
                        print("Invalid Price!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cpu set Price_Per_Unit=(%s) where ItemID=(%s)",(ppu,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='7':
                    break

                else:
                    print('-------------')
                    print("SELECT A VALID OPTION!")
                    continue

        elif choiceZ=='4':
            print('-------------')
            itemid=str(input("Enter the (ItemID) of the Product: "))
            if itemid=='':
                print('-------------')
                print("Invalid ItemID!")
                continue
            else:
                pass
            print('-------------')
            mycursor.execute("Select*from ram where ItemId=(%s)",(itemid,))
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Memory','Clocked','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
            print(y)
            while True:
                print('-------------')
                sen=("What you want to Modify?")
                for i in sen:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print("(1) ItemID")
                time.sleep(0.2)
                print("(2) Brand")
                time.sleep(0.2)
                print("(3) Product Name")
                time.sleep(0.2)
                print("(4) Type")
                time.sleep(0.2)
                print("(5) Memory")
                time.sleep(0.2)
                print("(6) Clocked")
                time.sleep(0.2)
                print("(7) Quantity")
                time.sleep(0.2)
                print("(8) Price(Per Unit)")
                time.sleep(0.2)
                print("(9) PREVIOUS PAGE <=")
                time.sleep(0.2)
                print('-------------')
                StatementA="Select one of the options (1/2/3/4/5/6/7/8/9): "
                for b in StatementA:
                    print(b,end='')
                    time.sleep(0.03)
                choiceA=str(input(""))

                if choiceA=='1':
                    newitemid=str(input("Enter New ItemID: "))
                    if newitemid=='':
                        print('-------------')
                        print("Invalid ItemID!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update ram set ItemID=(%s) where ItemID=(%s)",(newitemid,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue
                elif choiceA=='2':
                    brand=str(input("Enter New Brand Name: "))
                    if brand=='':
                        print('-------------')
                        print("Invalid Brand!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update ram set Brand=(%s) where ItemID=(%s)",(brand,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='3':
                    productname=str(input("Enter New Product Name: "))
                    if productname=='':
                        print('-------------')
                        print("Invalid Product Name!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update ram set ProductName=(%s) where ItemID=(%s)",(productname,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='5':
                    memory=str(input("Enter Updated Memory: "))
                    if memory=='':
                        print('-------------')
                        print("Invalid Memory!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update ram set Memory=(%s) where ItemID=(%s)",(memory,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='4':
                    Type=str(input("Enter the Updated Type: "))
                    if Type=='':
                        print('-------------')
                        print("Invalid Type of Product!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update ram set Type=(%s) where ItemID=(%s)",(Type,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='6':
                    clockspeed=str(input("Enter the ClockSpeed: "))
                    if clockspeed=='':
                        print('-------------')
                        print("Invalid Clockspeed!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update ram set Clocked=(%s) where ItemID=(%s)",(clockspeed,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='7':
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        print('-------------')
                        print("Invalid Quantity!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update ram set Qnt=(%s) where ItemID=(%s)",(qnt,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='8':
                    ppu=str(input("Enter the Updated Price(Per Unit): "))
                    if ppu=='':
                        print('-------------')
                        print("Invalid Price!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update ram set Price_Per_Unit=(%s) where ItemID=(%s)",(ppu,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='9':
                    break

                else:
                    print('-------------')
                    print("SELECT A VALID OPTION!")
                    continue


        elif choiceZ=='5':
            print('-------------')
            itemid=str(input("Enter the (ItemID) of the Product: "))
            if itemid=='':
                print('-------------')
                print("Invalid ItemID!")
                continue
            else:
                pass
            print('-------------')
            mycursor.execute("Select*from storagedevice where ItemId=(%s)",(itemid,))
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Capacity','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print(y)
            while True:
                print('-------------')
                sen=("What you want to Modify?")
                for i in sen:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print("(1) ItemID")
                time.sleep(0.2)
                print("(2) Brand")
                time.sleep(0.2)
                print("(3) Product Name")
                time.sleep(0.2)
                print("(4) Type")
                time.sleep(0.2)
                print("(5) Capacity")
                time.sleep(0.2)
                print("(6) Quantity")
                time.sleep(0.2)
                print("(7) Price(Per Unit)")
                time.sleep(0.2)
                print("(8) PREVIOUS PAGE <=")
                time.sleep(0.2)
                print('-------------')
                StatementA="Select one of the options (1/2/3/4/5/6/7/8): "
                for b in StatementA:
                    print(b,end='')
                    time.sleep(0.03)
                choiceA=str(input(""))

                if choiceA=='1':
                    newitemid=str(input("Enter New ItemID: "))
                    if newitemid=='':
                        print('-------------')
                        print("Invalid ItemID!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update storagedevice set ItemID=(%s) where ItemID=(%s)",(newitemid,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue
                elif choiceA=='2':
                    brand=str(input("Enter New Brand Name: "))
                    if brand=='':
                        print('-------------')
                        print("Invalid Brand!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update storagedevice set Brand=(%s) where ItemID=(%s)",(brand,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='3':
                    productname=str(input("Enter New Product Name: "))
                    if productname=='':
                        print('-------------')
                        print("Invalid Product Name!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update storagedevice set ProductName=(%s) where ItemID=(%s)",(productname,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='4':
                    Type=str(input("Enter the Updated Type: "))
                    if Type=='':
                        print('-------------')
                        print("Invalid Type of Product!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update storagedevice set Type=(%s) where ItemID=(%s)",(Type,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='5':
                    capacity=str(input("Enter the Capacity: "))
                    if capacity=='':
                        print('-------------')
                        print("Invalid Capacity!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update storagedevice set Capacity=(%s) where ItemID=(%s)",(capacity,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='6':
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        print('-------------')
                        print("Invalid Quantity!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update storagedevice set Qnt=(%s) where ItemID=(%s)",(qnt,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='7':
                    ppu=str(input("Enter the Updated Price(Per Unit): "))
                    if ppu=='':
                        print('-------------')
                        print("Invalid Price!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update storagedevice set Price_Per_Unit=(%s) where ItemID=(%s)",(ppu,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='8':
                    break

                else:
                    print('-------------')
                    print("SELECT A VALID OPTION!")
                    continue


        elif choiceZ=='6':
            print('-------------')
            itemid=str(input("Enter the (ItemID) of the Product: "))
            if itemid=='':
                print('-------------')
                print("Invalid ItemID!")
                continue
            else:
                pass
            print('-------------')
            mycursor.execute("Select*from cooler where ItemId=(%s)",(itemid,))
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Size','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print(y)
            while True:
                print('-------------')
                sen=("What you want to Modify?")
                for i in sen:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print("(1) ItemID")
                time.sleep(0.2)
                print("(2) Brand")
                time.sleep(0.2)
                print("(3) Product Name")
                time.sleep(0.2)
                print("(4) Type")
                time.sleep(0.2)
                print("(5) Size")
                time.sleep(0.2)
                print("(6) Quantity")
                time.sleep(0.2)
                print("(7) Price(Per Unit)")
                time.sleep(0.2)
                print("(8) PREVIOUS PAGE <=")
                time.sleep(0.2)
                print('-------------')
                StatementA="Select one of the options (1/2/3/4/5/6/7/8): "
                for b in StatementA:
                    print(b,end='')
                    time.sleep(0.03)
                choiceA=str(input(""))

                if choiceA=='1':
                    newitemid=str(input("Enter New ItemID: "))
                    if newitemid=='':
                        print('-------------')
                        print("Invalid ItemID!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cooler set ItemID=(%s) where ItemID=(%s)",(newitemid,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue
                elif choiceA=='2':
                    brand=str(input("Enter New Brand Name: "))
                    if brand=='':
                        print('-------------')
                        print("Invalid Brand!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cooler set Brand=(%s) where ItemID=(%s)",(brand,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='3':
                    productname=str(input("Enter New Product Name: "))
                    if productname=='':
                        print('-------------')
                        print("Invalid Product Name!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cooler set ProductName=(%s) where ItemID=(%s)",(productname,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='4':
                    Type=str(input("Enter the Updated Type: "))
                    if Type=='':
                        print('-------------')
                        print("Invalid Type of Product!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cooler set Type=(%s) where ItemID=(%s)",(Type,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='5':
                    size=str(input("Enter the Size: "))
                    if size=='':
                        print('-------------')
                        print("Invalid Size!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cooler set Size=(%s) where ItemID=(%s)",(size,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='6':
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        print('-------------')
                        print("Invalid Quantity!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cooler set Qnt=(%s) where ItemID=(%s)",(qnt,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='7':
                    ppu=str(input("Enter the Updated Price(Per Unit): "))
                    if ppu=='':
                        print('-------------')
                        print("Invalid Price!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update cooler set Price_Per_Unit=(%s) where ItemID=(%s)",(ppu,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='8':
                    break

                else:
                    print('-------------')
                    print("SELECT A VALID OPTION!")
                    continue


        elif choiceZ=='7':
            print('-------------')
            itemid=str(input("Enter the (ItemID) of the Product: "))
            if itemid=='':
                print('-------------')
                print("Invalid ItemID!")
                continue
            else:
                pass
            print('-------------')
            mycursor.execute("Select*from powersupply where ItemId=(%s)",(itemid,))
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Power','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
            print(y)
            while True:
                print('-------------')
                sen=("What you want to Modify?")
                for i in sen:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print("(1) ItemID")
                time.sleep(0.2)
                print("(2) Brand")
                time.sleep(0.2)
                print("(3) Product Name")
                time.sleep(0.2)
                print("(4) Power")
                time.sleep(0.2)
                print("(5) Quantity")
                time.sleep(0.2)
                print("(6) Price(Per Unit)")
                time.sleep(0.2)
                print("(7) PREVIOUS PAGE <=")
                time.sleep(0.2)
                print('-------------')
                StatementA="Select one of the options (1/2/3/4/5/6/7): "
                for b in StatementA:
                    print(b,end='')
                    time.sleep(0.03)
                choiceA=str(input(""))

                if choiceA=='1':
                    newitemid=str(input("Enter New ItemID: "))
                    if newitemid=='':
                        print('-------------')
                        print("Invalid ItemID!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update powersupply set ItemID=(%s) where ItemID=(%s)",(newitemid,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue
                elif choiceA=='2':
                    brand=str(input("Enter New Brand Name: "))
                    if brand=='':
                        print('-------------')
                        print("Invalid Brand!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update powersupply set Brand=(%s) where ItemID=(%s)",(brand,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='3':
                    productname=str(input("Enter New Product Name: "))
                    if productname=='':
                        print('-------------')
                        print("Invalid Product Name!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update powersupply set ProductName=(%s) where ItemID=(%s)",(productname,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='4':
                    power=str(input("Enter the Power: "))
                    if power=='':
                        print('-------------')
                        print("Invalid Power!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update powersupply set Power=(%s) where ItemID=(%s)",(power,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='5':
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        print('-------------')
                        print("Invalid Quantity!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update powersupply set Qnt=(%s) where ItemID=(%s)",(qnt,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='6':
                    ppu=str(input("Enter the Updated Price(Per Unit): "))
                    if ppu=='':
                        print('-------------')
                        print("Invalid Price!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update powersupply set Price_Per_Unit=(%s) where ItemID=(%s)",(ppu,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='7':
                    break

                else:
                    print('-------------')
                    print("SELECT A VALID OPTION!")
                    continue


        elif choiceZ=='8':
            print('-------------')
            itemid=str(input("Enter the (ItemID) of the Product: "))
            if itemid=='':
                print('-------------')
                print("Invalid ItemID!")
                continue
            else:
                pass
            print('-------------')
            mycursor.execute("Select*from otherperipherals where ItemId=(%s)",(itemid,))
            x=mycursor.fetchall()
            y=PrettyTable(['ItemID','Brand','Product Name','Type','Comments','Qnt.','Price(Per Unit)'])
            for i in x:
                y.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
            print(y)
            while True:
                print('-------------')
                sen=("What you want to Modify?")
                for i in sen:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                print("(1) ItemID")
                time.sleep(0.2)
                print("(2) Brand")
                time.sleep(0.2)
                print("(3) Product Name")
                time.sleep(0.2)
                print("(4) Type")
                time.sleep(0.2)
                print("(5) Comments")
                time.sleep(0.2)
                print("(6) Quantity")
                time.sleep(0.2)
                print("(7) Price(Per Unit)")
                time.sleep(0.2)
                print("(8) PREVIOUS PAGE <=")
                time.sleep(0.2)
                print('-------------')
                StatementA="Select one of the options (1/2/3/4/5/6/7/8): "
                for b in StatementA:
                    print(b,end='')
                    time.sleep(0.03)
                choiceA=str(input(""))

                if choiceA=='1':
                    newitemid=str(input("Enter New ItemID: "))
                    if newitemid=='':
                        print('-------------')
                        print("Invalid ItemID!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update otherperipherals set ItemID=(%s) where ItemID=(%s)",(newitemid,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue
                elif choiceA=='2':
                    brand=str(input("Enter New Brand Name: "))
                    if brand=='':
                        print('-------------')
                        print("Invalid Brand!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update otherperipherals set Brand=(%s) where ItemID=(%s)",(brand,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='3':
                    productname=str(input("Enter New Product Name: "))
                    if productname=='':
                        print('-------------')
                        print("Invalid Product Name!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update otherperipherals set ProductName=(%s) where ItemID=(%s)",(productname,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='4':
                    Type=str(input("Enter the Updated Type: "))
                    if Type=='':
                        print('-------------')
                        print("Invalid Type of Product!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update otherperipherals set Type=(%s) where ItemID=(%s)",(Type,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='5':
                    comments=str(input("Enter the Comments(if any, press (enter) if no comments): "))
                    if comments=='':
                        comments='NULL'
                        pass
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update otherperipherals set Power=(%s) where ItemID=(%s)",(comments,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='6':
                    qnt=str(input("Enter the Quantity: "))
                    if qnt=='':
                        print('-------------')
                        print("Invalid Quantity!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update otherperipherals set Qnt=(%s) where ItemID=(%s)",(qnt,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='7':
                    ppu=str(input("Enter the Updated Price(Per Unit): "))
                    if ppu=='':
                        print('-------------')
                        print("Invalid Price!")
                        continue
                    else:
                        pass
                    ch=str(input("Are you Sure to Update (Y/N): "))
                    ch=ch.upper()
                    if ch=='Y':
                        mycursor.execute("update otherperipherals set Price_Per_Unit=(%s) where ItemID=(%s)",(ppu,itemid))
                        con.commit()
                        print("RECORD UPDATED SUCCESSFULLY!")
                        break
                    elif ch=='N':
                        break
                    else:
                        print('-------------')
                        print('SELECT A VALID OPTION!')
                        continue

                elif choiceA=='8':
                    break

                else:
                    print('-------------')
                    print("SELECT A VALID OPTION!")
                    continue

        elif choiceZ=='9':
            break

        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            continue
