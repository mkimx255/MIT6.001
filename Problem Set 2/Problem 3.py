balance = 320000
annualInterestRate = 0.2

initialBalance = balance
monthlyInterestRate = (annualInterestRate) / 12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
monthlyPayment = (lowerBound + upperBound) / 2
count = 0
epsilon = 0.01
while True:
    monthlyPayment = (lowerBound + upperBound) / 2
    while count < 12:
        balance = balance - monthlyPayment
        balance = balance + (monthlyInterestRate * balance)
        count += 1
    if balance < -epsilon:
        upperBound = monthlyPayment
    elif balance > epsilon:
        lowerBound = monthlyPayment
    elif abs(balance) <= epsilon:
        minimumPayment = monthlyPayment
        break
    balance = initialBalance
    count = 0
print("Lowest Payment: " + str(round(minimumPayment, 2)))