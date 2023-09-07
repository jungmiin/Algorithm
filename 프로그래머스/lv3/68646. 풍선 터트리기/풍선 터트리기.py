def solution(a):
    right = 0
    left = 0
    index = a.index(min(a))
    left_min = a[0]
    right_min = a[-1]
    for i in range(1, index+1):
        if i == 1:
            left = 1
        if left_min > a[i]:
            left_min = a[i]
            left += 1
    for i in range(-1, index-len(a), -1):
        if i == -1:
            right = 1
        if right_min > a[i]:
            right_min = a[i]
            right += 1
    # print(right, left)
    return right + left 