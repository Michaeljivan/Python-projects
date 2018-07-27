def atm(withdraw, funds, fee):
	if(withdraw > funds):
		result = funds
	elif(withdraw < funds):
		result = (funds - withdraw) - fee
	return result

x = float(input())
y = float(input())

if(x > 0 and x<= 2000):
	if(x % 5 == 0):
		withdraw_a = x
		fee = 0.50
	else:
		withdraw_a = 0
		fee = 0

if(y >= 0 and y <= 2000):
	account_b = y

print(atm(withdraw_a, account_b, fee))
