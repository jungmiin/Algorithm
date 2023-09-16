import sys
from copy import deepcopy
from itertools import permutations
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수
INF = int(1e9)

def solution():
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    rcs = [list(map(int, input().split())) for _ in range(K)]
    result = INF
    for p in permutations(rcs, K):
        copy_a = deepcopy(A) 
        for r, c, s in p:
            r -= 1
            c -= 1
            for n in range(s, 0, -1):
                tmp = copy_a[r-n][c+n]
                copy_a[r-n][c-n+1:c+n+1] = copy_a[r-n][c-n:c+n]  
                for row in range(r-n, r+n):  
                    copy_a[row][c-n] = copy_a[row+1][c-n]
                copy_a[r+n][c-n:c+n] = copy_a[r+n][c-n+1:c+n+1]  
                for row in range(r+n, r-n, -1):  
                    copy_a[row][c+n] = copy_a[row-1][c+n]
                copy_a[r-n+1][c+n] = tmp
        for row in copy_a:
            result = min(result, sum(row))
    print(result)

for _ in range(TEST_CASE):
    solution()