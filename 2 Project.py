# WAP to print students management system.

student={1:{"name":"rohit","city":"pune","passing_year":2024,"percentage":72,"cource":"python"}}
print("-"*100)
print(" "*35,"The Kiran Academy")
print("-"*100)
while True:
    print("""

        Dash-Board
        1. Added Data
        2. Display Data
        3. Update Data
        4. Delete Data
        5. Filter
    """)

    ch=int(input("Enter Your Choice: "))
    if ch==1:
        rno=int(input("Enter Your Registration Number: "))
        name=input("Enter Your Name: ")
        city=input("Enter Your City: ")
        year=int(input("Enter Your Passing Year: "))
        percentage=int(input("Enter Your Percentage: "))
        cource=input("Enter Your Cource: ")
        student[rno]={"name":name,"city":city,"passing_year":year,"percentage":percentage,"cource":cource}
        print(student)

    elif ch==2:
        print("="*106)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Name","City","Passing_year","Percentage","Cource"))
        print("="*106)

        for i in student:
             print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(student[i]["name"],student[i]["city"],student[i]["passing_year"],student[i]["percentage"],student[i]["cource"]))
             print("-"*106)

    elif ch==3:
        rno=int(input("Enter Your Rno: "))
        if rno in student:
            print("""
                        Update Values
                1. name
                2. city
                3. passing_year
                4. percentage
                5. cource
                """)
            ch=int(input("Enter Your Choice: "))
            if ch==1:
                uname=input("Enter Your Update Nmae: ")
                student[rno]["name"]=uname
                print("Update Name Successfully...")

            elif ch==2:
                ucity=input("Enter Your Update city: ")
                student[rno]["city"]=ucity
                print("Update City Successfully...")

            elif ch==3:
                uyear=input("Enter Your Update passing year: ")
                student[rno]["passing_year"]=uyear
                print("Update Passing Year Successfully...")

            elif ch==4:
                upercentage=input("Enter Your Update percentage: ")
                student[rno]["percentage"]=upercentage
                print("Update Peacentage Successfully...")

            elif ch==5:
                ucource=input("Enter Your Update Cource: ")
                student[rno]["cource"]=ucource
                print("Update Cource Successfully...")
        else:
            print("Invalid Registrration Number.")
            
    elif ch==4:
        rno=int(input("Enter Your Rno: "))
        if rno in student:
            del student[rno]
            print("Delete Successfully")
        else:
            print("Invalid Registration Number.")

    elif ch==5:
        print("""
               1.name    
               2.city
               3.percentage
               4.course
               5.passing year
             """)
        ch=int(input('choose filter: '))
        if ch==1:
           na=input('enter name:')
           print('-'*97)
           print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('name','city','percentage','course','passing_year'))
           print('-'*97)
           for rno in student:
                if na==student[rno]['name']:
                    print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,student[rno]['name'],student[rno]['city'],student[rno]['percentage'],student[rno]['cource'],student[rno]['passing_year']))
                    print('-'*97)
           print('filter successfully:')

        elif ch==2:
            city=input('enter city:')
            print('-'*97)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
            print('-'*97)
            for rno in student:
                if city==student[rno]['city']:
                    print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,student[rno]['name'],student[rno]['city'],student[rno]['percentage'],student[rno]['cource'],student[rno]['passing_year']))
                    print('-'*97)
            print('filter successfully:')
            
        elif ch==3:
           percentage=eval(input('enter percentage:'))
           print('-'*97)
           print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
           print('-'*97)
           for rno in student:
                if percentage==student[rno]['percentage']:
                    print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,student[rno]['name'],student[rno]['city'],student[rno]['percentage'],student[rno]['cource'],student[rno]['passing_year']))
                    print('-'*97)
           print('filter successfully:')  

        elif ch==4:
            cou=input('enter cource:')
            print('-'*97)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
            print('-'*97)
            for rno in student:
                if cou==student[rno]['cource']:
                    print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,student[rno]['name'],student[rno]['city'],student[rno]['percentage'],student[rno]['cource'],student[rno]['passing_year']))
                    print('-'*97)
            print('filter successfully:')  

        elif ch==5:
            pe=int(input('enter passing year:'))
            print('-'*97)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
            print('-'*97)
            for rno in student:
                if pe==student[rno]['passing_year']:
                    print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,student[rno]['name'],student[rno]['city'],student[rno]['percentage'],student[rno]['cource'],student[rno]['passing_year']))
                    print('-'*97)
            print('filter successfully:') 

        else:
         print('invalid filter')
         
    else:
        print("Invalide Input...")
        break