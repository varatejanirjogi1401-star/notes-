# Write a python program that asks the user for their name and age, then prints a greeting with their age next year.
name = input("Enter the name of the person: ") # Get the name of the person from user input 
age = int(input("Enter the age of the person: ")) # Get the age of the person from user input and convert it to an integer
age = age+1 # Increment the age by 1 to get the age next year
print(f"Hello {name}, your age in next year is {age}")
