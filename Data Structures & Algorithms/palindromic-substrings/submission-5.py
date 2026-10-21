class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        palindrome = [ [0 for _ in range(N)] for _ in range(N) ]

        def ispal(i: int, j: int) -> bool:
            if s[i] != s[j]: return False

            i, j = i+1, j-1
            return i >= j or palindrome[i][j] == 1

        count = 0
        for w in range(N):
            for i in range(N-w): 
                if ispal(i, i+w): 
                    palindrome[i][i+w] = 1
                    count += 1

        return count

"""
dp? 
aaa(6) + b -> 7 min 1+
aaa(6) + a -> 10
aba(3) + b -> 5 

aa(3) + a -> 6

abab + b
"""