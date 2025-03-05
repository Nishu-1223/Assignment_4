# Task 1: Read a File and Handle Errors

file_name=input("Enter a file name:")
try:
    with open(file_name, "r") as file:
        for line in file:
            print(line, end="")

except FileNotFoundError:
    print(f"The file {file_name} was not found.")
