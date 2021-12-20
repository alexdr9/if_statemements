# --------------- day 8

employee_file = open("Employees.txt", "a")               # opens the file and allows the ability to append and add
                                                         # items to the end of the existing data

print(employee_file.readable())                          # states in boolean if the file is readable to python or not

employee_file.write("\nAlex - Legend")                   # writes new data to the file on a new line

employee_file.close()
