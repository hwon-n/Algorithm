'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''


import sys

queue = []
n = int(input())

for i in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] in 'push':
        queue.append(order[1])
    elif order[0] in 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif order[0] in 'size':
        print(len(queue))
    elif order[0] in 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] in 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[0] in 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])