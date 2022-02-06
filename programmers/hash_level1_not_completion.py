def solution(participant, completion):
    answer = ''
    hash_dict = {}
    sum_hash = 0
    
    # 해쉬 테이블 생성 + 총 합 계산
    for name in participant:
        hash_dict[hash(name)] = name
        sum_hash += hash(name)
        
    # 완주 선수 삭제
    for name in completion:
        sum_hash -= hash(name)
    
    # 총 합에서 완주된 선수를 삭제하고 나면 완주하지 못한 선수가 남음
    answer = hash_dict[sum_hash]
    
    return answer