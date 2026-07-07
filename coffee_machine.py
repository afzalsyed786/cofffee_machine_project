# Resoures in the coffee machine
resoures={"milk":1500,
          "water":1500,
          "coffee_beans":500,
          "cups":15
         }

# Coins in the coffee machine
coins={
       "10":10,
       "5" :10,
       "2" :10,
       "1" :10
      }
# Espresso
Espresso={"milk":0,
          "water":50,
          "coffe_beans":18
         }
#Latte
Latte={"milk":150,
       "water":150,
       "coffe_beans":24
      }
#Cappuccino
Cappuccino={"milk":100,
            "water":100,
            "coffe_beans":24
            }
# Function to check resources for making coffee
def coffee_making_checker(resources,choice,n,Espresso,Latte,Cappuccino):
    # Avl 
    milk_avl=resources["milk"]
    water_avl=resources["water"]
    coffee_beans_avl=resources["coffee_beans"]
    cups_avl=resources["cups"]

    #Req
    req={}
    if(choice==1):
        req["milk"]=Espresso["milk"]*n
        req["water"]=Espresso["water"]*n
        req["coffee_beans"]=Espresso["coffe_beans"]*n
    elif(choice==2):
        req["milk"]=Latte["milk"]*n
        req["water"]=Latte["water"]*n
        req["coffee_beans"]=Latte["coffe_beans"]*n
    elif(choice==3):
        req["milk"]=Cappuccino["milk"]*n
        req["water"]=Cappuccino["water"]*n
        req["coffee_beans"]=Cappuccino["coffe_beans"]*n
    else:
        print("choose correct option😒\n")
     
    # Checking Requirements
    if(milk_avl-req["milk"]>=0):
        pass
    else:
        print("Insufficient Milk😔\n")
        return 0
    if(water_avl-req["water"]>=0):
        pass
    else:
        print("Insufficient Water😔\n")
        return 0
    if(coffee_beans_avl-req["coffee_beans"]>=0):
        pass
    else:
        print("Insufficient Coffee beans😔\n")
        return 
    return 1,req

# Checking Money
def coffee_cost_cal(ch,n,mg):
    if(ch==1):
        req_money=25*n
    elif(ch==2):
        req_money=35*n
    elif(ch==3):
        req_money=30*n
    else:
        print("choose correct option😒\n")
    if(mg-req_money>=0):
        return mg-req_money
    else:
        print("No sufficient money is given😒\n")
        return -1

# Function to upadate resources
def Update_resources(resources):
    # To update milk
    mop=int(input("Press 1 to update milk😊 "))
    if(mop==1):
        milk_to_added=int(input("Enter milk in ml to add in coffee machine 🥛 "))
        resources["milk"]=resources["milk"]+milk_to_added
        print()
    else:
        print("U have pressed wrong option no milk is added😔\n")

    # To update water
    wop=int(input("Press 1 to update water😊 "))
    if(wop==1):
        water_to_added=int(input("Enter water in ml to add in coffee machine 💧 "))
        resources["water"]=resources["water"]+water_to_added
        print()
    else:
        print("U have pressed wrong option no water is added😔\n") 
    
    # To upadate Coffee beans
    cbop=int(input("Press 1 to update coffee beans😊 "))
    if(cbop==1):
        coffee_beans_to_added=int(input("Enter coffee beans in gm to add in coffee machine 🫘 "))
        resources["coffee_beans"]=resources["coffee_beans"]+coffee_beans_to_added
        print()
    else:
        print("U have pressed wrong option no coffee beans is added😔\n")  

    # To update coffe cups
    cop=int(input("Press 1 to update coffe cups😊 "))
    if(cop==1):
        coffee_cups_to_added=int(input("Enter coffee cups to add in coffee machine 🥤 "))
        resources["cups"]=resources["cups"]+coffee_cups_to_added
        print()
    else:
        print("U have pressed wrong option no coffee cups is added😔\n")

# Function to upadate coins
def Update_coins(coins):
    # To update 10 rupees coins
    op10=int(input("Press 1 to update 10 rupees coins🪙 "))
    if(op10==1):
        r10=int(input("Enter no of 10 rupees coins to add 😊 "))
        coins["10"]=coins["10"]+r10
        print()
    else:
        print("U have pressed wrong option no 10 rupees coins are added😔\n")
    
    # To update 5 rupees coins
    op5=int(input("Press 1 to update 5 rupees coins🪙 "))
    if(op5==1):
        r5=int(input("Enter no of 5 rupees coins to add 😊 "))
        coins["5"]=coins["5"]+r5
        print()
    else:
        print("U have pressed wrong option no 5 rupees coins are added😔\n")

    # To update 2 rupees coins
    op2=int(input("Press 1 to update 2 rupees coins🪙 "))
    if(op2==1):
        r2=int(input("Enter no of 2 rupees coins to add 😊 "))
        coins["2"]=coins["2"]+r2
        print()
    else:
        print("U have pressed wrong option no 2 rupees coins are added😔\n")

    # To update 1 rupees coins
    op1=int(input("Press 1 to update 1 rupees coins🪙 "))
    if(op1==1):
        r10=int(input("Enter no of 1 rupees coins to add 😊 "))
        coins["1"]=coins["1"]+r1
        print()
    else:
        print("U have pressed wrong option no 1 rupees coins are added😔\n")

# Function to check resources
def Resource_checker(resources):
    k=1
    while(k==1):
        print("1. Check Resources😊")
        print("2. Update Resources😊")
        print("3. Exit😔")
        op=int(input("Selected Required Option😊 "))
        print()
        if(op==1):
            print(f"milk(ml)         :   {resources["milk"]}🥛")
            print(f"water(ml)        :   {resources["water"]}💧")
            print(f"coffee_beans(gm) :   {resources["coffee_beans"]}🫘")
            print(f"cups             :   {resources["cups"]}🥤")
            print()
        elif(op==2):
            password=input("To update resources u have to enter password😊 ")
            if(password=='msdhoni7'):
                Update_resources(resources)
            else:
                print("U have entered wrong password try again😒\n")
        elif(op==3):
            k=0
        else:
            print("Enter correct option😒\n")

# Function to check coins
def Money_checker(coins):
    k=1
    while(k==1):
        print("1. Check coins😊")
        print("2. Update coins😊")
        print("3. Exit😔")
        op=int(input("Selected Required Option😁 "))
        print()
        if(op==1):
            print(f"10 Rupees coins        :   {coins["10"]}🪙")
            print(f"5  Rupees coins        :   {coins["5"]}🪙")
            print(f"2  Rupees coins        :   {coins["2"]}🪙")
            print(f"1  Rupees coins        :   {coins["1"]}🪙")
            print()
        elif(op==2):
             password=input("To update coins u have to enter password😊 ")
             if(password=='msdhoni7'):
                 Update_coins(coins)
             else:
                print("U have entered wrong password try again😒\n")
        elif(op==3):
            k=0
        else:
            print("Enter correct option😒\n")
        
# Main coffee machine code
machine_state=True
while(machine_state):  
    print("🎈WELCOME TO COFFEE MAKER🎈")
    print("1. Coffees☕")
    print("2. Resource🥛")
    print("3. Money🪙")
    print("4. Turn Off the coffee Machine😔")
    option=int(input("Select Required Option😊 "))
    print()
    if(option==1):
        print("1. Espresso - 25🪙")
        print("2. Latte - 35🪙")
        print("3. Cappuccino - 30🪙")
        ch=int(input("Please Select Your Choice😊 "))
        n=int(input("Do u want 1 or 2 coffees😁 "))
        print()
        can_make_coffee,req=coffee_making_checker(resoures,ch,n,Espresso,Latte,Cappuccino)
        bal=0
        if(can_make_coffee):
            money_given=int(input("please Give money for coffee😊 "))
            bal=coffee_cost_cal(ch,n,money_given)
        if(bal+1):
            rbal=bal
            resoures["milk"]=resoures["milk"]-req["milk"]
            resoures["water"]=resoures["water"]-req["water"]
            resoures["coffee_beans"]=resoures["coffee_beans"]-req["coffee_beans"]
            resoures["cups"]=resoures["cups"]-n
            c10=bal//10
            coins["10"]=coins["10"]-c10
            bal=bal%10
            c5=bal//5
            coins["5"]=coins["5"]-c5
            bal=bal%5
            c2=bal//2
            coins["2"]=coins["2"]-c2
            bal=bal%2
            c1=bal//1
            coins["1"]=coins["1"]-c1
            if(ch==1):
                print("Here is Your Espresso🥤")
            elif(ch==2):
                print("Here is Your Latte🥤")
            elif(ch==3):
                print("Here is Your Cappuccino🥤")
            if(rbal==0):
                print("You have given correct money😊\n")
            else:
                print(f"Here is your balance money {rbal}🪙\n")
    elif(option==2):
        Resource_checker(resoures)
    elif(option==3):
        Money_checker(coins)
    elif(option==4):
        machine_state=False
    else:
        print("Enter correct option😒\n")
    print("====================================================================================================================================================================================================================================================")


