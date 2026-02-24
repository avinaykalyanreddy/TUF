"""
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
"""

class Solution:
    def sumRootToLeaf(self, root ):

        bits = []

        def traverse(root):

            if not root:

                return 0

            if (not root.left and not
            root.right):

                bits.append(str(root.val))
                x = int("".join(bits),2)
                bits.pop()

                return x

            bits.append(str(root.val))

            left = traverse(root.left)
            right = traverse(root.right)

            bits.pop()
            return left + right

        return traverse(root)