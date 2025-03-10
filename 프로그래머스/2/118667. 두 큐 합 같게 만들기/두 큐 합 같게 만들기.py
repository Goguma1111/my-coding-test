from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1),deque(queue2)
    q1_sum, q2_sum = sum(q1), sum(q2)
    for i in range(300000) :
        if q1_sum == q2_sum :
            return i
        elif q1_sum > q2_sum :
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
        else :
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num  

    return -1

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))    