import sys
from collections import Counter
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    r, c, target = map(int, input().split())
    array = [[0]*100 for _ in range(100)]
    answer = -1
    W, H = 3, 3
    for i in range(3):
        x, y, z = map(int, input().split())
        array[i][0], array[i][1], array[i][2] = x, y, z
    for sec in range(101):
        if array[r-1][c-1] == target:
            answer = sec
            break
        if W <= H: # R 연산
            for h in range(H):
                row = array[h]
                counter = Counter(row)
                del counter[0]
                result = sum(sorted([[i, j] for i, j in counter.items()], key=lambda x: (x[1], x[0])), [])
                tmp_w = min(len(result), 100)
                W = max(W, tmp_w)
                new_array = [0]*100
                for w in range(tmp_w):
                    new_array[w] = result[w]
                array[h] = new_array
        else: # C 연산
            for w in range(W):
                column = [array[i][w] for i in range(len(array))]
                counter = Counter(column)
                del counter[0]
                result = sum(sorted([[i, j] for i, j in counter.items()], key=lambda x: (x[1], x[0])), [])
                tmp_h = min(len(result), 100)
                H = max(H, tmp_h)
                new_array = [0]*100
                for h in range(tmp_h):
                    new_array[h] = result[h]
                for k in range(len(array[0])):
                    array[k][w] = new_array[k]
    print(answer)


for _ in range(TEST_CASE):
    solution()