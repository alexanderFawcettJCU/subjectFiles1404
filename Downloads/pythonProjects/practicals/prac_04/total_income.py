"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    amount_months = int(input("How many months? "))

    for amount_months in range(1, amount_months + 1):
        income = float(input("Enter income for month {}: ".format(amount_months)))
        incomes.append(income)
    income_report(amount_months, incomes)


def income_report(amount_months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for amount_months in range(1, amount_months + 1):
        income = incomes[amount_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(amount_months, income, total))


main()
