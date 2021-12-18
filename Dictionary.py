# ----------------- day 6

month_conversions = {                      # creates a dictionary called month_conversions using a { symbol
    "Jan": "January",                      # creates a key: and a value linked to the key
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: "First month"                     # numbers can also be used in dictionaries
}                                        # } closes the dictionary

print(month_conversions["Dec"])          # prints the value associated with the key
print(month_conversions.get("Dec"))      # this .get function will also work here to get the value for Dec

print(month_conversions.get("Luv", "Not a valid key"))      # if the program cannot find the key then "not a
                                                            # valid key" will be printed
