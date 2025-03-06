def solution(array):
    max1 = max(array)
    index = array.index(max1)

    return [max1, index]


print(solution([0, 8, 1]))