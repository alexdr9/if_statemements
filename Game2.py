# -------------- day 6

secret_word = "mongo"                           # sets the variable to a string
guess = ""                                      # sets a blank string variable
guess_count = 0                                 # sets a variable for the guess count and makes it equal to zero
guess_limit = 3
out_of_guesses = False                          # sets a false value for variable

while guess != secret_word and not(out_of_guesses):    # creates a while loop, if the user input is not the secret word,
    if guess_count < guess_limit:
        guess = input("Guess the secret word: ")           # then repeat the while loop to continue guessing
        guess_count += 1                                   # adds 1 to the guess count
    else:
       out_of_guesses = True
if out_of_guesses:
    print("You are a mongo and you have lost the game")
else:
    print("You are a mongo!")                              # when user enters the correct guess, prints the string
