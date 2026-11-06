class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ranges, maxh, minh = {}, heights[0], heights[0]
        for pos, h in enumerate(heights):
            if h not in ranges: ranges[h] = (pos, pos)
            else: 
                i, j = ranges[h]
                ranges[h] = (min(i, pos), max(j, pos))

            maxh, minh = max(maxh, h), min(minh, h)
            

        left, right = ranges[maxh]
        most = maxh * (right - left)

        for h in range(maxh-1, minh-1, -1):
            # skip if h is not in ranges
            if h not in ranges: continue
            
            # merge range 
            i, j = ranges[h]
            left, right = min(left, i), max(right, j)

            # update most
            most = max(most, h * (right - left))

        return most

"""
h, range, A
7, (1, 5), 28
6, (1, 7), 36
5, inside -> smaller
4, same
3, same
2, same
1, (0, 7), 7

O(N) to build h: range
O(H) to process and track max maxh to minh
O(N)
"""