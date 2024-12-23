from collections import defaultdict

with open('input.txt') as file:
    connections = list(map(tuple, (line.strip().split("-") for line in file)))

graph = defaultdict(set)

for x, y in connections:
    graph[x].add(y)
    graph[y].add(x)

def find_maximal_clique(R, P, X):
    maximal_clique = None

    if not P and not X:
        return R
    for v in list(P):
        possible_clique = find_maximal_clique(R | {v}, P & graph[v], X & graph[v])
        if possible_clique and (maximal_clique is None or len(possible_clique) > len(maximal_clique)):
            maximal_clique = possible_clique
        P.remove(v)
        X.add(v)
    
    return maximal_clique

maximal_clique = find_maximal_clique(set(), set(graph.keys()), set())
print(",".join(sorted(list(maximal_clique))))