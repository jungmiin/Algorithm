from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def solution(board, ir, ic):
    answer = int(1e9)
    def bfs(start, end):
        sr, sc = start
        er, ec = end
        visited = [[False]*4 for _ in range(4)]
        queue = deque()
        queue.append((sr, sc, 0))
        while queue:
            r, c, cost = queue.popleft()
            if visited[r][c]: continue
            visited[r][c] = True
            if r == er and c == ec:
                # print(start, "->", end, "is", cost)
                return cost
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < 4 and 0 <= nc < 4:
                    queue.append((nr, nc, cost+1))
                nr, nc = r, c
                while True:
                    nnr, nnc = nr + dr[i], nc + dc[i]
                    if not (0 <= nnr < 4 and 0 <= nnc < 4):
                        queue.append((nr, nc, cost+1))
                        break
                    if copy_board[nnr][nnc] != 0:
                        queue.append((nnr, nnc, cost+1))
                        break
                    nr, nc = nnr, nnc
        return 
    # 어떤 카드를 먼저 제거할지
    # 카드 두 장중에서도 어떤 카드를 먼저 선택할지
    cards = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards[board[i][j]].append((i, j))
    cases = list(permutations(cards.keys(), len(cards.keys())))
    for case in cases:
        copy_board = deepcopy(board)
        case_cost = 0
        cur = (ir, ic)
        for card in case:
            # 두개의 카드중 어느 것을 먼저 선택할지
            card_0 = bfs(cur, cards[card][0])
            card_1 = bfs(cur, cards[card][1])
            if card_0 < card_1:
                card_0 += bfs(cards[card][0], cards[card][1])
                case_cost += card_0+2
                cur = cards[card][1]
            else:
                card_1 += bfs(cards[card][1], cards[card][0])
                case_cost += card_1+2
                cur = cards[card][0]
            # for i in range(-1, 1):
            #     card_cost[i] += bfs(cur, cards[card][i])
            #     card_cost[i] += bfs(cards[card][i], cards[card][i-1])
            # # 비교
            # if card_cost[0] <= card_cost[1]:
            #     case_cost += card_cost[0] + 2
            #     cur = cards[card][1]
            # else:
            #     case_cost += card_cost[1] + 2
            #     cur = cards[card][0]
            # board 업데이트 
            for r, c in cards[card]:
                copy_board[r][c] = 0
        #     print("--tmp cost--", case_cost, cur, card_cost)
        # print(case, "is", case_cost)
        answer = min(answer, case_cost)
    return answer