# ------------------ day 6

for letter in "Pineapple":          # for every letter in string, print each letter in a loop and end when finished
    print(letter)

instruments = ["guitar", "drums", "Bass"]        # creates a list with strings
for instrument in instruments:                   # sets a variable (instrument) for the values in instruments list
    print(instrument)                            # and prints each instrument

print(len(instruments))                          # prints the number of items in instruments list

for index in range(0, 10):                       # sets a variable (index) in a range between 0 and 10 (not including 10
    print(index)                                 # prints the specified index

for index1 in range(len(instruments)):           # creates a for loop and will print the length of the list
    print(instruments[index1])                   # prints each individual item in the list

for index2 in range(5):                          # creates a loop that repeats 5 times
    if index2 == 0:                              # if this is the first loop then print the string
        print("first iteration")
    else:                                        # if the loop is on the second to fifth loop then print the string
        print("not first")


# ------------------ day 7

# Exponent function

def raise_to_power(base_num, pow_num):           # creates a function with two parameters
    result = 1                                   # creates a variable where we store the result of the math
    for index3 in range(pow_num):  # loops through the range of numbers from zero up to (not including) the power number
        result = result * base_num               # each loop multiplies the result by the base number
    return result                                # returns to result

print(raise_to_power(3, 2))                      # specifies the base number and power number, then prints the function