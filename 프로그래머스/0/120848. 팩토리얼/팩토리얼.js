function solution(n) { // 팩토리얼
    let answer = 1;
    let a = 0;
    while (answer <= n) {
        a++;
        answer *= a;
    }
    return a-1;
}
3628800
console.log(solution(7));