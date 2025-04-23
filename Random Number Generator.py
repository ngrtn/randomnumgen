import random
def reset():
        res = str(input('\nDo you want to reset? y/n: '))
        if res == 'y':
            main()
        if res == 'n':
            print()

def main():
    frst_num = int(input('\nWelcome to Random Number Generator! To start type first number: '))
    scnd_num = int(input('Now type second number!: '))
    if scnd_num < frst_num:
        print('First number must be greater than second number!')
        main()
    if scnd_num == frst_num:
        result = random.randint(frst_num, scnd_num)
        print('Not random number is:', result)
        reset()
    else:
        result = random.randint(frst_num, scnd_num)
        print('Random number is:', result)
        reset()
main()