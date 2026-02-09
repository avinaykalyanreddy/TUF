"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

"""
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_arr = []

        def inorder(root):

            if not root:

                return

            inorder(root.left)

            sorted_arr.append(root)

            inorder(root.right)

        inorder(root)


        def balance_tree(sorted_arr):

            n = len(sorted_arr)

            mid = n//2

            def build_tree(sorted_arr,left,right):

                if left > right:

                    return None

                mid = (left+right)//2

                node = sorted_arr[mid]

                node.left = build_tree(sorted_arr,left,mid-1)
                node.right = build_tree(sorted_arr,mid+1,right)
                return node
            node = sorted_arr[mid]

            node.left = build_tree(sorted_arr,0,mid-1)
            node.right = build_tree(sorted_arr,mid+1,n-1)

            return node

        return balance_tree(sorted_arr)

"""
Time complexity --> O(n)
Space complexity --> O(n)
"""