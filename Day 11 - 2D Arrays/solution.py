if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    total_sum = 0
    maximun = -9 * 7  # Minimum value that can have the sum of an hourglass
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            total_sum = total_sum + arr[i][j] + arr[i][j+1] + arr[i][j+2]
            total_sum = total_sum + arr[i+1][j+1]
            total_sum = total_sum + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if (total_sum > maximun):
                maximun = total_sum
            total_sum = 0

    print(maximun)
