'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''

class Solution(object):

    def canJump(self, nums):
        # boundry condition
        if len(nums) == 1: return True

        max_cover = 0
        cur = 0

        while cur <= max_cover:
            tmp_cover = cur + nums[cur]
            if tmp_cover > max_cover:
                max_cover = tmp_cover
            if max_cover >= len(nums) - 1:
                return True
            cur += 1

        return False
