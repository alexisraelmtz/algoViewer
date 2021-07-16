# Depth First Search (DFS)

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
count = 0
components = [0 for _ in range(size)]
visited = [False for _ in range(size)]


def depthForSearch(node):
    if visited[node]:
        print(f"BackTracking Node: {node}")
        return
    visited[node] = True

    neighbours = graph[node]
    for next in neighbours:
        print(f"Currently at Node {node}: {neighbours}. Visiting {next}")
        depthForSearch(next)


# Initialize DFS at node zero
# init = 18
init = (int(input("Choose Init Node -- Depth for Search Algorithm: ")))
print("\nLoading DFS Algorithm ...\n")
depthForSearch(init)
