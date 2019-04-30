'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):

    def generater(self, pair, nl, nr):
        if nl == nr == 0:
            self.ret.append(pair)
            return
        else:
            if nl > 0 :
                self.generater(pair+'(', nl-1, nr+1)
            if nr > 0 :
                self.generater(pair+')', nl, nr-1)

    def generateParenthesis(self, n):
        self.ret = list()
        self.generater('', n, 0)
        return self.ret
