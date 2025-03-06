def solution(rsp):
    win_dict ={'0': '5', '2':'0', '5':'2'}

    answer = []

    for r in rsp:
        answer.append(win_dict[r])

    return ''.join(answer)    


print(solution("2"))
print(solution("205"))