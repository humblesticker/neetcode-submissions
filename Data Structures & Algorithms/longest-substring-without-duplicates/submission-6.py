class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start, longest, L = -1, 0, len(s)

        for i in range(L):
            seen[s[i]] = i
            if i+1 < L and s[i+1] not in seen: continue

            # next char is dup or ooi
            # update longest and start 
            longest = max(longest, i-start)
            if i+1 >= L: continue

            while True:
                start += 1
                del seen[s[start]]
                # dup is just removed and start points to the prev dup
                if s[start] == s[i+1]: break 
                
        return longest
        
"""
optimize
if same char in a row reset
you can track pos and create new set in between
"""