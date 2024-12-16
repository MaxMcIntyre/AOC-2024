from collections import defaultdict, deque

with open('input.txt') as file:
    data = file.read()

orderings, updates = data.split("\n\n")
orderings = orderings.split("\n")
updates = updates.split("\n")

graph = defaultdict(list)
for ordering in orderings:
    a, b = ordering.split("|")
    graph[a].append(b)

res = 0

for update in updates:
    update_list = update.split(",")
    update_nodes = set(update_list)
    in_degree = {node: 0 for node in update_nodes}

    for node in update_nodes:
        for neighbour in graph[node]:
            if neighbour in update_nodes:
                in_degree[neighbour] += 1
    
    queue = deque(update_list)
    topo_order = []

    while queue:
        node = queue.popleft()
        if in_degree[node] != 0:
            break

        for neighbour in graph[node]:
            if neighbour in update_nodes:
                in_degree[neighbour] -= 1
    
    if not queue:
        res += int(update_list[len(update_list) // 2])
    
print(res)