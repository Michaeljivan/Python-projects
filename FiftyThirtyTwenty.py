# The Fifty Thirty Twenty Salary Budgeter

balance = float(input("Amount $"))

def savings_fifty_percent(balance):
	savings = (balance * 0.50)
	return savings


def essentials_thirty_percent(balance):
	essentials = (balance * 0.30)
	return essentials


def spending_twenty_percent(balance):
	spending = (balance * 0.20)
	return spending



print("(50%)Money for Savings:\t\t\t", savings_fifty_percent(balance))
print("(30%)Money for Essentials:\t\t", essentials_thirty_percent(balance))
print("(20%)Money for Spending:\t\t", spending_twenty_percent(balance))