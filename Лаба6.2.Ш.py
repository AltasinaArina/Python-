adj = [
    [1, 3],
    [0, 3, 4, 5],
    [4, 5],
    [0, 1, 5],
    [1, 2],
    [1, 2, 3]
]
level = [-1] * len(adj)
def bfs(s):
    global level
    level[s] = 0
    queue = [s]
    while queue:
        v = queue.pop(0)
        for w in adj[v]:
            if level[w] == -1:
                queue.append(w)
                level[w] = level[v] + 1
for i in range(len(adj)):
    if level[i] == -1:
        bfs(i)
print(level[2])

