print("Hello Welcome to our cafe")
name = input("What is your name? \n").lower()
if name == "betselot" or name == "ben" or name == "loki":
    status = input(name +" Admite you are stupide \n").lower()
    counter = int(input("how many time did you thank your Cool big brother ? \n"))
    if (status == "yes" or status == "ok") and counter > 4:
        print("that is good " + name + "so let continue ...")
    elif status == "i do not think so" and counter<=3:
        print(name + " thing hard about it ")
        exit()
    else:
        print("You are not welcome")
        exit()
else:
    print()
menu = "Tea\nCoffee\nKeshr\nLatte\n"
price = 0
order = input("welcome to the cafe " + name + " , what can i get you from our menu\n " + menu).lower()
if order == "tea": 
    price = 10
elif order == "keshr":
    price = 12
elif order == "coffee":
    price = 20
elif order =="latte":
        price = 15   
else:
    print("There is nothing like that in our cafe")
    exit()
much = int(input("How many do you want \n"))
total = price * much
print("so the total price is ===> " + str(total))
print("Thank you, " + name + " for ordering, Your order of " + str(much) +" " + order + " it will be ready soon pleas have set")


