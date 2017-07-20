'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135 
So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0

'''

totalPaid = 0

#balance, annualInterestRate, monthlyPaymentRate = 42, 0.2, 0.04

for temp in range(12):
    # calculate the monthly interest rate
    monthlyInterestRate = annualInterestRate / 12.0

    # calculate the minimum monthly payment
    minMonthlyPayment = monthlyPaymentRate * balance

    # keep track of amount paid each month
    totalPaid = totalPaid + minMonthlyPayment

    # update the balance after minimum monthly payment
    monthlyBalance = balance - minMonthlyPayment

    # update the balance each month
    balance = monthlyBalance * ( 1 + monthlyInterestRate )

print('Remaining balance: ' + str(round(balance, 2)))

