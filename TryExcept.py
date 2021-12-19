# ---------------------- day 7

# Try / Except is a process of using code to find where an error is occurring in your code

try:                                              # the code will first try the indented code
    number = int(input("Enter a number: "))
    print(number)
except:                                           # if an error occurs then the below code will follow
    print("Invalid input")                        # prints the string
