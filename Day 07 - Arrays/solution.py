n = int(input())
arr = list(map(int, input().rstrip().split()))

reverse = ""
for i in range(n-1, -1, -1):
    reverse += str(arr[i]) + " "
print(reverse)

# Option 2
# aux = ""
# for i in range(len(arr))[::-1]:
#   aux = aux + str(arr[i]) + " "
# print(aux)

# Option 3
# print(" ".join(map(str, arr[::-1])))
