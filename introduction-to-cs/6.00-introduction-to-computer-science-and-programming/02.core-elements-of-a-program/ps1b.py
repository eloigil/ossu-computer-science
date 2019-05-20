# Problem Set 1b
# Name: Eloi Gil
# Time Spent: 1:30
#

initialBalance = float(input('Enter the outstanding balance on your credit card: '))
annualInterestRate = float(input('Enter the annual credit card interest rate as a decimal: '))
monthlyInterest = annualInterestRate / 12.0
monthlyPayment = 10.0
months = 1
balance = initialBalance

iterations = 0

while balance > 0.0:
    iterations += 1
    months = 1
    monthlyPayment += 10.0
    balance = initialBalance
    while months <= 12:
        balance = balance * (1.0 + monthlyInterest) - monthlyPayment
        if balance <= 0:
            break
        else:
            months += 1
            

print(months)
print(monthlyPayment)
print(round(balance, 2))

    
