class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    # Solution 1
    def insert(self, head, data):
        if (head == None):
            head = Node(data)
        else:
            curr_node = head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = Node(data)

        return head

    # Solution 2 (Recursive method)
    # def insert(self, head, data):
    #     if (head == None):
    #         head = Node(data)
    #     elif (head.next == None):
    #         head.next = Node(data)
    #     else:
    #         self.insert(head.next, data)

    #     return head


# A linked list is composed of nodes, each node containing
# a data field and a following field pointing to the next element
# in the list (or null if it is the last element in the list)
linked_list = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = linked_list.insert(head, data)
linked_list.display(head)
