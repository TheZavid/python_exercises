GRAPH = dict()
DIST = dict()


def to_visit(vertex):
    output = set()
    for next_v in GRAPH[vertex]:
        if DIST[next_v] == -1:
            output.add(next_v)

    return output

def furthest(graph, v):
    global GRAPH
    global DIST
    GRAPH = graph
    del graph
    for key in GRAPH:
        DIST[key] = -1
    cur_nodes = set(v)
    nodes_to_visit = set()
    distance = 0
    last_known = cur_nodes
    while cur_nodes:
        for node in cur_nodes:
            DIST[node] = distance

        for node in cur_nodes:
            nodes_to_visit |= to_visit(node)

        last_known = cur_nodes
        cur_nodes = nodes_to_visit
        nodes_to_visit = set()
        distance += 1

    return last_known.pop(), (distance - 1) # -1 because distance is incremented on the last loop


abc = { 'a': ['b', 'd'], 'b': ['a', 'c', 'd'], 'c': ['b', 'e'],
'd': ['a', 'b', 'e'], 'e': ['c', 'd'] }

print(furthest(abc, 'b'))
