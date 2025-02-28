def solution(numbers):
    for i in range(len(numbers)) : # 리스트의 길이만큼
        numbers[i] *= 2


    return numbers


print(solution([1, 2, 3, 4, 5]))