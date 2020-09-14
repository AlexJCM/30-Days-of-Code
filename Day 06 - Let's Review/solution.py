# Enter your code here. Read input from STDIN. Print output to STDOUT
number_words = int(input())
for i in range(number_words):
    even_letters = ""
    odd_letters = ""
    word = input()

    for j in range(len(word)):
        if (j % 2 == 0):
            even_letters = even_letters + word[j]
        else:
            odd_letters = odd_letters + word[j]

    print(even_letters, odd_letters)

# Option 2
# number_words = int(input())
# for i in range(number_words):
#    word = input()
#    print(word[::2], word[1::2])
