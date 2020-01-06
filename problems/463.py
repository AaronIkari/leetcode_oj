'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

class Solution(object):

    def __init__(self):
        self.num_island = 0
        self.num_intercept = 0
        self.vis = set()


    def dfs(self, grid, i, j, m, n):

        self.vis.add((i,j))
        self.num_island += 1


        if i+1 < m and grid[i+1][j] == 1:
            self.num_intercept += 1
            if (i+1, j) not in self.vis:
                self.dfs(grid, i+1, j, m, n)
        if i-1 >= 0 and grid[i-1][j] == 1:
            self.num_intercept += 1
            if (i-1, j) not in self.vis:
                self.dfs(grid, i-1, j, m, n)
        if j+1 < n and grid[i][j+1] == 1:
            self.num_intercept += 1
            if (i, j+1) not in self.vis:
                self.dfs(grid, i, j+1, m, n)
        if j-1 >= 0 and grid[i][j-1] == 1:
            self.num_intercept += 1
            if (i, j-1) not in self.vis:
                self.dfs(grid, i, j-1, m, n)


    def islandPerimeter(self, grid):

        m, n = len(grid), len(grid[0])

        s_i, s_j = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    s_i, s_j = i, j

        self.dfs(grid, s_i, s_j, m, n)


        return self.num_island*4-self.num_intercept
