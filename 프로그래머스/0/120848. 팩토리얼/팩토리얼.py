def solution(n):
    answer = 0           #정답 후보를 저장할 변수

    for i in range(1, n+1) :
        fact = 1

        for j in range(2, i+1) :
            fact *= j

        if fact <= n:
            answer = i

        else:
            break;
        
    return answer

print(solution(7)) 