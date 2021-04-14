class Node:
    def __init__(self, root):
        self.value = root
        self.left = None
        self.right = None
    
class TTraversal:
    def __init__(self, root):
        self.root = Node(root)
    

    def pre_order(self, start, traversal):
        """root>left>right"""
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal
"""
                1
        2               3
    4       5
6       7
"""
    

tree = TTraversal(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.left.left = Node(6)
tree.root.left.left.right = Node(7)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)
tree.root.right.right.left = Node(10)
tree.root.right.right.right = Node(11)

print(tree.pre_order(tree.root.left.left, ' '))




