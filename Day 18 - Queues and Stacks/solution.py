
class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    # LIFO
    def pushCharacter(self, ch):
        """Add an value passed as an argument to the top of the stack"""
        self.stack.append(ch)

    def popCharacter(self):
        """Remove the value at the top of the stack and return it."""
        return self.stack.pop()

    # FIFO
    def enqueueCharacter(self, ch):
        """Add an value to the back of the line."""
        self.queue.append(ch)

    def dequeueCharacter(self):
        """Remove the value at the head of the line and return it; the element
        that was previously second in line is now  at the head of the line"""
        #char = self.queue[0]
        #self.queue = self.queue[1:]
        # return char
        # Or
        return self.queue.pop(0)


# read the string word
word = input()
length_word = len(word)

# Create the Solution class object
obj = Solution()

# push/enqueue all the characters of string word to stack and queue
for i in range(length_word):
    obj.pushCharacter(word[i])
    obj.enqueueCharacter(word[i])

isPalindrome = True
'''Pop the top character from stack
dequeue the first character from queue
compare both the characters'''
for i in range(length_word // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

# finally print whether string word is palindrome or not.
if isPalindrome:
    print("The word, " + word + ", is a palindrome.")
else:
    print("The word, " + word + ", is not a palindrome.")
