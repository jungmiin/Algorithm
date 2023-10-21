const compareNumber = (a, b) => a[1] - b[1]
function solution(routes) {
    let answer = 0;
    let lastCamera = -1;
    const newRoutes = routes.map(route => [route[0]+30000, route[1]+30000]).sort(compareNumber)
    for (let i = 0; i < newRoutes.length; i++) {
        const [start, end] = newRoutes[i]
        if (start > lastCamera || end < lastCamera) {
            answer += 1
            lastCamera = end
        }
    }
    return answer;
}