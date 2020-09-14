import math


def isPrime(number):
    if (number == 2):
        print("Prime")
    elif (number < 2):
        print("Not prime")
    else:
        if (number % 2 == 0):  # Check if the value is even
            print("Not prime")
        else:
            for i in range(2, math.ceil(math.sqrt(number))+1):
                if (number % i == 0):
                    number = 1
                    break
            if (number == 1):
                print("Not prime")
            else:
                print("Prime")


n = int(input())
for i in range(n):
    number = int(input())
    isPrime(number)
