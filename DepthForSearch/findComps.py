# Finding Connected Components:
# --- Depth First Search (DFS) ---


graph = [
    # adjacency list
    [1, 2],             # 0
    [0, 2, 3],          # 1
    [0, 1, 3],          # 2
    [1, 2],             # 3
    [5, 9],             # 4
    [4, 9, 10, 6],      # 5
    [7, 8, 11, 10, 5],  # 6
    [6],                # 7
    [6],                # 8
    [4, 5],             # 9
    [11, 5, 6],         # 10
    [6, 18, 12, 10],    # 11
    [11, 18],           # 12
    [16, 14],           # 13
    [13, 16, 15],       # 14
    [14],               # 15
    [13, 17, 14],       # 16
    [16],               # 17
    [12, 11],           # 18
]
size = len(graph)
count = 0
components = [0 for _ in range(size)]
visited = [False for _ in range(size)]


def findComponents():
    global count
    for position in range(size):
        if not visited[position]:
            count += 1
            depthForSearch(position)
        print(f"BackTracking Node: {position}")
    return (count, components)


def depthForSearch(node):
    visited[node] = True
    components[node] = count

    neighbours = graph[node]
    for next in neighbours:
        if not visited[next]:
            print(
                f"Currently at Node {node}: {neighbours}. Visiting {next}"
            )
            depthForSearch(next)


# Initialize DFS at node zero
comps, list = findComponents()
print(f"Number of Connected Components: {comps}\n")
for node in range(len(list)):
    print(f"Node {node} in Component {list[node]}")
