"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

def check_sales_valid(original_num):
    while True:
        try:
            new_numeral = float(original_num)
        except ValueError:
            print("That's an incorrect value. Just enter a number, please.")
            original_num = input("$")
            continue
        else:
            return(new_numeral)

sales = float(check_sales_valid(input("Enter sales: $")))

if sales >= 1000:
    bonus = sales * 0.15
    print("Your bonus for this sales season is $" + str(bonus))
elif sales < 1000 and sales > 0:
    bonus = sales * 0.1
    print("Your bonus for this sales season is $" + str(bonus))
elif sales <= 0:
    print("That's an incorrect value. Your power is too low.")

print("Bonus Loop Time")

sales = input("Enter the Bonus Loop Sales: $")
check_sales_valid(sales)
sales = float(sales)

while sales >= 0:
    if sales >= 1000:
        bonus = sales * 0.15
        print("Your bonus for this sales season is $" + str(bonus))
    elif sales < 1000:
        bonus = sales * 0.1
        print("Your bonus for this sales season is $" + str(bonus))
    sales = input("Enter the Bonus Loop Sales: $")
    check_sales_valid(sales)
    sales = float(sales)
print("Your power is weak.")