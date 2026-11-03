class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = res = 0
        t = 0
        while r < len(s) and t < 50:
            t+=1
            count = 0
            seen = dict()
            while r < len(s) and s[r] not in seen:
                seen[s[r]] = r
                r += 1
                count += 1
            if r < len(s):
                l = r = seen[s[r]] + 1
            res = max(res, count)
        return res

        # res = 0
        # for i in range(len(s)):
        #     curr_res = 0
        #     seen = set()
        #     for j in range(i + 1, len(s)):
        #         if s[j] in seen:
        #             res = max(res, curr_res)
        #         else:
        #             seen.add(s[j])
        #             curr_res += 1
        # return res
                