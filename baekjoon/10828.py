'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys

s = []
n = int(sys.stdin.readline())

for i in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] in 'push':
        s.append(order[1])
    elif order[0] in 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif order[0] in 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
    elif order[0] in 'size':
        print(len(s))
    elif order[0] in 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)