def solution(sides):
    
    return sum(sides) - (max(sides) - min(sides)) -1

print(solution([11, 7]))