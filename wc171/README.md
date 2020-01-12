# Leetcode Weekly Contest 171

## Tags:
###### tags: `leetcode`, `wc171`

## Overview
| Problems | Language  | Status |  Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: |
| [1317. Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/contest/weekly-contest-171/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) | Python 3.4.3 | <span style="color:green">AC</span> |  32 ms |  12.6 MB |
| [1318. Minimum Flips to Make a OR b Equal to c](https://leetcode.com/contest/weekly-contest-171/problems/minimum-flips-to-make-a-or-b-equal-to-c/) | Python 3.4.3 | <span style="color:green">AC</span> |  24 ms |  12.8 MB |
| [5309. Number of Operations to Make Network Connected](https://leetcode.com/contest/weekly-contest-171/problems/number-of-operations-to-make-network-connected/) | Python 3.4.3 | <span style="color:green">AC^</span> |  532 ms | 44.1 MB |
| [1320. Minimum Distance to Type a Word Using Two Fingers](https://leetcode.com/contest/weekly-contest-171/problems/minimum-distance-to-type-a-word-using-two-fingers/) | ? | ? | ? ms |  ? MB |


## Solutions
### 1317. Convert Integer to the Sum of Two No-Zero Integers
```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zero(k):        
            while k > 0:
                if k%10 == 0:
                    return True
                k //= 10

            return False

        A = 1
        B = n - A

        while has_zero(A) or has_zero(B):
            A += 1
            B -= 1

        return [A, B]
```

### 1318. Minimum Flips to Make a OR b Equal to c
```python
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ret = 0
        while a or b or c:
            ba, bb, bc = a%2, b%2, c%2
            a //= 2
            b //= 2
            c //= 2

            if bc == 0:
                ret += (ba+bb)
            else: # bc == 1
                if ba == bb == 0:
                    ret += 1

        return ret
```
### 5309. Number of Operations to Make Network Connected
```python
class Solution:
    def dfs(self, nd, conn, vis):
        vis[nd] = True
        if nd in conn:
            for nb in conn[nd]:
                if not vis[nb]:
                    self.dfs(nb, conn, vis)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n-1:
            return -1

        vis = [False for _ in range(n)]
        conn = dict()

        for n1,n2 in connections:
            if n1 not in conn:
                conn[n1] = list()
            conn[n1].append(n2)
            if n2 not in conn:
                conn[n2] = list()
            conn[n2].append(n1)

        # num of connected conponent
        ret = 0
        for nd in range(n):
            if not vis[nd]:
                self.dfs(nd, conn, vis)
                ret += 1

        return ret-1
```
