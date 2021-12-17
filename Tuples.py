# ----------------------------- day 4

# lists will be contained in [], and can be modified. Tuples are stored in () and cannot be modified

coordinates = (4, 5)                                 # tuple stored in a variable container
print(coordinates[0])

coordinates2 = [(4, 5), (6, 7), (8, 9)]              # list of tuples stored in a variable container
print(coordinates2)


# functions

def say_hi(name, age):                                                   # defines a function
    print("Hi " + name + " you are " + str(age) + " years old.")         # prints function, converts integer to string

say_hi("Alex", 29)                                                       # calls the function
say_hi("Boyo", 29)


# return statements

def cube(num):                           # defines a function named 'cube' and it takes one value (an integer number)
    return num*num*num                   # python will execute the function and return the value when printed

result = (cube(3))                       # sets the result as a variable and returns the value
print(result)                            # prints the result

