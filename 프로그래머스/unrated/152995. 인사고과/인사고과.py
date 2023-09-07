def solution(scores):
    wanho, scores = scores[0], scores[1:]
    rank = 1
    tmp_eval = 0
    # print(sorted(scores, key=lambda x : -sum(x)))
    for attitude, evaluation in sorted(scores, key=lambda x : (-x[0], x[1])):
        if wanho[0] < attitude and wanho[1] < evaluation:
            return -1
        if tmp_eval <= evaluation:
            tmp_eval = evaluation
            if wanho[0] + wanho[1] < attitude + evaluation:
                rank += 1
    return rank