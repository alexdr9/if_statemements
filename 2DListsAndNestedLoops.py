# ------------------ day 7

number_grid = [                  # creates a lists (array) called number_grid
    [1, 2, 3],                   # creates more lists within a list containing integer values
    [4, 5, 6],
    [7, 8, 9],
    [0]
]                                # closes the list

print(number_grid[0][0])         # prints row position 0, column position 0 (in this case being number 1 in the list)
print(number_grid[1][2])         # prints number 6 from the lists (positions start from 0, not 1)

