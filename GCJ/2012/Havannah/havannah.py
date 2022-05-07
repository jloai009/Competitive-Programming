from collections import Counter
from sys import stdin

def play(case, game):
    """
    Google Code Jam 2012 Round 3 Problem 2:
    Havannah
    """

    S, M, moves = game
    graph = UnionFind(S)
    ans = []
    ring = False

    for i, move in enumerate(moves):
        r, c = move
        
        neigh = [(r+1,c+1), (r,c+1), (r-1,c), (r-1,c-1), (r,c-1), (r+1,c)]

        neighReps = [(graph.find(n) if n in graph.up else None) for n in neigh] * 2
    
        for i1, r1 in enumerate(neighReps):
            for i2, r2 in enumerate(neighReps):
                if i1 < i2 and 1 < i2-i1 < 5 and r1 and r2 and r1 == r2:
                    if any([n is None for n in neighReps[i1+1:i2]]) \
                    and any([n is None for n in neighReps[i2+1:i1+6]]):
                        ring = True

        for adj in neigh:
            if adj in graph.up:
                graph.union(move, adj)

        rep, compInfo = graph.find(move)
        corners = edges = 0

        for j in range(6):
            if compInfo & 1<<j:
                corners += 1
        
        for j in range(6, 12):
            if compInfo & 1<<j:
                edges += 1

        if corners > 1:
            ans.append("bridge")
        if edges > 2:
            ans.append("fork")
        if ring:
            ans.append("ring")

        if ans:
            output = [f"Case #{case}: "]
            for j, w in enumerate(ans):
                output.append(w)
                if j+1 != len(ans):
                    output.append("-")
            output.append(f" in move {i+1}")
            print("".join(output))
            return

    print(f"Case #{case}: none")


class UnionFind:
    def __init__(self, S):
        self.S = S
        self.up = {}
        self.rank = Counter()

    def find(self, x):
        if x not in self.up:
            self.up[x] = [x, checkType(x, self.S)]

        if self.up[x][0] == x:
            return self.up[x]

        self.up[x] = self.find(self.up[x][0])
        return self.up[x]

    def union(self, x, y):
        repX = self.find(x)
        repY = self.find(y)
        
        if repX == repY:
            return False

        if self.rank[repX[0]] == self.rank[repY[0]]:
            self.rank[repX[0]] += 1
            self.up[repX[0]][1] |= repY[1]
            self.up[repY[0]] = repX

        elif self.rank[repX[0]] > self.rank[repY[0]]:
            self.up[repX[0]][1] |= repY[1]
            self.up[repY[0]] = repX

        else:
            self.up[repY[0]][1] |= repX[1]
            self.up[repX[0]] = repY
        return True


def checkType(x, S):
    for i, corner in enumerate(((1,1), (1,S), (S, S*2-1), (S*2-1, S*2-1), (S*2-1, S), (S, 1))):
        if x == corner:
            return 1 << i

    if S < 3:
        return 0
    
    r, c = x
    if r == 1:
        return 1 << 6
    elif c == 1:
        return 1 << 7
    elif c == S*2-1:
        return 1 << 8
    elif r == S*2-1:
        return 1 << 9
    elif abs(r-c) == S-1:
        if r > c:
            return 1 << 10
        else:
            return 1 << 11

    return 0


if __name__ == "__main__":
    T = int(stdin.readline())
    instances = []
    for _ in range(T):
        S, M = list(map(int, stdin.readline().split()))
        moves = []
        for _ in range(M):
            moves.append(tuple(map(int, stdin.readline().split())))

        instances.append([S, M, moves])

    for i, instance in enumerate(instances):
        play(i+1,instance)
