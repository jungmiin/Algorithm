import sys
from collections import defaultdict
import bisect
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    T = int(input().rstrip())
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    M = int(input().rstrip())
    B = list(map(int, input().split()))
    array_a, array_b = [], []
    for i in range(N):
        array_a.append(A[i])
        for j in range(i+1, N):
            array_a.append(array_a[-1]+A[j])
    for i in range(M):
        array_b.append(B[i])
        for j in range(i+1, M):
            array_b.append(array_b[-1]+B[j])
    array_a.sort()
    array_b.sort()
    answer = 0
    for a in range(len(array_a)):
        right = bisect.bisect_right(array_b, T-array_a[a])
        left = bisect.bisect_left(array_b, T-array_a[a])
        answer += right-left
    print(answer)

for _ in range(TEST_CASE):
    solution()