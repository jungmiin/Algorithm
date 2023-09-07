def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x: x[1])
    camera = -30001
    for s, e in routes:
        if not s <= camera <= e:
            answer += 1
            camera = e
        # checkable = False
        # for camera in cameras:
        #     if s <= camera[0] <= e or s <= camera[1] <= e:
        #         checkable = True
        # if not checkable:
        #     cameras.append((s, e))
    print(routes, camera)
    return answer