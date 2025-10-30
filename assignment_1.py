import time

def read_gragh_file(fileName):
    graph = {}
    num_vertices = 0
    num_edges = 0

    with open(fileName, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('c'):
                continue

            parts = line.split()

            if parts[0] == 'p':
                num_vertices = int(parts[2])
                num_edges = int(parts[3])
                graph = {i: [] for i in range(1, num_vertices+1)}

            elif parts[0] == 'e':
                u = int(parts[1])
                v = int(parts[2])
                graph[u].append(v)
                graph[v].append(u)

    return graph, num_vertices, num_edges


def createExtGraph(graph : dict, v_count : int) -> dict:
    tmp_graph = {}

    for item in graph.keys():
        tmp_graph[item] = [i for i in range(1, v_count+1) if i not in graph[item] and i != item]

    return tmp_graph


def largest_first_rask(graph : dict):
    sorted_vertices = sorted(graph.keys(), key=lambda v: len(graph[v]), reverse=True)
    print(sorted_vertices)

    colors = {}
    available_colors = list(range(len(graph)))

    for vertex in sorted_vertices:
        used_colors = set()
        for neighbor in graph[vertex]:
            if neighbor in colors:
                used_colors.add(colors[neighbor])

        for color in available_colors:
            if color not in used_colors:
                colors[vertex] = color
                break

    return colors, len(set(colors.values()))


def find_max_clique(graph : dict) -> list:

    vertices = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)

    print(f'sorted vertices = {vertices}')

    cliques = []
    clique = []
    count_cliques = 0

    while vertices:

        clique = []
        best_vertex = vertices[0]
        candidates_per_clique = [x for x in vertices if x in graph[best_vertex]]
        clique.append(best_vertex)

        while candidates_per_clique:

            best_vertex_per_clique = candidates_per_clique[0]
            clique.append(best_vertex_per_clique)
            candidates_per_clique = [x for x in candidates_per_clique if x in graph[best_vertex_per_clique]]

        cliques.append(clique)
        count_cliques += 1 
        vertices = [item for item in vertices if item not in clique]

    return cliques, count_cliques


if __name__ == '__main__':

    start_t = time.time()

    graph, V, E = read_gragh_file(f'school1.col')
    
    ext_graph = createExtGraph(graph, V)

    colors, num_of_colors = find_max_clique(ext_graph)

    end_t = time.time()

    execute_time = end_t - start_t

    print(f"colors = {colors}, num_of_colors = {num_of_colors}")

    print(f"execution time = {execute_time}")