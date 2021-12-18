# ----------------------------- day 5

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(422, 50, 63))

# !=     not equal to
# ==     equal to
# >      greater than
# <      less than
# >=     more than, or equal to
# <=     less than, or equal to
