import re


def sortNames(names):
    number_swaps = 0
    for i in range(len(names)):
        for i in range(len(names)-1):
            if (names[i] > names[i+1]):
                temp = names[i]
                names[i] = names[i+1]
                names[i+1] = temp
                number_swaps += 1
        if (number_swaps == 0):
            return names
    return names


if __name__ == '__main__':
    N = int(input())

    pattern = r".*\@gmail.com$"
    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if re.match(pattern, emailID):
            names.append(firstName)

    # Solution 1
    sorted_names = sorted(names)
    for i in range(len(sorted_names)):
        print(sorted_names[i])

    # Solution 2
    # print(*sorted(names), sep='\n')

    # Solution 3
    # print("\n".join(sortNames(names)))
