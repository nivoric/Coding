user_input = input("Enter your number; \n=> ")

if user_input == "":
    print("nothing inserted!")

else:
    try:
        num = int(user_input)
        if num % 2 == 0:
            print("This is an even number")
        else:
            print("This is an odd number")
    except ValueError:
        print("Please enter a number only!")
