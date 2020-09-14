# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_guide = {}

for _ in range(n):
    name, number = input().split()
    phone_guide[name] = number

while True: 
    try:
        search_string = str(input())
        if(search_string in phone_guide):
            print(search_string + "=" + phone_guide[search_string])
        else:
            print("Not found")
    except:
        break
