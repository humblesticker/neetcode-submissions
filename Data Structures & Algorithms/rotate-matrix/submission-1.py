class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for i in range(N//2):
            for j in range(i, N-1-i):
                ni, nj = j, N-1-i
                prev = matrix[i][j]

                for _ in range(4): # last one is already swapped
                    temp = matrix[ni][nj]
                    matrix[ni][nj] = prev
                    prev = temp
                    ni, nj = nj, N-1-ni
        
"""
BF
in-place

test
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

4
i, j
0, 0
    ni, nj, swap
    0, 3, (4, 1)
    3, 3, (16, 4)
    3, 0, (13, 16)
0, 1
    1, 3, (8, 2)
    3, 2, (15, 8)
    2, 0, (9, 15)

1, 1
    1, 2, (7, 6)
    2, 2, (11, 7)
    2, 1, (10, 11)





1: ok
2: 
i, j
0, 0
ni, nj, swap
0, 1, (2, 1)
1, 1, (4, 2)
1, 0, (3, 4) ok


i, j -> j, N-1-i -> N-1-i, N-1-j -> N-1-j, i -> i, j


i, j
0, 0
1, 1
until i, j != j, N-1-i

steps 
1. one cell [x]
2. one row [x]
3. 2 rows 


 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
"""