n = 10
adj_list = [[2, 4, 6],
            [9],
            [0, 3],
            [2, 4],
            [0, 3],
            [],
            [0, 7, 8],
            [6],
            [6],
            [1]]
s = 0
visited = [False] * n
def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if visited[w] == False:
            dfs(w)
dfs(s)
print(visited.count(True))
