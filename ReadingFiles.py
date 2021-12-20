# ------------------ day 8

# reading files in Python

# open("Employees.txt", "r")         # opens file in local directory with the ability to read its contents
# open("Employees.txt", "w")         # opens file in local directory with the ability to write or change its contents
# open("Employees.txt", "a")         # opens file in local directory with the ability to append, or add data to the file
# open("Employees.txt", "r+")        # opens file in local directory with the ability to read and write

employee_file = open("Employees.txt", "r")       # opens the read only file & saves its contents in a variable container

print(employee_file.readable())             # returns a true or false boolean to state if the file is readable in python
                                            # this only works if the file is opened in "r" state, as it is so above

print(employee_file.read())                 # the .read function displays all information in the file and prints it out

print(employee_file.readline())             # reads and prints out the first line of the file
print(employee_file.readline())             # duplicating this function will print each consecutive line from the file
print(employee_file.readline())             # prints the 3rd line, etc.

print(employee_file.readlines())            # prints all the lines and contains the information in a list/array

print(employee_file.readlines()[2])         # prints line 1 from the file
print(employee_file.readlines()[3])         # prints line 2 from the file, etc.

for employee in employee_file.readlines():   # stores employee as a variable and runs a for loop which prints every line
    print(employee)

employee_file.close()                        # files will need to be closed after being opened

