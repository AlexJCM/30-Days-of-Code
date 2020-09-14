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
    def levelOrder(self, root):
        if root:
            queue = [root]
            # while len(queue) is not 0
            while queue:
                node = queue.pop()
                print(node.data, end=" ")
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)

    # Solution 2
    # def levelOrder(self, root):
    #     result = ""
    #     if root:
    #         queue = [root]
    #         while queue:
    #             result += str(queue[0].data) + " "
    #             if queue[0].left:
    #                 queue.append(queue[0].left)
    #             if queue[0].right:
    #                 queue.append(queue[0].right)
    #             queue.pop(0)
    #     print(result)


T = int(input())
my_tree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = my_tree.insert(root, data)
my_tree.levelOrder(root)
