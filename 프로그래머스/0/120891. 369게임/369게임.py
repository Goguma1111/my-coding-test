def solution(order):
    answer = str(order).count("3") + str(order).count("6") + str(order).count("9")

    return answer

print(solution("2,9,4,2,3"))