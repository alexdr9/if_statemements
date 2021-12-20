# -------------------- day 8

employee_file = open("Employees.txt", "w")           # Opens the file and stores as variable, opens in write mode
                                                     # if the file name is not already an existing file then python
                                                     # will create a new file with the name entered in the string when
                                                     # opened with a "w" function

employee_file.write("\nAlex - Legend")                  # when opened in write mode, the string entered here will
                                                        # overwrite everything else that is already in the file

employee_file.close()                                   # closes the file


new_file = open("index.html", "w")                          # creates a new file called 'index' in .html format

new_file.write("<dev>Hi, this is a new HTML file</dev")     # writes a new line to the file in html coding language

new_file.close()                                            # closes the file
