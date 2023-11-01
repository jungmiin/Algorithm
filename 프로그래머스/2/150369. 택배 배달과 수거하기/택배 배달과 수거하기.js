function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    let [d, p] = [0, 0];
    for (let i of Array.from(Array(n), (_, index) => n-index-1)) {
        [d, p] = [d+deliveries[i], p+pickups[i]]
        while (d > 0 || p > 0) {
            [d, p] = [d-cap, p-cap]
            answer += (i+1)*2
        }
    }
    return answer;
}