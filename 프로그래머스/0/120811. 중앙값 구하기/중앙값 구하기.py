def solution(array):
    array.sort()

    return array[len(array) // 2]


print(solution([1, 2, 7, 10, 11]))