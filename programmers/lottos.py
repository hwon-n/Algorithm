def solution(lottos, win_nums):
    nums = len([i for i in lottos if i in win_nums])
    win_dict = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    
    if 0 in lottos:
        zeros = lottos.count(0) + nums
    else:
        zeros = nums
    
    answer = [win_dict[zeros], win_dict[nums]]
    return answer