def solution(n):
    answer = 0
    for i in range(1, n+1) :
        count = 0

        for j in range(1, i+1):
            if i % j == 0 :
                count = count +1
                if count >=3 :
                    answer = answer + 1
                    break




    return answer


print(solution(15))