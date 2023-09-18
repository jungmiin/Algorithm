# 왼쪽 방향으로 간 적 없다면 좌회전해서 전진
# 만약 인도거나 이미 방문했다면, 다시 좌회전
# 4방향 모두 확인했는데 전진하지 못했다면, 현재 방향을 유지한채로 후진 (만약 그 뒤가 인도라면 작동 멈추기)
# 위의 과정 다시 반복
# 북, 동, 남, 서

n, m = map(int, input().split())
x, y, d = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
tmp_coord = [x, y]
tmp_direction = d
road[x][y] = 2
cnt = 0
while True:
    r, c = tmp_coord
    tmp_direction = (tmp_direction-1)%4
    nr, nc = r+dr[tmp_direction], c+dc[tmp_direction]
    if 0 <= nr < n and 0 <= nc < m:
        if road[nr][nc] == 0:
            cnt = 0
            tmp_coord = [nr, nc]
            road[nr][nc] = 2
        elif cnt < 3:
            cnt += 1
        elif cnt == 3:
            nr, nc = r-dr[tmp_direction], c-dc[tmp_direction]
            if road[nr][nc] == 1:
                break
            else:
                tmp_coord = [nr, nc]
                cnt = 0
answer = 0
for r in range(n):
    for c in range(m):
        if road[r][c] == 2:
            answer += 1
print(answer)
