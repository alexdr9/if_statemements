# ----------------------------- day 5

def max_num(num1, num2, num3):                            # defines a function to find the largest number out of the 3
    if num1 >= num2 and num1 >= num3:                     # creates an if statement where if num1 is the largest
        return num1                                       # to return num1 back to the user, if not then go to next line
    elif num2 >= num1 and num2 >= num3:                   # else if statement to find if num2 is larger
        return num2                                       # if true then returns num2 to the user
    else:                              # else statement to close, if neither number is larger than num3 then print num3
        return num3

print(max_num(422, 50, 63))            # print the larger number

# !=     not equal to
# ==     equal to
# >      greater than
# <      less than
# >=     more than, or equal to
# <=     less than, or equal to
