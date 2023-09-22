from itertools import combinations, permutations
import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    permus = sorted(list(set(permutations(numbers, M))))
    for permu in permus:
        print(' '.join(list(map(str, permu))))

for _ in range(TEST_CASE):
    solution()