# Take the user’s birth year as input and calculate their age in the year 2026. Print a message like ``You will be 20 years old in 2026.''
birth_year = int(input("Enter your birth year: "))
age_in_2026 = 2026 - birth_year
print(f"You will be {age_in_2026} years old in 2026.")