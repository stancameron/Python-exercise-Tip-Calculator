#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator!!")
bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10,12 or 15? ")
num_of_people = input("How many people to split the bill ")
people = int(num_of_people)

#changed the string to float
cons_bill = float(bill)
cons_tip = int(tip_percent)

#calculations 
tip_with_cons_bill = cons_bill * (cons_tip/100) + cons_bill
each_person = tip_with_cons_bill / people

result = round(each_person,2)

#"{:.2f}".format() changes the format of the code to string 
result = "{:.2f}".format(each_person)


print(f"Each person should pay: ${result}")
