available_items = ["computer", "laptop","keyboard","mouse", "modem"]
store = {"computer":7, "laptop":8,"keyboard":6,"mouse":5, "modem":5}
user = input("What is your name ? : ")
print("Welcome {} Here is a menu for you".format(user))
print()
print("AVAILABLE ITEMS ARE:\n\ncomponents\t\t\tcost\t\t\tquantity\n\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
print()
item_ordered = input("Enter the item you want to buy {} : ".format(user))
found_at = None
computer = 18000
laptop = 15000
keyboard = 1000
mouse = 500
modem = 900
Total = computer*7+laptop*8+keyboard*6+mouse*5+modem*5

for index in range(len(available_items)):
    if available_items[index]==item_ordered:
        found_at = index
if found_at is not None:
    if found_at == 0:
        a = int(input("How many {} {}?".format(item_ordered,user)))
        if a > 7:
            print("quantity exceed!! Please recheck our menu and reorder accordingly\n")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity : "))
            if a<=7:
                Tot = computer * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = computer * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
    elif found_at == 1:
        a = int(input("How many {} {}?".format(item_ordered,user)))
        if a > 8:
            print("quantity exceed!! Please recheck our menu and reorder accordingly")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity"))
            if a<=8:
                Tot = laptop * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a ,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = laptop * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
    elif found_at == 2:
        a = int(input("How many {} {}?".format(item_ordered,user)))
        if a>6:
            print("quantity exceed!! Please recheck our menu and reorder accordingly")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity"))
            if a<=6:
                Tot = keyboard * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = keyboard * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
    elif found_at == 3:
        a = int(input("how many {} {}?".format(item_ordered,user)))
        if a>5:
            print("quantity exceed!!please recheck  our menu and reorder accordingly")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity"))
            if a<=5:
                Tot = mouse * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = mouse * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
    elif found_at == 4:
        a = int(input("How many {} {}?".format(item_ordered,user)))
        if a > 5:
            print("quantity exceed!! Please recheck our menu and reorder accordingly")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity"))
            if a <= 5:
                Tot = modem * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = modem * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))

else:
    print("Sorry {} is not available in our shop {}".format(item_ordered,user))
    print("would you like to order anything else yes or no")
    y = "yes"
    n = "no"
    choice = input("Enter : ")
    if choice == y:
        item_ordered = input("Enter the item you want to buy {} : ".format(user))
        for index in range(len(available_items)):
            if available_items[index]==item_ordered:
                found_at = index
if found_at is not None:
    if found_at == 0:
        a = int(input("how many {} {}?".format(item_ordered,user)))
        if a > 7:
            print("quantity exceed!! Please recheck our menu and reorder accordingly\n")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity : "))
            if a<=7:
                Tot = computer * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = computer * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
    elif found_at == 1:
        a = int(input("How many {} {}?".format(item_ordered,user)))
        if a > 8:
            print("quantity exceed!! Please recheck our menu and reorder accordingly")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity"))
            if a<=8:
                Tot = laptop * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a ,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = laptop * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
    elif found_at == 2:
        a = int(input("How many {} {}?".format(item_ordered,user)))
        if a>6:
            print("quantity exceed!! Please recheck our menu and reorder accordingly")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity"))
            if a<=6:
                Tot = keyboard * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = keyboard * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
    elif found_at == 3:
        a = int(input("how many {} {}?".format(item_ordered,user)))
        if a>5:
            print("quantity exceed!!please recheck  our menu and reorder accordingly")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity"))
            if a<=5:
                Tot = mouse * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = mouse * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
    elif found_at == 4:
        a = int(input("How many {} {}?".format(item_ordered,user)))
        if a > 5:
            print("quantity exceed!! Please recheck our menu and reorder accordingly")
            print("AVAILABLE ITEMS ARE:\ncomponents\t\t\tcost\t\t\tquantity\n1.computer\t\t\t$18000\t\t\t7\n2.laptop\t\t\t$15000\t\t\t8\n3.keyboard\t\t\t$1000\t\t\t6\n4.mouse\t\t\t\t$500\t\t\t5\n5.modem\t\t\t\t$900\t\t\t5")
            a = int(input("renter the quantity"))
            if a <= 5:
                Tot = modem * a
                Total = Total - Tot
                print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))
            else:
                print("Sorry you entered wrong try again later")
        else:
            Tot = modem * a
            Total = Total - Tot
            print("you ordered {} {} and your total cost is {}\nThank you {}:)".format(a,item_ordered,Tot,user))

print("-" * 80)
if item_ordered in store:
    store[item_ordered]-=a
    print("inventory left after shopping is ",store)





