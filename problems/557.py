'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''

class Solution(object):
    def reverseWords(self, s):
        s_splits = s.split()
        rev_s_splits = list()

        for s_split in s_splits:
            rev_s_splits.append(s_split[::-1])

        ret = ' '.join(rev_s_splits)
        return ret
