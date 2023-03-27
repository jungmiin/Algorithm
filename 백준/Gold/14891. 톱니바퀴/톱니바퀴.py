# 톱니바퀴 2023/3/23 12:08 -

# [0][2] - [2][-2] / [1][2] - [2][-2] / [2][2] - [3][-2] 
# 이렇게 마주보고 있음
# rotate를 돌면서 위의 경우 확인 
# 몇번째 톱니바퀴가 회전하는지 확인하는게 중요할 것 같음 
# 0 -> 1 -> 2 -> 3
# 1 -> 0 -> 2 -> 3
# 2 -> 1 -> 0 -> 3
# 3 -> 2 -> 1 -> 0

# 이거를 case로 나눠서 확인한 다음 돌리기 
# 돌리는 방법은 원형큐

import sys
from collections import deque

input = sys.stdin.readline

wheel = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
K = int(input().rstrip())
rotate_list = [list(map(int, input().split())) for _ in range(K)]

# print(wheel, wheel[1][0])

# 회전시키기
for wheel_num, direction in rotate_list:
    tmp_wheel = []
    wheel_num = wheel_num -1 

    for i in range(4):
        tmp_wheel.append((wheel[i][6], wheel[i][2]))

    wheel[wheel_num].rotate(direction)
    

    if wheel_num != 0:
        for i in range(wheel_num, 0, -1):
            left, right = tmp_wheel[i-1][1], tmp_wheel[i][0]
            if left != right:
                if (wheel_num - (i-1)) % 2 == 0:
                    wheel[i-1].rotate(direction)
                else :
                    wheel[i-1].rotate(-1 * direction)
            else : 
                break

    if wheel_num != 3:
        for i in range(wheel_num, 3) :
            left, right = tmp_wheel[i][1], tmp_wheel[i+1][0]
            if left != right:
                if ((i+1) - wheel_num) % 2 == 0:
                    wheel[i+1].rotate(direction)
                else :
                    wheel[i+1].rotate(-1 * direction)
            else :
                break

# 점수 매기기
score = 0
for i in range(4):
    if wheel[i][0] == 1:
        score += pow(2, i)

print(score)
