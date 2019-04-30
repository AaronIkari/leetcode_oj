'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''

class Solution(object):

    def dp(self, pos, step):
        # terminal state
        if pos+step >= len(self.cost):
            return 0

        # visit before
        if (pos,step) in self.vis:
            return self.rcd[pos][step]

        # dp call
        else:
            # memorize
            self.rcd[pos][step] = self.cost[pos+step] + min( self.dp(pos+step, 1), self.dp(pos+step, 2) )
            self.vis.add( (pos,step) )
            return self.rcd[pos][step]

    def minCostClimbingStairs(self, cost):
        self.vis = set()
        self.rcd = [[0, 0, 0] for _ in range( len(cost) )]
        self.cost = cost

        return min( cost[0] + self.dp(0, 1),
                    cost[0] + self.dp(0, 2),
                    cost[1] + self.dp(1, 1),
                    cost[1] + self.dp(1, 2) )
