'''
문제 : 
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

입력:
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.

'''


def dfs(node, graph, visited):
    visited[node] = True
    print(node, end = ' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(i, graph, visited)

def bfs(node, graph, visited):
    queue = [node]
    visited[node] = True
    while queue:
        pop = queue.pop(0)
        print(pop, end = ' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]


for i in range(m):
    index, value = input().split(' ')
    index = int(index)
    value = int(value)
    
    graph[index] += [value]
    graph[value] += [index]

for i in range(1, n + 1):
    graph[i].sort()
    
visited = [False] * (n + 1)
dfs(v, graph, visited)

print()

visited = [False] * (n + 1)
bfs(v, graph, visited)