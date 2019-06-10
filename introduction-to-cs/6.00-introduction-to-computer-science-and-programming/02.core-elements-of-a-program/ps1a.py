# Problem Set 1a
# Name: Eloi Gil
# Time Spent: 1
#

balance = float(input('balance: '))
annualInterestRate = float(input('annual interest rate: '))
minMonthlyPaymentRate = float(input('minimum monthly payment rate: '))

month = 0.0
while month < 12.0:
    month += 1.0
    print('Month ' + str(month))
    minMonthlyPayment = round(balance * minMonthlyPaymentRate, 2)
    print('minimum monthly payment: ' + str(minMonthlyPayment))
    interestPaid = round(annualInterestRate / 12.0 * balance, 2)
    principlePaid = round(minMonthlyPayment - interestPaid, 2)
    print('principle paid: ' + str(principlePaid))
    balance -= round(principlePaid, 2)
    print('remaining balance: ' + str(round(balance, 2)))
