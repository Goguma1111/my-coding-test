
function solution(M, N) { // 종이자르기
    let answer = (M-1) + M * (N-1) ;
    return answer;
}

console.log(solution(2,5));
