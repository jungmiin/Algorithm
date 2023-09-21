from itertools import combinations
import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    N, M = map(int, input().split())
    combis = list(combinations(range(1, N+1), M))
    for combi in combis:
        for c in combi:
            print(c, end=" ")
        print()

for _ in range(TEST_CASE):
    solution()