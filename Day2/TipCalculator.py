#tip calculator
# Give the total bill, tip percentage and total number of people to split among. It will provide the output each individual has to pay

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_per = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
total_people = int(input("How many people to split the bill? "))
each_person_bill = round((((tip_per/100)*total_bill)+total_bill)/total_people, 2)
print(f"Each person should pay: ${each_person_bill}")