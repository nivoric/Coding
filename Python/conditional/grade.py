user_input = input("Enter your grade: \n=> ")

if user_input == "":
    print("No input!")
try:
    num = int(user_input)
    if num >= 90:
        print("this deserves an A+!")
    elif num >= 80:
        print("This deserves a B+")
    elif num >= 70:
        print("This deserves a C+")
    elif num <= 60:
        print("This is unacceptable")
except ValueError:
    print("Just enter a number!")
