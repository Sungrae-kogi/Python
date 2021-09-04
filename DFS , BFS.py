import sys

from collections import deque

input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True

    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소 뽑아서 출력
        v=queue.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 미방문된 원소들을 큐에 모두 넣고 방문처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True



graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

visited=[False]*9

bfs(graph,1,visited)
