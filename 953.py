'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Note:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
'''
class Solution(object):
    def compare_words(self, w1, w2, order):
        w1_l = 0
        w2_l = 0
        while w1_l < len(w1) and w2_l < len(w2):
            pre = order.index(w1[w1_l])
            post = order.index(w2[w2_l])
            if pre > post:
                return False
            elif pre < post:
                return True
            else:
                w1_l += 1
                w2_l += 1
        if w1_l == len(w1) and w2_l <= len(w2):
            return True
        else:
            return False

    def isAlienSorted(self, words, order):
        for i in range(0, len(words)-1):
            if not self.compare_words(words[i], words[i+1], order):
                return False
        return True
