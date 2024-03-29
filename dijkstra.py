import sys


def dijkstra(graph, origin, destination):
    distance = {v: sys.maxsize for v in graph}
    distance[origin] = 0
    visited = set()

    while visited != set(distance):
        current_vertex = None
        short_distance = sys.maxsize

        for v in graph:
            if v not in visited and distance[v] < short_distance:
                current_vertex = v
                short_distance = distance[v]
                if v == destination:
                    break

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            if distance[current_vertex] + weight < distance[neighbor]:
                distance[neighbor] = distance[current_vertex] + weight

    return distance


graph = {
    'ARAD': {'ZERIND': 75, 'SIBIU': 140, 'TIMISOARA': 118},
    'ZERIND': {'ARAD': 75, 'ORADEA': 71},
    'ORADEA': {'ZERIND': 71, 'SIBIU': 151},
    'SIBIU': {'ARAD': 140, 'ORADEA': 151, 'FAGARAS': 99, 'RIMNICU VILCEA': 80},
    'TIMISOARA': {'ARAD': 118, 'LUGOJ': 111},
    'LUGOJ': {'TIMISOARA': 111, 'MEHADIA': 70},
    'MEHADIA': {'LUGOJ': 70, 'DROBETA': 75},
    'DROBETA': {'MEHADIA': 75, 'CRAIOVA': 120},
    'CRAIOVA': {'DROBETA': 120, 'RIMNICU VILCEA': 146, 'PITESTI': 138},
    'RIMNICU VILCEA': {'SIBIU': 80, 'CRAIOVA': 146, 'PITESTI': 97},
    'FAGARAS': {'SIBIU': 99, 'BUCHAREST': 211},
    'PITESTI': {'RIMNICU VILCEA': 97, 'CRAIOVA': 138, 'BUCHAREST': 101},
    'BUCHAREST': {'FAGARAS': 211, 'PITESTI': 101, 'GIURGIU': 90, 'URZICENI': 85},
    'GIURGIU': {'BUCHAREST': 90},
    'URZICENI': {'BUCHAREST': 85, 'VASLUI': 142, 'HIRSOVA': 98},
    'VASLUI': {'URZICENI': 142, 'IASI': 92},
    'IASI': {'VASLUI': 92, 'NEAMT': 87},
    'NEAMT': {'IASI': 87},
    'HIRSOVA': {'URZICENI': 98, 'EFORIE': 86},
    'EFORIE': {'HIRSOVA': 86}
}

origin = str(input('from: ').upper().rstrip().lstrip())
destination = str(input('to: ').upper().rstrip().lstrip())
if origin not in graph or destination not in graph:
    print('Valores não existentes!!!')
else:
    short_path = dijkstra(graph, origin, destination)
    print(f'O caminho mais curto de {origin}, ate {destination} é de {short_path.get(destination)}')
