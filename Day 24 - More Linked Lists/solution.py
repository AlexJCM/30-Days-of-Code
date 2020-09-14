class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while(start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    # Solution 1
    def removeDuplicates(self, head):
        if (head == None or head.next == None):
            return head
        if (head.data == head.next.data):
            head.next = head.next.next
            self.removeDuplicates(head)
        else:
            self.removeDuplicates(head.next)
        return head

    # Solution 2
    # def removeDuplicates(self, head):
    #     if (head == None or head.next == None):
    #         return head
    #     current = head
    #     while(current.next):
    #         if(current.data == current.next.data):
    #             current.next = current.next.next
    #         else:
    #             current = current.next
    #     return head


"""Task: Given a node object with integer data field data, a
nd instance pointer next which points to the next node, you’ll 
need to use the removeDuplicates function to delete any duplicate 
nodes within the list and then return the head of the newly updated list."""

my_list = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = my_list.insert(head, data)
head = my_list.removeDuplicates(head)
my_list.display(head)
