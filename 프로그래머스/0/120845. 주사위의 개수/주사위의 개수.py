def solution(box, n):
    answer = 1

    for i in box :
        answer *= i // n 

    return answer


print(solution([1, 1, 1],1))