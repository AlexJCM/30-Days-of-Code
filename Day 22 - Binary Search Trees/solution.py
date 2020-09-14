class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    # Solution 1
    def getHeight(self, root):
        if (root == None):
            return -1
        max_height = max(self.getHeight(root.left), self.getHeight(root.right))
        return max_height + 1

    # Solution 2
    # def getHeight(self, root):
    #     heigth_left = 0
    #     height_right = 0
    #     if (root != None):
    #         if root.left:
    #             heigth_left = self.getHeight(root.left) + 1
    #         if root.right:
    #             height_right = self.getHeight(root.right) + 1

    #         return max(heigth_left, height_right)

    #     return 0


T = int(input())
my_tree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = my_tree.insert(root, data)

height = my_tree.getHeight(root)
print(height)
