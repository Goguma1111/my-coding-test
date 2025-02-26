def solution(n):
    
    answer = n **(1/2)
    if answer % 1 ==0 :
        return 1

    else:
        return 2


   


print(solution(144))       
print(solution(976))        