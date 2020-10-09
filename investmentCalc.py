import locale
locale.setlocale(locale.LC_ALL, '') #sets local currency for formatting of output

def calculateTenYears(number, additionalContribution):
    totalAmount = number
    for i in range (1, 121, 1):
        totalAmount = totalAmount + totalAmount * 7 / 100 / 12 + additionalContribution
        #7% yearly, divided by 100 (%), divided by 12 month in a year
        #additional contribution is a monthly contribution
    formattedTotal = locale.currency(totalAmount, grouping = True) #format the string to show dollars and commas between digits
    print('In 10 years your investment account would be around...')
    print(formattedTotal)    
    
print('Initial amount: ')
amount = int(input())
print('Amount of monthly contribution: ')
monthly = int(input())
calculateTenYears(amount, monthly)
