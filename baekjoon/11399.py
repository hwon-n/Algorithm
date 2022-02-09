import sys

def sum_time():
    n = int(input())
    time_list = input().split(' ')
    time_list = [int(i) for i in time_list]
    time_list.sort()
    
    for i in range(1, n):
        time_list[i] = time_list[i-1] + time_list[i]
            
    result = sum(time_list)
    return result

print(sum_time())