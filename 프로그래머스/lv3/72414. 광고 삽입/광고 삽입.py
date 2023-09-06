def time_to_sec(time):
    hour, minute, second = map(int, time.split(':'))
    return hour*3600 + minute*60 + second

def sec_to_time(sec):
    hour = sec//3600
    minute = (sec-hour*3600)//60
    second = sec-(hour*3600+minute*60)
    return str(hour).zfill(2)+":"+str(minute).zfill(2)+":"+str(second).zfill(2)

def solution(play_time, adv_time, logs):
    answer = ''
    adv_sec = time_to_sec(adv_time)
    play_sec = time_to_sec(play_time)
    dp = [0] * (play_sec+1)
    logs = sorted(logs)
    for log in logs:
        start_sec, end_sec = map(time_to_sec, log.split("-"))
        dp[start_sec] += 1
        dp[end_sec] -= 1 
    for i in range(1, play_sec+1):
        dp[i] += dp[i-1]
    time, max_time, max_start = 0, 0, 0
    for i in range(adv_sec+1):
        time += dp[i]
    max_time = time
    for cur_start in range(play_sec-adv_sec):
        time = time - dp[cur_start] + dp[cur_start+adv_sec]
        if time > max_time:
            max_time = time
            max_start = cur_start+1
    return sec_to_time(max_start)