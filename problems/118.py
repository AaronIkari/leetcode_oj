'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        ret = list()

        for r in range(numRows):
            row_len = r+1
            row = [0]*row_len
            for c in range(0, row_len):
                if c == 0 or c == row_len - 1:
                    row[c] = 1
                else:
                    row[c] = ret[r-1][c-1] + ret[r-1][c]

            ret.append(row)
        return ret
