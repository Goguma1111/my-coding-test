def solution(numbers):
    answer = 0

    numbers.sort()
    answer = numbers[-1] * numbers[-2]

    return answer


print(solution([1, 2, 3, 4, 5]))