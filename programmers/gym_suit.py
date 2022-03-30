def solution(n, lost, reserve):    
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    
    for i in set_reserve:
        p = i + 1
        m = i - 1
        
        if m in set_lost:
            set_lost.remove(m)
        elif p in set_lost:
            set_lost.remove(p)
    
    return n - len(set_lost)
