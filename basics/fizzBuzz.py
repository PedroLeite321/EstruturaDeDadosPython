#print variables that are divisible by 3 as fizz, 5 as buzz, and if a variable is divisible by both, print fizzbuzz
from random import randint
import random

def fizzBuzz(var):
    notDivisibleNums = []
    for var in range(0, len(var)):
        if var % 3 == 0 and var % 5 == 0:
            print(str(var) + " Fizz")
            continue
        elif var % 5 == 0:
            print(str(var) + " Buzz")
            continue
        elif var % 3 == 0:
            print("FizzBuzz")
            continue
        else:
            notDivisibleNums.append(var)
        
        


def randomNumberGenerator():
    generatedNumber = []
    for iterator in range(0, 20):
        rand = random.randint(1,20)
        generatedNumber.append(rand)

    return generatedNumber
list = randomNumberGenerator()
fizzBuzz(list)
    

