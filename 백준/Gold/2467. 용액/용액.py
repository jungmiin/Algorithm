import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    N = int(input().rstrip())
    numbers = list(map(int, input().split()))
    cur = [0, N-1]
    min_value = numbers[0]+numbers[N-1]
    min_cur = [0, N-1]
    while cur[0] < cur[1]:
        start, end = cur
        tmp_value = numbers[start]+numbers[end]
        if tmp_value > 0:
            cur[1] -= 1
        elif tmp_value < 0:
            cur[0] += 1
        else:
            min_cur = [start, end]
            break
        if abs(min_value) > abs(tmp_value):
            min_cur = [start, end]
            min_value = tmp_value
    print(numbers[min_cur[0]], numbers[min_cur[1]])

for _ in range(TEST_CASE):
    solution()