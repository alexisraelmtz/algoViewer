from collections import deque


graph = [
    # adjacency list
    [1, 2],             # 0
    [0, 2, 3],          # 1
    [0, 1, 3],          # 2
    [1, 2, 5],          # 3
    [5, 9],             # 4
    [3, 4, 9, 10, 6],   # 5
    [7, 8, 11, 10, 5],  # 6
    [6],                # 7
    [6],                # 8
    [4, 5],             # 9
    [11, 14, 5, 6],     # 10
    [6, 18, 12, 10],    # 11
    [13, 11, 18],       # 12
    [12, 16, 14],       # 13
    [13, 16, 15, 10],   # 14
    [14],               # 15
    [13, 17, 14],       # 16
    [16],               # 17
    [12, 11],           # 18
    [19],               # 19
]
size = len(graph)


def breadthForSearch(node):
    q = deque()
    q.append(node)

    visited = [False for _ in range(size)]
    visited[node] = True

    previous = [None for _ in range(size)]
    while q:
        node = q.popleft()
        neighbours = graph[node]
        for next in neighbours:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                previous[next] = node
                print(
                    f"Currently at Node {node}: {neighbours}. Visiting {next}")
            elif visited[next]:
                print(f"BackTracking Node: {node}")
    return previous


init = 10
prev = breadthForSearch(init)
print(prev)