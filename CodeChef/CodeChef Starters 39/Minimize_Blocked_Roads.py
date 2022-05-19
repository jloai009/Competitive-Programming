# CodeChef MINBLOCK Minimize Blocked Roads
# https://www.codechef.com/problems/MINBLOCK

import os, sys, io
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

edges = []
cities_saved = []

def dfs(node, parent, blocked):
    descendants = 0

    for edge in edges[node]:
        child, blockable = edge
        if child == parent:
            continue

        nodes_in_path = dfs(child, node, blocked or blockable)
        descendants += nodes_in_path

        if not blocked and blockable:
            cities_saved.append(nodes_in_path)
            
    return descendants + 1

for _ in range(int(input())):
    N, K = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    cities_saved.clear()

    for _ in range(N-1):
        U, V, X = map(int, input().split())
        edges[U].append((V, X))
        edges[V].append((U, X))
    
    dfs(1, -1, False)
    cities_saved.sort(reverse=True)

    infected = N
    roads_blocked = 0
    for n in cities_saved:
        if infected <= K:
            break
        infected -= n
        roads_blocked += 1

    print(roads_blocked if infected <= K else -1)