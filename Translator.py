# ------------------ day 7

def translate(phrase):                             # defines a translation where user will enter a phrase
    translation = ""                               # translation is a blank string
    for letter in phrase:                          # sets a loop, so for every letter in the entered phrase
        if letter.lower() in "aeiou":              # and if the letter in the phrase is a vowel (and change lower case)
            if letter.isupper():                   # if the letter entered is upper case
                translation = translation + "Hurr" # then add the following string with a capital letter
            else:                                  # if not..
                translation = translation + "hurr" # the translation will add the string in lower case
        else:                                      # if this above is not true and a consonant is entered instead...
            translation = translation + letter     # then the program will add the letter to the output
    return translation                             # returns the variable

print(translate(input("Enter a phrase: ")))        # prints the translate function and asks user to input a string

