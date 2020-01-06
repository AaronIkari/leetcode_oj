'''
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x, next):
         self.val = x
         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        lst = list()
        while head != None:
            lst.append(head.val)
            head = head.next

        l, r = 0, len(lst) - 1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1

        return True
