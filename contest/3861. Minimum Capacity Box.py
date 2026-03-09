"""
You are given an integer array capacity, where capacity[i] represents the capacity of the ith box, and an integer itemSize representing the size of an item.

The ith box can store the item if capacity[i] >= itemSize.

Return an integer denoting the index of the box with the minimum capacity that can store the item. If multiple such boxes exist, return the smallest index.

If no box can store the item, return -1.

"""


class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        idx = -1
        val = float("inf")

        for i in range(len(capacity)):

            if capacity[i] >= itemSize and capacity[i] < val and capacity[i] >= itemSize:
                val = capacity[i]
                idx = i

        return (idx)