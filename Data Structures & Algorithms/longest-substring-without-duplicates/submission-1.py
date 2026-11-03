class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest, L = 0, len(s)
        start = -1

        for i in range(L):
            seen.add(s[i])

            # update longest and start 
            if i+1 >= L or s[i+1] in seen:
                longest = max(longest, i-start)
                while i+1 < L:
                    start += 1
                    seen.remove(s[start])
                    if s[start] == s[i+1]: break # 

        return longest
        
"""
abcade -> 5
i, seen, longest, start
0, a, 0, -1
1, ab
2, bc, 3, 1
3, bca, 
4, bcad, 
5, bcade, 5, 


"""