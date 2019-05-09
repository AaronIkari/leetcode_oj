'''
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)
Return the number of moves required to make every node have exactly one coin.

Example 1:
Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.

Example 3:
Input: [1,0,2]
Output: 2

Example 4:
Input: [1,0,0,null,3]
Output: 4


Note:
1<= N <= 100
0 <= node.val <= N
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.total_move = 0


    def DFS(self, root):

        # leaf node
        if not root:
            return 0

        # var declare
        left_lack = 0
        right_lack = 0

        # DFS call, left child, move left-child if > 0
        if root.left:
            left_lack = self.DFS(root.left)
            self.total_move += left_lack if left_lack > 0 else 0

        # DFS call, right child, move right-child if > 0
        if root.right:
            right_lack = self.DFS(root.right)
            self.total_move += right_lack if right_lack > 0 else 0

        # move parent if > 0
        self.total_move += (root.val - 1 - left_lack - right_lack) if (root.val - 1 - left_lack - right_lack) > 0 else 0


        # require from parent
        return (1 - root.val) + left_lack + right_lack

    def distributeCoins(self, root):
        self.DFS(root)
        return self.total_move
