import sys

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

for _ in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    parents = list(map(int, input().split()))

    root = 1

    for i, p in enumerate(parents, 1):
        if i == p:
            root = i
        else:
            graph[p].append(i)

    path = []
    answer = []

    @bootstrap
    def dfs(node):
        path.append(node)
        if not graph[node]:
            answer.append(list(path))
            path.clear()
        for child in graph[node]:
            yield dfs(child)
        yield

    dfs(root)

    print(len(answer))
    for path in answer:
        print(len(path))
        print(*path)
    print()
