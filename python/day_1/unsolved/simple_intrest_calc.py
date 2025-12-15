# Take principal amount, rate of interest and time in years from the user. Compute simple interest = (P*T*R)/100 and display it. (Remember to convert inputs to numbers)
P = int(input("Enter the principle amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))
SImple_Intrest = (P*R*T)/100
print(f"The simple intrest is: {SImple_Intrest}")