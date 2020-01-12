# Leetcode Weekly Contest 170

## Tags:
###### tags: `leetcode`, `wc170`

## Overview
| Problems | Language  | Status |  Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: |
| [1309. - Decrypt String from Alphabet to Integer Mapping](https://leetcode.com/contest/weekly-contest-170/problems/decrypt-string-from-alphabet-to-integer-mapping/) | Python 3.4.3 | <span style="color:green">AC</span> | 28 ms |  12.7 MB |
| [1310. - XOR Queries of a Subarray](https://leetcode.com/contest/weekly-contest-170/submissions/detail/291284051/) | Python 3.4.3 | <span style="color:green">AC</span> | 416 ms |  27.3 MB |
| [1311. - Get Watched Videos by Your Friends](https://leetcode.com/contest/weekly-contest-170/problems/get-watched-videos-by-your-friends/) | Python 3.4.3 | <span style="color:green">AC</span> | -- ms |  -- MB |
| [1312. - Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/contest/weekly-contest-170/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | ? | ? | ? ms |  ? MB |


## Solutions
### 1309. - Decrypt String from Alphabet to Integer Mapping
```python
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

```

### 1310. - XOR Queries of a Subarray

```python
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        ret = list()

        xor_arr = list()
        xor_arr.append(arr[0])

        for i in range(1, len(arr)):
            xor_arr.append( xor_arr[i-1] ^ arr[i])

        for l, r in queries:
            if l == 0:
                ret.append(xor_arr[r])
            else:
                ret.append(xor_arr[l-1] ^ xor_arr[r])

        return ret
```
### 1311. - Get Watched Videos by Your Friends
```python
from collections import defaultdict
from queue import Queue

class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        n = len(friends)
        vis = [False for _ in range(n)]

        cnt = defaultdict(int)

        que = Queue()
        que.put( (id, 0) )
        vis[id] = True

        while not que.empty():
            ni, lev = que.get()
            if lev == level:
                for video in watchedVideos[ni]:
                    cnt[video] += 1
            else:
                for nbr_ni in friends[ni]:
                    if  not vis[nbr_ni]:
                        que.put( (nbr_ni, lev+1))
                        vis[nbr_ni] = True


        ret = sorted(cnt.items(), key=lambda item : (item[1], item[0]))
        ret = [x for (x,y) in ret]

        return ret
```
