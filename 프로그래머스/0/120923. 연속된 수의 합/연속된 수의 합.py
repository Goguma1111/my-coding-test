def solution(num, total):
    n = total // num -((num -1) // 2)


    answer = []
    for i in range(num) :
        answer.append(n)
        n += 1
    return answer


print(solution(3, 12))