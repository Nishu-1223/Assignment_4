# Task 2: Write and Append Data to a File

user_input1= input("Enter text to write to the file: ")
print("Data successfully written to output.txt.")

with open("output.txt","w")as file:
    file.write(user_input1 +"\n")

user_input2 = input("\nEnter additional text to append: ")
print("Data successfully appended.")
with open("output.txt","a") as file:
     file.write(user_input2 + "\n")

print("\nFinal content of output.txt:")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)


