"""
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

"""


class Node:

    def __init__(self, start, end, total):
        self.start = start
        self.end = end
        self.total = total

        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = nums

        def build_segment_tree(arr, start, end):
            if start == end:
                return Node(start, end, arr[start])

            mid = (start + end) // 2

            left_child = build_segment_tree(arr, start, mid)
            right_child = build_segment_tree(arr, mid + 1, end)

            total_sum = left_child.total + right_child.total

            root = Node(start, end, total_sum)
            root.left = left_child
            root.right = right_child
            return root

        self.root = build_segment_tree(self.nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:

        def Update(node, idx, val):

            if node.start == node.end == idx:
                node.total = val

                return node.total

            mid = (node.start + node.end) // 2

            if (idx <= mid):

                left_sum = Update(node.left, idx, val)
                right_sum = node.right.total

            else:

                left_sum = node.left.total
                right_sum = Update(node.right, idx, val)

            node.total = left_sum + right_sum

            return node.total

        Update(self.root, index, val)
        return None

    def sumRange(self, left: int, right: int) -> int:

        def query(node, L, R):

            if node.end < L or node.start > R:
                return 0

            if L <= node.start and node.end <= R:
                return node.total

            return query(node.left, L, R) + query(node.right, L, R)

        return query(self.root, left, right)
