"""

1. Find how many 5
2. Find how many 25
3. No. of 5 = n / 5 + n / 25 + n / 125 ……

Runtime: 52 ms, faster than 24.46% of Python3 online submissions for Factorial Trailing Zeroes.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Factorial Trailing Zeroes.

"""

def trailingZeroes(self, n: int) -> int:
    cnt_five = 0

    while n > 0:
        cnt_five += int(n / 5)
        n /= 5

    return cnt_five
