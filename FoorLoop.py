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
