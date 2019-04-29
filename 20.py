'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

class Solution(object):
    def isValid(self, s):
        parentheses = {
            '(': 1,
            ')': -1,
            '{': 2,
            '}': -2,
            '[': 3,
            ']': -3
        }
        stack = list()
        for s_i in s:
            # either ')', '}', or ']'
            if parentheses[s_i] < 0:
                # stack is empty "or" mismatch
                if not stack or stack[-1] + parentheses[s_i] != 0:
                    return False
                else:
                    del stack[-1]
            # either '(', '{', or '['
            else:
                stack.append(parentheses[s_i])

        if not stack:
            return True
        else:
            return False
