def solution(array, n):
    array.sort()

    dist = []

    for a in array :
        dist.append(abs(n-a))


    m = min(dist)

    f = dist. index(m)

    return array[f]

print(solution([3, 10, 28], 20))