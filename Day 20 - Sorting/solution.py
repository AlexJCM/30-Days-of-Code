n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

number_swaps = 0
for i in range(n):
    for j in range(n-1):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            aux = a[j]
            a[j] = a[j + 1]
            a[j + 1] = aux
            number_swaps += 1

    # If no elements were swapped during a traversal, array is sorted
    if (number_swaps == 0):
        break

print('Array is sorted in ' + str(number_swaps) + ' swaps.')
print('First Element:', a[0])
print('Last Element:', a[len(a) - 1])
