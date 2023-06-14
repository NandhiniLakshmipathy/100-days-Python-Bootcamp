print ("Welcome to the Tip Calculator")

#  Getting user inputs

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15 or 20 "))
people = int(input("How many people to split the bill? "))

#  Calculating Total bill with tip

tip_percent = tip/100
tip_amount = tip_percent * bill
total_bill = bill + tip_amount
bill_with_tip = "{:.2f}".format(total_bill/people)
print(f"Each person should pay: ${bill_with_tip}")
