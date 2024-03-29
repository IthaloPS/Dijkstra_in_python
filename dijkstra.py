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
                if (v == destination):
                  break

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            if distance[current_vertex] + weight < distance[neighbor]:
                distance[neighbor] = distance[current_vertex] + weight

    return distance

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86}
}

origin = str(input('from: '))
destination = str(input('to: '))

short_path = dijkstra(graph, origin, destination)

print(f'O caminho mais curto de {origin}, ate {destination} é de {short_path.get(destination)}')
