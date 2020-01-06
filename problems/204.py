'''
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4

Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        # primes table
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(math.sqrt(n))+1):
            for j in range(i*2, n, i):
                primes[j] = False

        return primes.count(True)
