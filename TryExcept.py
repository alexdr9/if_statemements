# ---------------------- day 7

# Try / Except is a process of using code to find where an error is occurring in your code

try:                                              # the code will first try the indented code
    value = 10 / 0                                # this will throw an error overruling the below error, because..
                                                  # 10/0 is not possible in maths, so we need to make an exception
    number = int(input("Enter a number: "))       # this will error if the user inputs a string instead of an int number
    print(number)
except ZeroDivisionError:                         # 10/0 will output a zerodiv error so we except it and print the below
    print("Zero division error")
except ValueError:                                # if user enters a string then python will output a value error
    print("Invalid input")                        # prints the string
except ZeroDivisionError as err:                  # this will print the error in the below variable
    print(err)