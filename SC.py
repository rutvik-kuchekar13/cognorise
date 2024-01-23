print ("~~~~~Simple  Calculator~~~~~")

num1 = float(input("Enter a number here: "))
num2 = float(input("Enter another number here: "))

print ("""
Press 1 for Addition 
Press 2 for Subtraction
Press 3 for Multiplication
Press 4 for Division""")

choice = int(input("Enter a number between 1-4: "))

if choice == 1:
    sum = num1+num2
    print ("The Addition of the given two numbers is",sum)
elif choice == 2:
    print ("The Subtraction of the given two numbers is",num1-num2)
elif choice == 3:
    print ("The Multiplication of the given two numbers is",num1*num2)
elif choice == 4:
    print ("The Division of the given two numbers is",num1/num2)
else:
    print ("Invalid Input from the User")