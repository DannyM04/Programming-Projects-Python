# Lines 2-4 inquire the user on what currency they use, what income they make per annum and their tax percentage.
userCurrency = input("Please enter your local currency symbol (eg. £ or $) ")
userIncomeYearly = input("How much money do you make per annum? ").replace(',', '')
userIncomeYearly = float(userIncomeYearly)
userIncomeTaxPercentage = input("What is your income tax percentage? ").replace('%', '')
userIncomeTaxPercentage = float(userIncomeTaxPercentage)

# Lines 9-12 calculates the monthly income of the user after their taxes.
userIncomeTax = userIncomeYearly * (userIncomeTaxPercentage / 100)
userIncomeYearlyAfterTax = userIncomeYearly - userIncomeTax
userIncomeMonthly = userIncomeYearlyAfterTax / 12
userIncomeMonthly = round(userIncomeMonthly, 2)

print("You have", userCurrency, userIncomeMonthly, "Per month")
print("Now, add all your montly expenses")

# Line 17 creates a list for the expenses the user has.
expenses = []

# addExpense function asks the user for the name and amount of their expense then inquires if they have any others to add. If not, the function ends.
def addExpense():
    while True:
        expenseName = input("Please enter expense name: ")
        expenseAmount = float(input("Please enter the expense amount (per month): "))
        
        #Each expense is created as a dictionary and then appended to the expenses list.
        expense = {'name': expenseName, 'amount': expenseAmount}
        expenses.append(expense)
        
        moreExpenses = input("Do you have another expense to add? (yes/no): ")
        if moreExpenses == 'no':
            break

addExpense()

# Lines 37-40 should display the expenses they have added.
print("Current list of expenses: ")
print(expenses)
for expense in expenses:
    print(f"{expense['name']}: {userCurrency} {expense['amount']}")

expenseTotal = sum(expense['amount'] for expense in expenses)

# Lines 45-52 calculate how much disposable income the user has and what percentage of their expenditure takes up their income.
userDisposableIncome = userIncomeMonthly - expenseTotal
print("Total expenses: ", userCurrency, expenseTotal)
print("After your expenses and taxes, you have: ", userCurrency, userDisposableIncome, "per month")

userExpenditurePercentage = (expenseTotal / userIncomeMonthly) * 100
userExpenditurePercentage = round(userExpenditurePercentage, 2)

print("Your expenditure takes up ", userExpenditurePercentage, "% of your income")

if expenseTotal > userIncomeMonthly:
    print("Your expenditure is not sustainable! Please try to cut back on your spending")