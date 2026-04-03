"""
You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.
"""
head = [0,1,2,3];nums = [0,1,3]
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


h = ListNode(head[0])
temp = h

for i in range(1,len(head)):

    n = ListNode(head[i])

    temp.next = n
    temp = n
res = 0
s = set(nums)
while h:

    if h.val in s and (h.next is None or h.next.val not in s):

        res += 1

    h = h.next

print(res)


