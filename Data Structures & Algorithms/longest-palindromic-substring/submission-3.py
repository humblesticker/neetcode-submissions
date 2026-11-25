class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        left, right = 0, 0

        def check(l, r):
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1

            # previous valid
            l += 1
            r -= 1
            if r - l > right - left: return l, r
            else: return left, right

        for i in range(N):
            left, right = check(i, i)
            if i+1 < N: left, right = check(i, i+1)
        
        return s[left:right+1]
        

"""
ababd
i, (l,r), (left, right)
0, (0,0), (0,0) 
1, (0,2), (0,2)
2, (1,3)
3, (3,3)
4, (4,4)
"""