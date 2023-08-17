costs = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3]
        ,[7, 1, 2, 4, 2, 3, 5, 4, 5, 6]
        ,[6, 2, 1, 2, 3, 2, 3, 5, 4, 5]
        ,[7, 4, 2, 1, 5, 3, 2, 6, 5, 4]
        ,[5, 2, 3, 5, 1, 2, 4, 2, 3, 5]
        ,[4, 3, 2, 3, 2, 1, 2, 3, 2, 3]
        ,[5, 5, 3, 2, 4, 2, 1, 5, 3, 2]
        ,[3, 4, 5, 6, 2, 3, 5, 1, 2, 4]
        ,[2, 5, 4, 5, 3, 2, 3, 2, 1, 2]
        ,[3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]

def num_to_coord(start, dest):
    sx = (start-1) // 3 if start != 0 else 3
    sy = (start-1) % 3 if start != 0 else 1
    dx = (dest-1) // 3 if dest != 0 else 3
    dy = (dest-1) % 3 if dest != 0 else 1
    return [(sx, sy), (dx, dy)]

def calculate(start, dest):
    (sr, sc), (dr, dc) = num_to_coord(start, dest)
    if sr == dr: return abs(sc-dc) * 2
    if sc == dc: return abs(sr-dr) * 2
    return abs(sr-dr) * 2 + abs(sc-dc) * 2 -1

def solution(numbers):
    answer = 0
    INF = int(1e9)
    dp = {}
    pos = (4, 6)
    dp[pos] = 0
    
    for number in numbers:
        num = int(number)
        cur = {}
        for pos, cost in dp.items():
            left, right = pos
            if right == num:
                if not (left, num) in cur.keys() or cur[(left, num)] > cost + 1:
                    cur[(left, num)] = cost + 1
            elif left == num:
                if not (num, right) in cur.keys() or cur[(num, right)] > cost +1:
                    cur[(num, right)] = cost + 1
            else:
                # right_cost = calculate(right, num)
                # left_cost = calculate(left, num)
                right_cost = costs[right][num]
                left_cost = costs[left][num]
                if not (left, num) in cur.keys() or cur[(left, num)] > cost + right_cost:
                    cur[(left, num)] = cost + right_cost
                if not (num, right) in cur.keys() or cur[(num, right)] > cost + left_cost:
                    cur[(num, right)] = cost + left_cost
        dp = cur
        
    return min(list(dp.values()))