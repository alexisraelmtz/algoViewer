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
]
size = len(graph)


def breadthForSearch(start, end):
    def solve(node):
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
                    print(
                        f"Currently at Node {node}: {neighbours}. Visiting {next}")
                    q.append(next)
                    visited[next] = True
                    previous[next] = node
                elif visited[next]:
                    print(f"BackTracking Node: {node}")
        print(previous)
        return previous

    def buildPath(start, end, reversePath):
        path = []
        check = [False for _ in range(size)]
        for position in reversePath[end:start:-1]:
            if position != None and not check[position]:
                path.append(position)
            else:
                break
        path.reverse()
        if path[0] == start:
            return path
        return []

    reversePath = solve(start)

    return buildPath(start, end, reversePath)


init = 0
end = 9
path = breadthForSearch(init, end)
print(path)
