import time
import datetime
from finalcode import*
print('==========================================================================')
print("WELCOME TO TECH DREAMS".center(75))
print('==========================================================================')
x=str(input("Enter Your Name: "))
print("Hello",x,end='')
time.sleep(0.8)
print("!")
time.sleep(0.8)

while True:
    print('-------------')
    print("(1) Register New User!")
    time.sleep(0.4)
    print("(2) Login(USER)!")
    time.sleep(0.4)
    print("(3) Login(ADMIN)!")
    time.sleep(0.4)
    print("(4) QUIT Tech Dreams Application!")
    time.sleep(0.2)
    print('-------------')
    x="Select one of the options (1/2/3/4): "
    for i in x:
        print(i,end='')
        time.sleep(0.03)
    ch=str(input(""))
    print('-------------')
    
    if ch=='1':
        x=("Note: You need Admin Permissions to Create a New User Account!")
        for i in x:
            print(i,end="")
            time.sleep(0.03)
        print()
        time.sleep(0.1)
        print('-------------')
        ques="Want to proceed? (Y/N): "
        for i in ques:
            print(i,end='')
            time.sleep(0.03)
        finalchoice=str(input(""))
        finalchoice=finalchoice.upper()
        
        if finalchoice=='Y':
            print('-------------')
            adminname=str(input("Admin Name: "))
            adminpassword=str(input("Admin Password: "))
            print('-------------')
            statement="Checking Entered Information"
            for j in statement:
                print(j,end="")
                time.sleep(0.03)
            time.sleep(0.4)
            a="..."
            for c in a:
                print(c,end="")
                time.sleep(0.3)
            time.sleep(0.4)
            print()
            result=searchadmin(adminname,adminpassword)
            if result==True:
                print('-------------')
                abc=("You can create New User by entering details Below!")
                for j in abc:
                    print(j,end="")
                    time.sleep(0.03)
                time.sleep(0.4)
                print()
                createuser()
                pass
            
        elif finalchoice=='N':
            continue

        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            continue
            
    elif ch=='2':
        name=input("Enter your Username: ")
        password=input("Enter your Password : ")
        n=searchuser(name,password)
        while n==True:
            print('-------------')
            statement1='''Welcome To Tech Dreams Management Software'''
            statement2='''Choose your desired operation to perform from below!'''
            for i in statement1:
                print(i,end='')
                time.sleep(0.03)
            print()
            time.sleep(0.1)
            for i in statement2:
                print(i,end='')
                time.sleep(0.03)
            print()
            time.sleep(0.1)
            print('(1) Sales Management')
            time.sleep(0.4)
            print('(2) Product Management')
            time.sleep(0.4)
            print('(3) Logout')
            time.sleep(0.2)
            print('-------------')
            Statement3="Select one of the options (1/2/3): "
            for j in Statement3:
                print(j,end='')
                time.sleep(0.03)
            choice=str(input(""))
            print('-------------')

            if choice=='3':
                print("Logging Out",end='')
                x="..."
                for i in x:
                    print(i,end='')
                    time.sleep(0.5)
                print()
                time.sleep(0.8)
                print("Logout Successful!")
                time.sleep(1)
                break
             
            elif choice=='2':
                while True:
                    Statement6="What would you like to perform?"
                    for z in Statement6:
                        print(z,end='')
                        time.sleep(0.03)
                    print()
                    print("(1) Add New Product(s)")
                    time.sleep(0.4)
                    print("(2) Modify Existing Product(s)")
                    time.sleep(0.4)
                    print("(3) View Inventory")
                    time.sleep(0.4)
                    print("(4) PREVIOUS PAGE <=")
                    time.sleep(0.2)
                    print('-------------')
                    Statement7="Select one of the options (1/2/3/4): "
                    for g in Statement7:
                        print(g,end='')
                        time.sleep(0.03)
                    choiceAB=str(input(""))
                    if choiceAB=='4':
                        break
                    elif choiceAB=='1':
                        addproducts()
                    elif choiceAB=='2':
                        modifyproducts()                    
                    elif choiceAB=='3':
                        print('-------------')
                        while True:
                            state="Choose which Order to View?"
                            for x in state:
                                print(x,end='')
                                time.sleep(0.03)
                            print()
                            print("(1) SerialWise Inventory (Categories are Serialized)")
                            time.sleep(0.2)
                            print("(2) Visual Inventory (Pie Chart Visualization)")
                            time.sleep(0.2)
                            print("(3) Sorted Inventory (Categories are sorted according to needs)")
                            time.sleep(0.2)
                            print("(4) PREVIOUS PAGE <=")
                            time.sleep(0.2)
                            print('-------------')
                            statement="Select one of the options (1/2/3/4): "
                            for g in statement:
                                print(g,end='')
                                time.sleep(0.03)
                            choiceC=str(input(""))
                            if choiceC=='4':
                                print('-------------')
                                break
                            elif choiceC=='1':
                                actualinventory()
                            elif choiceC=='2':
                                visualinventory()
                            elif choiceC=='3':
                                sortedinventory()                                    
                            else:
                                print('-------------')
                                print("SELECT A VALID OPTION!")
                                print('-------------')
                                continue
                    else:
                        print('-------------')
                        print("SELECT A VALID OPTION!")
                        print('-------------')
                        continue

            elif choice=='1':
                while True:
                    Statement4="What would you like to perform?"
                    for y in Statement4:
                        print(y,end='')
                        time.sleep(0.03)
                    print()
                    print("(1) Create a Bill")
                    time.sleep(0.4)
                    print("(2) Add a Customer")
                    time.sleep(0.4)
                    print("(3) View List of Customers")
                    time.sleep(0.4)
                    print("(4) Modify Customer Records")
                    time.sleep(0.4)
                    print("(5) Delete a Customer")
                    time.sleep(0.4)
                    print("(6) PREVIOUS PAGE <=")
                    time.sleep(0.2)
                    print('-------------')
                    Statement5="Select one of the options (1/2/3/4/5/6): "
                    for g in Statement5:
                        print(g,end='')
                        time.sleep(0.03)
                    choiceA=str(input(""))
                    if choiceA=='6':
                        break
                    elif choiceA=='1':
                        bill()
                    elif choiceA=='5':
                        print('-------------')
                        delcust()
                    elif choiceA=='2':
                        print('-------------')
                        createcust()
                    elif choiceA=='3':
                        print('-------------')
                        viewcust()
                    elif choiceA=='4':
                        print('-------------')
                        modifycust()
                    else:
                        print('-------------')
                        print("SELECT A VALID OPTION!")
                        print('-------------')
                        continue
            else:
                print("SELECT A VALID OPTION!")
                continue

    elif ch=='3':
        x=("Note: ADMINS ONLY!")
        for i in x:
            print(i,end="")
            time.sleep(0.03)
        print()
        time.sleep(0.1)
        print('-------------')
        ques="Want to proceed? (Y/N): "
        for i in ques:
            print(i,end='')
            time.sleep(0.03)
        finalchoice=str(input(""))
        finalchoice=finalchoice.upper()

        if finalchoice=='Y':
            print('-------------')
            adminname=str(input("Admin Name: "))
            adminpassword=str(input("Admin Password: "))
            print('-------------')
            statement="Checking Entered Information"
            for j in statement:
                print(j,end="")
                time.sleep(0.03)
            time.sleep(0.4)
            a="..."
            for c in a:
                print(c,end="")
                time.sleep(0.3)
            time.sleep(0.4)
            print()
            result=searchadmin(adminname,adminpassword)
            while result==True:
                print('-------------')
                abc=("WELCOME TO TECH DREAMS MANEGEMENT AND ADMINISTRATION SOFTWARE!")
                for j in abc:
                    print(j,end="")
                    time.sleep(0.03)
                time.sleep(0.4)
                print()
                statement2='Choose your desired operation to perform from below!'
                for i in statement2:
                    print(i,end='')
                    time.sleep(0.03)
                print()
                time.sleep(0.1)
                print('(1) Sales Management')
                time.sleep(0.4)
                print('(2) Product Management')
                time.sleep(0.4)
                print('(3) Administration')
                time.sleep(0.4)
                print('(4) Logout')
                time.sleep(0.2)
                print('-------------')
                Statement3="Select one of the options (1/2/3/4): "
                for j in Statement3:
                    print(j,end='')
                    time.sleep(0.03)
                choice=str(input(""))
                print('-------------')

                if choice=='4':
                    print("Logging Out",end='')
                    x="..."
                    for i in x:
                        print(i,end='')
                        time.sleep(0.5)
                    print()
                    time.sleep(0.8)
                    print("Logout Successful!")
                    time.sleep(1)
                    break
            
                elif choice=='1':
                    while True:
                        Statement1="What would you like to perform?"
                        for z in Statement1:
                            print(z,end='')
                            time.sleep(0.03)
                        print()
                        print("(1) Create a Bill")
                        time.sleep(0.4)
                        print("(2) Add a Customer")
                        time.sleep(0.4)
                        print("(3) View List of Customers")
                        time.sleep(0.4)
                        print("(4) Modify Customer Records")
                        time.sleep(0.4)
                        print("(5) Delete a Customer")
                        time.sleep(0.4)
                        print("(6) PREVIOUS PAGE <=")
                        time.sleep(0.2)
                        print('-------------')
                        Statement5="Select one of the options (1/2/3/4/5/6): "
                        for g in Statement5:
                            print(g,end='')
                            time.sleep(0.03)
                        choiceA=str(input(""))
                        if choiceA=='6':
                            break
                        elif choiceA=='1':
                            print('-------------')
                            bill()
                        elif choiceA=='5':
                            print('-------------')
                            delcust()
                        elif choiceA=='2':
                            print('-------------')
                            createcust()
                        elif choiceA=='3':
                            print('-------------')
                            viewcust()
                        elif choiceA=='4':
                            print('-------------')
                            modifycust()
                        else:
                            print('-------------')
                            print("SELECT A VALID OPTION!")
                            print('-------------')
                            continue
                elif choice=='3':
                    while True:
                        statement2='Choose your desired operation to perform from below!'
                        for i in statement2:
                            print(i,end='')
                            time.sleep(0.03)
                        print()
                        time.sleep(0.1)
                        print('(1) Register a New User')
                        time.sleep(0.4)
                        print('(2) Edit info of Existing User')
                        time.sleep(0.4)
                        print('(3) Delete an Existing User)')
                        time.sleep(0.4)
                        print('(4) View Existing User(s)')
                        time.sleep(0.4)
                        print('(5) View Login History')
                        time.sleep(0.4)
                        print('(6) Change Admin Password')
                        time.sleep(0.4)
                        print('(7) PREVIOUS PAGE <=')
                        time.sleep(0.2)
                        print('-------------')
                        Statement="Select one of the options (1/2/3/4/5/6/7): "
                        for g in Statement:
                            print(g,end='')
                            time.sleep(0.03)
                        choiceADMIN=str(input(""))
                        if choiceADMIN=='1':
                            print('-------------')
                            createuser()
                            print('-------------')
                            pass
                        elif choiceADMIN=='2':
                            edituser()
                            pass
                        elif choiceADMIN=='3':
                            print('-------------')
                            deluser()
                            print('-------------')
                            pass   
                        elif choiceADMIN=='4':
                            print('-------------')
                            viewuser()
                            print('-------------')
                            pass
                        elif choiceADMIN=='5':
                            print('-------------')
                            login()
                            print('-------------')
                            pass
                        elif choiceADMIN=='6':
                            print('-------------')
                            changeadminpass()
                            print('-------------')
                            pass
                        elif choiceADMIN=='7':
                            break
                        else:
                            print('-------------')
                            print("SELECT A VALID OPTION!")
                            print('-------------')

                elif choice=='2':
                    while True:
                        Statement4="What would you like to perform?"
                        for z in Statement4:
                            print(z,end='')
                            time.sleep(0.03)
                        print()
                        print("(1) Add New Product(s)")
                        time.sleep(0.4)
                        print("(2) Modify Existing Product(s)")
                        time.sleep(0.4)
                        print("(3) View Inventory")
                        time.sleep(0.4)
                        print("(4) PREVIOUS PAGE <=")
                        time.sleep(0.2)
                        print('-------------')
                        Statement4="Select one of the options (1/2/3/4): "
                        for g in Statement4:
                            print(g,end='')
                            time.sleep(0.03)
                        choiceA=str(input(""))
                        if choiceA=='4':
                            break
                        elif choiceA=='1':
                            addproducts()
                        elif choiceA=='2':
                            modifyproducts()                
                        elif choiceA=='3':
                            print('-------------')
                            while True:
                                state="Choose which Order to View?"
                                for x in state:
                                    print(x,end='')
                                    time.sleep(0.03)
                                print()
                                print("(1) SerialWise Inventory (Categories are Serialized)")
                                time.sleep(0.2)
                                print("(2) Visual Inventory (Pie Chart Visualization)")
                                time.sleep(0.2)
                                print("(3) Sorted Inventory (Categories are sorted according to needs)")
                                time.sleep(0.2)
                                print("(4) PREVIOUS PAGE <=")
                                time.sleep(0.2)
                                print('-------------')
                                statement="Select one of the options (1/2/3/4): "
                                for g in statement:
                                    print(g,end='')
                                    time.sleep(0.03)
                                choiceC=str(input(""))
                                if choiceC=='4':
                                    print('-------------')
                                    break
                                elif choiceC=='1':
                                    actualinventory()
                                elif choiceC=='2':
                                    visualinventory()
                                elif choiceC=='3':
                                    sortedinventory()                                    
                                else:
                                    print('-------------')
                                    print("SELECT A VALID OPTION!")
                                    print('-------------')
                                    continue
                        else:
                            print('-------------')
                            print("SELECT A VALID OPTION!")
                            print('-------------')
                            continue
                else:
                    print("SELECT A VALID OPTION!")
                    continue

        elif finalchoice=='N':
            continue

        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            continue

        continue

    elif ch=='4':
        x=str(input("Are you Sure? (Y/N): "))
        x=x.upper()
        if x=='Y':
            thanks="Exiting Application"
            z='...'
            for i in thanks:
                print(i,end='')
                time.sleep(0.03)
            for j in z:
                print(j,end='')
                time.sleep(0.5)
            print()
            print("DONE!")
            break
        elif x=='N':
            pass
        else:
            print('-------------')
            print("SELECT A VALID OPTION!")
            pass
    else:
        print("SELECT A VALID OPTION!")
        continue

