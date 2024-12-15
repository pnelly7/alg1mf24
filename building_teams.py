from collections import deque

def is_bipartite(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * (n + 1)

    def bfs(start):
        queue = deque([start])
        color[start] = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False 
        return True

    for i in range(1, n + 1):
        if color[i] == -1:
            if not bfs(i):
                return "IMPOSSIBLE"
    return " ".join(str(c + 1) for c in color[1:])

if __name__ == "__main__":
    n, m = map(int, input("Add meg a csúcsok és élek számát: ").split())
    edges = []
    for _ in range(m):
        u, v = map(int, input("Adj meg egy élt (két csúcsot): ").split())
        edges.append((u, v))
    print(is_bipartite(n, edges))