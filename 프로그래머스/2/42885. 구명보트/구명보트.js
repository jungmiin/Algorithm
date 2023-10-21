const compareNumber = (a, b) => a-b

function solution(people, limit) {
    let answer = 0;
    people.sort(compareNumber)
    let start = 0
    let end = people.length-1
    while (start <= end) {
        if (people[start]+people[end] <= limit) {
            start++
        }
        end--
        answer++
    }
    return answer;
}