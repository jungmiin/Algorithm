def solution(commands) :
    answer = []
    graph = [["EMPTY"] * 51 for _ in range(51)]
    merge = [[(i,j) for j in range(51)] for i in range(51)]
    for index, command in enumerate(commands):
        c = command.split(" ")
        if c[0] == "UPDATE":
            if len(c) == 3:
                value1, value2 = c[1:]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if graph[i][j] == value1:
                            graph[i][j] = value2
            elif len(c) == 4:
                r, c, value = c[1:]
                r, c = int(r), int(c)
                x, y = merge[r][c]
                graph[x][y] = value
        elif c[0] == "MERGE":
            r1, c1, r2, c2 = c[1:]
            r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
            if r1 == r2 and c1 == c2:
                continue
            x1, y1 = merge[r1][c1]
            x2, y2 = merge[r2][c2]
            if graph[x1][y1] == "EMPTY":
                graph[x1][y1] = graph[x2][y2]
            for i in range(1, 51):
                for j in range(1, 51):
                    if merge[i][j] == (x2, y2):
                        merge[i][j] = (x1, y1)
        elif c[0] == "UNMERGE":
            r, c = c[1:]
            r, c = int(r), int(c)
            x, y = merge[r][c]
            tmp = graph[x][y]
            for i in range(1, 51):
                for j in range(1, 51):
                    if merge[i][j] == (x,y):
                        merge[i][j] = (i, j)
                        graph[i][j] = "EMPTY"
            graph[r][c] = tmp
        elif c[0] == "PRINT":
            r, c = c[1:]
            r, c = int(r), int(c)
            x, y = merge[r][c]
            answer.append(graph[x][y])
        # print()
        # print("command", index, command)
        # print()
        # for i in range(1, 51):
        #     for j in range(1, 51):
        #         if graph[i][j] != "EMPTY":
        #             print("graph", i, j, graph[i][j])
        #         if merge[i][j] != (i,j):
        #             print("merge", i, j, merge[i][j])
            
    return answer
            