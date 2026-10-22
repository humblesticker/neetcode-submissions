class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        p1, p2 = [ False ] * N, [ False ] * N

        count = 0
        for j in range(N):
            p1, p2 = p2, p1 # swap to use p1 as cur and p2 and next
            for i in range(j+1): 
                if s[i] == s[j] and (j-i <= 1 or p1[i+1]): 
                    p2[i] = True
                    count += 1
                else: p2[i] = False

        return count

"""
fdsklf
i,j,p1,p2
0,0,[F],[T]
0,1,[T],[F]
1,1,[T,F],[F,T]
0,2,[F,T],[F,F]
1,2,[F,T],[F,F]
2,2,[F,T,F],[F,F,T]


aaa(6) + b -> 7 min 1+
aaa(6) + a -> 10
aba(3) + b -> 5 

list of N, at pos j
previous items indicates substring (start, i) is palindrome
"""