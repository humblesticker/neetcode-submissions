class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        at, bt, ct = target
        flag = 0

        for a, b, c in triplets:
            if a > at or b > bt or c > ct: continue
            if a == at: flag |= 1
            if b == bt: flag |= 2
            if c == ct: flag |= 4

        return flag == 7
        
"""
filter out triplet a > at or b > bt or c > ct
as long as you can find at, bt, ct you are good 

O(N)

triplet, flag
(2,5,6), skip
(1,4,4), 0
(5,7,5), skip


"""