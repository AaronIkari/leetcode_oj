'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):

        part1 = list()
        part2 = list()
        while head != None:
            if head.val < x:
                part1.append(head.val)
            else: # head.val >= x
                part2.append(head.val)
            head = head.next
        ret = part1 + part2

        if_tail = True
        post = None

        for val in reversed(ret):
            ln = ListNode(val)
            if if_tail:
                if_tail = False
                ln.next = None
            else:
                ln.next = post
            post = ln

        ret_head = post

        return ret_head
