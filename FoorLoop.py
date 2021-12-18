# ------------------ day 6

for letter in "Pineapple":          # for every letter in string, print each letter in a loop and end when finished
    print(letter)

instruments = ["guitar", "drums", "Bass"]        # creates a list with strings
for instrument in instruments:                   # sets a variable (instrument) for the values in instruments list
    print(instrument)                            # and prints each instrument

print(len(instruments))                          # prints the number of items in instruments list

for index in range(0, 10):                       # sets a variable (index) in a range between 0 and 10 (not including 10
    print(index)                                 # prints the specified index

for index1 in range(len(instruments)):           # 
    print(instruments[index1])                   # prints all items in instruments list
