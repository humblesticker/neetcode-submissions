class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        ispal = [ False ] * N
        longest, result = 0, ""

        for i in range(N):
            for pos in range(i+1):
                # single or empy char between pos and i is palindrom
                if s[pos] == s[i] and (i - pos <= 2 or ispal[pos+1]): 
                    ispal[pos] = True 
                    if i-pos+1 > longest:
                        longest = i-pos+1
                        result = s[pos:i+1]
                        
                else: ispal[pos] = False
                    
        return result

"""
BF: all pairs and scan N^3
is it possible to avoid repeated check of substring? STUCK!

1. pal
2. track long


CHECK!
ababd
i, pal, long
0, [T], 1
1, [F,T], 1
2, [T,F,T], 3
3, [F,T,F,T], 3
4, [F,F,F,F,T], 3 

at i, check all substrings N^2 (AHA!)
at 3

a(ba)b
b(a)b
ab

track sub(pos) is pal or not for previous step, N resource
"""