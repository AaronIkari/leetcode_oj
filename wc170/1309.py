'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follow:

1. Characters ('a' to 'i') are represented by ('1' to '9') respectively.
2. Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
3. Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Example 1:
Input: s = "10#11#12"
Output: "jkab"

Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"

Example 3:
Input: s = "25#"
Output: "y"

Example 4:
Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
 
Constraints:
1. 1 <= s.length <= 1000
2. s[i] only contains digits letters ('0'-'9') and '#' letter.
3. s will be valid string such that mapping is always possible.
'''


class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        ret = ''

        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i + 2] == '#':
                ret += chr(ord('j') + int(s[i:i+2]) - 10)
                i += 3

            else:
                ret += chr(ord('a') + int(s[i]) - 1)
                i += 1

        return ret
