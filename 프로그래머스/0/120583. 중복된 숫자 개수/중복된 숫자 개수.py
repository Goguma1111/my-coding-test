def solution(array, n):
    answer = 0

    for i in array :
        if  i == n : # n이랑 같으면
            answer += 1

    return answer



print(solution([1, 1, 2, 3, 4, 5],1))