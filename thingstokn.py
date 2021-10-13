first_name = input("What is your first name?")
second_name = input("What is your second name?")
if first_name.isalpha() and second_name.isalpha() == True:
    print("{} {} Welcome".format(first_name, second_name))
    print("Do you wish to continue with us yes or No?")
    y = "yes"
    N = "No"
    user = input()
    if user == y:
        age = int(input("How old are you : "))
        if age > 18:
            print("You are old enough, let's proceed")
            print("User maturity/disorder test. Let's begin!\nPlease answer the question if you will to follow us")
            user_answer = input("What is 9*10?")
            if user_answer.isnumeric() == True:
                print("You are ready to go")
                username = input("Enter your user name\nNOTE:user name should be alphanumeric : ")
                if username.isalnum() == True:
                    print("You have successfully registered {} {} \nYour username is {}".format(first_name,second_name,username))
                else:
                    print("This user name is invalid")
                    print("Enter correct username as we mentioned it should be alphanumeric")
                    username = input()
                    if username.isalnum() == True:
                        print("You have successfully registered {} {}Your username is {}".format(first_name,second_name,username))
                    else:
                        print("Sorry login failed")
            else:
                print("your answer is incorrect \nSorry unmaturity or disorder people are not allowed")
        else:
            print("Sorry {} {} come back after {} years".format(first_name, second_name, 18-age))
    else:
        print("Thank you")
elif first_name.isalpha() != True:
    print("Please Check your first name")
    first_name = input("Reenter your first name : ")
    if first_name.isalpha() == True:
        print("{} {} Welcome".format(first_name, second_name))
    print("Do you wish to continue with us yes or No?")
    y = "yes"
    N = "No"
    user = input()
    if user == y:
        age = int(input("How old are you : "))
        if age > 18:
            print("You are old enough, let's proceed")
            print("User maturity/disorder test. Let's begin!\nPlease answer the question if you will to follow us")
            user_answer = input("What is 9*10?")
            if user_answer.isnumeric() == True:
                print("You are ready to go")
                username = input("Enter your user name\nNOTE:user name should be alphanumeric : ")
                if username.isalnum() == True:
                    print("You have successfully registered {} {} \nYour username is {}".format(first_name,second_name,username))
                else:
                    print("This user name is invalid")
                    print("Enter correct username as we mentioned it should be alphanumeric")
                    username = input()
                    if username.isalnum() == True:
                        print("You have successfully registered {} {}Your username is {}".format(first_name,second_name,username))
                    else:
                        print("Sorry login failed")
            else:
                print("your answer is incorrect \nSorry unmaturity or disorder people are not allowed")
        else:
            print("Sorry {} {} come back after {} years".format(first_name, second_name, 16-age))
    else:
        print("Thank you")
elif second_name.isalpha() != True:
    print("Please check your second name")
    second_name = input("Please re enter your second name : ")
    if second_name.isalpha() == True:
        print("{} {} welcome".format(first_name, second_name))
    print("Do you wish to continue with us yes or No?")
    y = "yes"
    N = "No"
    user = input()
    if user == y:
        age = int(input("How old are you : "))
        if age > 18:
            print("You are old enough, let's proceed")
            print("User maturity/disorder test. Let's begin!\nPlease answer the question if you will to follow us")
            user_answer = input("What is 9*10?")
            if user_answer.isnumeric() == True:
                print("You are ready to go")
                username = input("Enter your user name\nNOTE:user name should be alphanumeric : ")
                if username.isalnum() == True:
                    print("You have successfully registered {} {} \nYour username is {}".format(first_name,second_name,username))
                else:
                    print("This user name is invalid")
                    print("Enter correct username as we mentioned it should be alphanumeric")
                    username = input()
                    if username.isalnum() == True:
                        print("You have successfully registered {} {}Your username is {}".format(first_name,second_name,username))
                    else:
                        print("Sorry login failed")
            else:
                print("your answer is incorrect \nSorry unmaturity or disorder people are not allowed")
        else:
            print("Sorry {} {} come back after {} years".format(first_name, second_name, 16-age))
    else:
        print("Thank you")
else:
    print("Your name is not valid, Retry again")
