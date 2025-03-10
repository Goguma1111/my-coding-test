def solution(want: list, num: list, disc: list) -> int:
    # 필요한 제품 목록과 수량을 딕셔너리로 변환
    want_dict = {}
    for i, v in enumerate(want):
        want_dict[v] = num[i]
    print(want_dict)

    # 슬라이딩 윈도우 크기
    win_size = sum(num)
    cnt = 0

    # 현재 윈도우 내 제품 개수를 저장하는 딕셔너리
    window_dict = {}

    # 초기 윈도우 설정
    for i in range(win_size):
        item = disc[i]
        window_dict[item] = window_dict.get(item, 0) + 1

    # 두 개의 딕셔너리를 비교
    is_valid = True
    for item in want_dict:
        # 판매물품의 수량이 내가 원하는 수량보다 적거나 없다면
        if window_dict.get(item, 0) < want_dict[item]:
            is_valid = False
            break

    if is_valid:
        cnt += 1

    # 슬라이딩 윈도우 이동
    for i in range(len(disc) - win_size):
        # 제거할 아이템
        remove_item = disc[i]
        window_dict[remove_item] -= 1
        if window_dict[remove_item] == 0:
            del window_dict[remove_item]

        # 추가할 아이템
        add_item = disc[i + win_size]
        window_dict[add_item] = window_dict.get(add_item, 0) + 1

        # 두 개의 딕셔너리를 비교
        is_valid = True
        for item in want_dict:
            # 판매물품의 수량이 내가 원하는 수량보다 적거나 없다면
            if window_dict.get(item, 0) < want_dict[item]:
                is_valid = False
                break

        if is_valid:
            cnt += 1

    return cnt


print(solution(["banana", "apple", "rice", "pork", "pot"],
      [3,2,2,2,1],
      ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))