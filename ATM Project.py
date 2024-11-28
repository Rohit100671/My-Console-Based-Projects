'''WAP to print ATM Softwar.'''

bankpin={1001:100000,1002:200000,1003:300000,1004:400000,1005:500000,1006:6000000,1007:700000,1008:8000000,1009:9000000,1010:1000000}
while True:
    
    Cardinsert=input("Insert Your Card(yes/no): ")
    if Cardinsert=='yes':
        print("After Inserting Can't Remove Your Card...")
        print("="*125)
        print(" "*40,"Welcome To our RJT Bank ATM!")
        print("="*125)
        
        
        print("""
                ATM Desktop
                1. Withdraw
                2. Deposit
                3. Balance Inquiry
                4. Exit
        """)
        ch=int(input("Enter Your Choice: "))
        if ch==1:
            pin=int(input("After Withdraw Your Amount First Insert Your ATM Pin No.: "))
            if pin in bankpin:
                print("Your Account is Feched Successfully...")
                wa=int(input("Enter Your Withdraw Amount: "))
                if wa<bankpin[pin]:
                    print("Your Withdrawl is Successful...\n")
                    totalwid=bankpin[pin]-wa
                    bankpin[pin]=totalwid

                else:
                    print("Entered Amount Are Invalid...\n")
                
            else:
                print("Your Account Is Not Feched...\n")

        elif ch==2:
            pin=int(input("Enter Your ATM Pin: "))
            depo=int(input("Enter Deposit Amount: "))
            totaldepo=bankpin[pin]+depo
            bankpin[pin]=totaldepo
            print("Deposit is Successful...\n")

        elif ch==3:
            pin=int(input("Enter Your Pin: "))
            print(f"Your Account Balance is {bankpin[pin]}\n")
            
        elif ch==4:
            print("Exit Successful...")
            break
    else:
        print("You Are Not Insert Your Card......")
        break