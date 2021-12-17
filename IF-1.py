# -------------------------- day 5

is_christmas = False                       # sets a true or false boolean for the variable containers
is_snowing = False
is_wonderful_time = False
is_december = True

if is_christmas or is_snowing:             # initialises IF statement to print the below if one or the other are True
    print("It's Christmaasssss! ..or it's snowing")
elif is_christmas and (is_snowing):        # prints string if both variables are True
    print("We're simply having a wonderful Christmas time")
elif not(is_christmas) and (is_snowing):        # prints string if both variables are True
    print("It's snowing!")
else:                                      # if this is not true then prints the below string instead
    print("It's not Christmas and it's not snowing")
if is_december and not(is_wonderful_time):          # if the first variable is true and the second is false then prints
    print("Bar Humbug")
