if __name__ == '__main__':
    n = int(input())
    counter = 0
    maximun = 0

    while n != 0:
        if (n % 2 == 1):
            counter += 1
            if (counter > maximun):
                maximun = counter
        else:
            counter = 0

        n = n // 2  # floor division

    print(maximun)
