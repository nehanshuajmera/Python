# Bill Calculation
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percent = tip / 100
total = bill * percent + bill
people = int(input("How many people to split the bill? "))
pay = round(total / people, 2)
print(pay)