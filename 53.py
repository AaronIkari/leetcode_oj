'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

# Reference: https://www.youtube.com/watch?v=86CQq3pKSUw

class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return None
        max_cur = max_global = nums[0]
        for i in range(1, len(nums)):
            max_cur = max(max_cur + nums[i], nums[i])
            if max_cur > max_global:
                max_global = max_cur

        return max_global
