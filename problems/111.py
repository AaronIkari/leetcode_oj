'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        # empty tree
        if not root:
            return 0
        # only one node
        if not root.left and not root.right:
            return 1

        # left subtree empty
        if not root.left:
            return 1 + self.minDepth(root.right)
        # right subtree empty
        elif not root.right:
            return 1 + self.minDepth(root.left)
        # TreeNode with left and right subtree
        else:
            return 1 + min( self.minDepth(root.left), self.minDepth(root.right))
