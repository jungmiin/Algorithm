from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def pre(Y, answer):
    root = Y[0]
    y1, y2 = [], []
    for y in Y[1:]:
        y1.append(y) if root[0] > y[0] else y2.append(y)
    answer.append(root[2])
    if len(y1) > 0: pre(y1, answer)
    if len(y2) > 0: pre(y2, answer)
    return

def post(Y, answer):
    root = Y[0]
    y1, y2 = [], []
    for y in Y[1:]:
        y1.append(y) if root[0] > y[0] else y2.append(y)
    if len(y1) > 0: post(y1, answer)
    if len(y2) > 0: post(y2, answer)
    answer.append(root[2])
    return

def solution(nodeinfo):
    answer = [[], []]
    for i, info in enumerate(nodeinfo): info.append(i+1)
    Y = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    pre(Y, answer[0])
    post(Y, answer[1])
    return answer
    