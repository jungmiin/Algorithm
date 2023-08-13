def solution(m, n, startX, startY, balls):
    answer = []
    for endX, endY in balls:
        k = float("inf")
        # print(startX, startY, endX, endY)
        if startX!=endX or endY>startY:
            k = min(k, (startX-endX)**2+(startY+endY)**2)
            # print("1", k, (startX-endX)**2, (startY+endY)**2)
        if startY!=endY or endX>startX:
            k = min(k, (startX+endX)**2+(startY-endY)**2)
            # print("2", k, (startX+endX)**2, (startY-endY)**2)
        if startX!=endX or endY<startY:
            k = min(k, (startX-endX)**2+(2*n-endY-startY)**2)
            # print("3", k, (startX-endX)**2, (2*n-endY-startY)**2)
        if startY!=endY or endX<startX:
            k = min(k, (2*m-endX-startX)**2+(startY-endY)**2)
            # print("4", k, (2*m-endX-startX)**2, (startY-endY)**2)
        answer.append(k)
    return answer