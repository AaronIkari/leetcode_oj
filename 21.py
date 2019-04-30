'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(-1)

        while l1 and l2:
            if l1.val > l2.val:
                nn = ListNode(l2.val)
                l2 = l2.next
            else:
                nn = ListNode(l1.val)
                l1 = l1.next

            cur.next = nn
            cur = cur.next

        cur.next = l1 or l2

        return dummy.next
