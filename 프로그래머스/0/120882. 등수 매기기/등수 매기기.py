def solution(score):
    avg = []

    for i in score :
        avg.append(sum(i)/2)

    answer1 = sorted(avg, reverse=True)

    answer = []
    for i in avg :
        answer.append(answer1.index(i) + 1)

    return answer


print(solution([[80, 70],[90, 50], [40, 70], [50, 80]]))