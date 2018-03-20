'''user chosen lines of 6 numbers, sorted in ascending order, has to be unique picks between 1 and 45'''
import random

def main():
    amount_lines = int(input("How many lines of Quick Picks today?" ))
    for quick_picks_list in range(1, amount_lines+1):
        LIST = []
        for i in range(6):
            new_num = random_num(LIST)
            LIST.append(new_num)
        print(sorted(LIST))

def random_num(list):
    rand_control = 0
    while rand_control == 0:
        rand_num = random.randint(1,45)
        if rand_num in list:
            rand_control = 0
        else:
            rand_control = 1
    return rand_num

main()

