from collections import defaultdict

with open('input.txt') as file:
    connections = list(map(tuple, (line.strip().split("-") for line in file)))

graph = defaultdict(set)

for x, y in connections:
    graph[x].add(y)
    graph[y].add(x)

connected_sets = 0
for node in graph:
    for neighbour in graph[node]:
        contains_t = node[0] == "t" or neighbour[0] == "t"
        for second_neighbour in graph[neighbour]:
            if second_neighbour in graph[node] and (contains_t or second_neighbour[0] == "t"):
                connected_sets += 1

print(connected_sets // 6)