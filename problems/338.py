'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

class Solution(object):

    def ten2two(self, ten):
        rev_two = list()
        while(ten > 0):
            rev_two.append(ten % 2)
            ten /= 2
        return rev_two

    def countBits(self, num):
        ret = list()
        num_rev_two = self.ten2two(num)

        for t in range(num+1):
            ret.append(sum(num_rev_two))
            for i in range( len(num_rev_two) ):
                if num_rev_two[i] == 0:
                    num_rev_two[i] = 1
                else:
                    num_rev_two[i] = 0
                    break

        return reversed(ret)
