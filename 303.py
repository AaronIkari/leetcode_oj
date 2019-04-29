'''
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''

class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.sum_arr = []

        cur_sum = 0
        for i in range( len(nums) ):
            cur_sum += nums[i]
            self.sum_arr.append(cur_sum)

    def sumRange(self, i, j):
        return self.sum_arr[j] - self.sum_arr[i] + self.nums[i]

    def run(self, i, j):
        print '{}'.format( self.sumRange(i, j) )


num_array = NumArray([-2,0,3,-5,2,-1])
num_array.run(0,2)
num_array.run(2,5)
num_array.run(0,5)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
