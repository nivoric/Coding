user_input = input("Enter your number: \n=> ")
if user_input == " ":
    print("There is no input")
try:
    num = int(user_input)
    if num > 0:
        print("This number is positive!")
    elif num < 0:
        print("This number is negative!")
    elif num == 0:
        print("This number is zero!")
except ValueError:
    print("Invalid input")
