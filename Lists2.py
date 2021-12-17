
# -------------------------------- day 4

instruments = ["Guitar", "Bass", "Drums", "Keyboard", "Bongos", "Bongos"]

instruments.append("Full Orchestra")                    # append function adds another item to the lists
instruments.insert(1, "Vocals")                         # inserts a new string to index position 1 in list
instruments.remove("Keyboard")                          # removes item from the list
number_of_instruments = [1, 2, 3, 4]

name_of_members = ["Liam", "Alex", "Curtis"]
name_of_leavers = ["Luke"]

name_of_leavers.clear()                                 # Clears all items from the list
instruments.pop()                                       # removes the item at the end of the list

instruments.extend(number_of_instruments)               # extend function adds another list to the primary list

print(name_of_members)                                  # items were cleared so doesn't print

print(instruments)

instruments.reverse()                                   # reverses the position of items in the list

print(instruments.index("Drums"))                       # prints the index position of the string
print(instruments.count("Bongos"))                      # prints the count number of items for the entered string

name_of_members2 = name_of_members.copy()               # copies the list to a new list
name_of_members2.sort()                                 # sorts the items in the list in alphabetical order
print(name_of_members2)

