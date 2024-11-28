 # PROJECT--1  WAP to print Hotel menus.

item={1:"Tea",2:"Poha",3:"Misal",4:"Dosa",5:"Vada-Pav",6:"Samosa",7:"Dhokla",8:"Gulabjamun",9:"Pakode"}
price={1:10,2:20,3:99,4:55,5:15,6:30,7:35,8:25,9:25}
print("-"*100)
print(" "*40,"Welcome To our RJT Hotel")
print("-"*100)
print("""
- RJT Hotel Menu -
1. Tea
2. Poha
3. Misal
4. Dosa
5. Vada-Pav
6. Samosa
7. Dhokla
8. Gulabjamun
9. Pakode
    """)
it=[]
qu=[]
while True:

    choice=int(input("Enter your Choice: "))
    quantity=int(input("Enter your Quantity: "))
    print(f"Your Order is {item[choice]} in {quantity} Quantity is Added on list.")
    it.append(choice)
    qu.append(quantity)
    print(it)
    print(qu)
    ch=input("You Want To Continue(y/n): ")
    if ch=='n':
        print(" "*40,"RJT Hotel")
        print("-"*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("items","Quantity","Price","Amount"))
        print("-"*85)

        sum=0
        for i in range(len(it)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(item[it[i]],qu[i],price[it[i]],qu[i]*price[it[i]]))
            print("-"*85)
            sum=sum+qu[i]*price[it[i]]
        print(f"Your Bill is {sum}\n Thank You Sir! Visite Net Time!!!")
        break