'''
Shop calculator program. Asks for total amount of items, enters price for each, calculates total.
Apples 10% discount if total is over $100
'''

def check_num_valid(original_num):
    while True:
        try:
            new_numeral = float(original_num)
        except ValueError:
            print("That's an incorrect value. Just enter a number, please.")
            original_num = input("")
            continue
        else:
            return new_numeral

def num_negative(original_num):
    while original_num < 0:
        print("No negatives. Try again.")
        new_numeral = check_num_valid(input("$"))
        return new_numeral
    else:
        return original_num

print("Please enter the total amount of items.")
total_amount = 0
number_items = int(check_num_valid(input()))

while number_items < 0:
    print("No negative items. Try again.")
    number_items = int(check_num_valid(input()))

for i in range(0, number_items, 1):
    total_amount = total_amount + int(num_negative(check_num_valid(input("Enter cost of item: $"))))

if total_amount >= 100:
    print("You've earned a discount!")
    total_amount = total_amount * 0.9

print("The total amount of goods is $" + str(total_amount))
