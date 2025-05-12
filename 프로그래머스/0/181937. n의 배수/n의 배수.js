function solution(num, n) { // n의 배수
    let answer = num % n == 0 ? 1:0;
    return answer;
}

console.log(solution(98,2));
console.log(solution(34,3));
