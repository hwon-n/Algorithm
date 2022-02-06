def solution(participant, completion):
    answer = ''
    hash_dict = {}
    sum_hash = 0
    
    for name in participant:
        hash_dict[hash(name)] = name
        sum_hash += hash(name)
        
    for name in completion:
        sum_hash -= hash(name)
        
    answer = hash_dict[sum_hash]
    
    return answer