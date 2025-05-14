function solution(numer1, denom1, numer2, denom2) { // 분수의 덧셈
    let answer = []
    let numer = (numer1 * denom2) + (numer2 * denom1);
    let denom =  denom1 * denom2;
    const gcd = (numer, denom) => (numer % denom === 0 ? denom : gcd(denom, numer % denom))

    answer[0] = numer / gcd(numer, denom);
    answer[1] = denom / gcd(numer, denom);

    return answer;
}

console.log(solution(1,2,3,4));
console.log(solution(9,2,1,3));