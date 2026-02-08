"""
Given a binary tree, determine if it is height-balanced.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)

root.right = TreeNode(2)

root.right.right = TreeNode(3)

x = True

def traverse(root):

    global x
    if not root:

        return 0


    left = traverse(root.left)
    right = traverse(root.right)

    if abs(left-right) > 1:

        x = False

    return max(left,right)+1


traverse(root)
print(x)