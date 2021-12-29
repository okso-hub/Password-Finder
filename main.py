from random import choice
from os import system
import string
import timeit

start = timeit.default_timer()
counter = 0
clear = lambda: system("clear")
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$%&/)(!"?=§öäü'


def split(word):
    return [char for char in word]


def main(counter=counter):
    clear()
    raw_password = str(input("Enter password: "))
    generated_password = ""

    while generated_password != raw_password:
        generated_password = ""

        for _ in range(len(raw_password)):
            generated_password += choice(string.ascii_letters)

        print(generated_password)
        clear()
        counter += 1
    else:
        print(f"Done. The password is {generated_password}")
        stop = timeit.default_timer()
        print(f"Runtime: {stop - start} \nTries: {counter}")


if __name__ == "__main__":
    main()
