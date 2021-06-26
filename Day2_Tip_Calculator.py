bill_amt = float(input("Enter the bill amount : "))
tip_amt = int(input("How much percentage, do you want to tip 12%,10%,5% ?"))
num_per = int(input("How many people to split the bill ?"))
tip_percent = tip_amt/100 * bill_amt

total_bill = bill_amt + tip_percent
bill_per_person = total_bill / num_per
print("{:.2f}".format(bill_per_person))
