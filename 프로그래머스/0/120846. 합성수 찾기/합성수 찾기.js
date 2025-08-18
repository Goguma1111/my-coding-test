function solution(n) { // 합성수 찾기
    let answer = 0;
    let count =0
    for(let i=0;i<=n;i++){
        count=0
        for(let j=1;j<=i;j++){
            if(i%j===0){
                count++
            }
        }
        if(3<=count) answer++
    }
    return answer;
}

console.log(solution(10))
console.log(solution(15))