value = input().strip()

try:
    print(int(value))
except ValueError:
    print('Bad String')
