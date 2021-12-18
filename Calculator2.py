# ------------------ day 6

num1 = float(input("Enter the first number: "))     # num1 variable will be input by the user as a float (decimal number
op = input("Enter the operator: ")                  # operator key entered by the user is stored in a variable container
num2 = float(input("Enter the second number: "))    # num2 variable will be input by the user as a float (decimal number

if op == "+":                                       # if op input by user is equal to a plus symbol then
    print(num1 + num2)                              # print num1 plus num2
elif op == "-":                                     # if the input is not a plus symbol then
    print(num1 - num2)                              # print num1 minus num2, and so on...
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:                                               # if the input is none of the symbols above then print the below
    print("Invalid operator")

