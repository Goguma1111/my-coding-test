function solution(angle) { // 각도기
    let answer = 0;

    if (0 < angle && angle < 90) {
        return answer = 1;
    } else if (angle == 90) {
        return answer = 2;
    } else if (90 < angle && angle < 180) {
        return answer = 3;
    } else  {
        return answer = 4;
    }
}


console.log(solution(70));