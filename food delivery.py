def login(name,pswd):
    print("username: ",name)
    print("password: ",pswd)
    print()
    return
user = input("Enter your usernmae : ")
password = input("enter password : ")
login(user, password)
available_items = ["idle", "dosa","pallav","biryani", "fish fry"]
print("Welcome {} to our restorant Here is a menu for you".format(user))
print()
print("MENUE:\n1.idle\t\t\t\t$40\n2.dosa\t\t\t\t$30\n3.pallav\t\t\t$45\n4.biryani\t\t\t$60\n5.fish fry\t\t\t$50")
print()
idle = 40
dosa = 30
pallav = 45
biryani = 60
fishfry = 50
found_at = None
item_ordered = input("Enter the item you want to buy {} : ".format(user))
for index in range(len(available_items)):
    if available_items[index]==item_ordered:
        found_at = index
if found_at is not None:
    if found_at == 0:
        a = int(input("How many?"))
        Tot = idle * a
        print("you ordered {} {} and total cost is {}\nThank you".format(a,item_ordered,Tot))
    elif found_at == 1:
        a = int(input("How many?"))
        Tot = dosa * a
        print("you ordered {} {} and total cost is {}\nThank you".format(a,item_ordered,Tot))
    elif found_at == 2:
        a = int(input("How many?"))
        Tot = pallav * a
        print("you ordered {} {} and total cost is {}\nThank you".format(a,item_ordered,Tot))
    elif found_at == 3:
        a = int(input("How many?"))
        Tot = biryani * a
        print("you ordered {} {} and total cost is {}\nThank you".format(a,item_ordered,Tot))
    elif found_at == 4:
        a = int(input("How many?"))
        Tot = fishfry * a
        print("you ordered {} {} and total cost is {}\nThank you".format(a,item_ordered,Tot))
else:
    print("Sorry {} not avilable in our restaurent".format(item_ordered))



