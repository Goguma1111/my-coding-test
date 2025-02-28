def solution(numbers, k):
    answer = 0
    p = 0

    for i in range(k) :
        answer = numbers[p]
        p = (p + 2) % len(numbers)

    return answer


print(solution([1,2,3,4],2))