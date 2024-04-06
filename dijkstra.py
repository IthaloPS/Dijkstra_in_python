import sys


def dijkstra(grafo, origem, destino):
    distancia = {v: sys.maxsize for v in grafo}
    distancia[origem] = 0
    visitado = set()
    caminho = {v: [] for v in grafo}

    while visitado != set(distancia):
        atual_vertex = None
        menor_distancia = sys.maxsize

        for v in grafo:
            if v not in visitado and distancia[v] < menor_distancia:
                atual_vertex = v
                menor_distancia = distancia[v]
                if v == destino:
                    break

        visitado.add(atual_vertex)

        for vizinho, peso in grafo[atual_vertex].items():
            if distancia[atual_vertex] + peso < distancia[vizinho]:
                distancia[vizinho] = distancia[atual_vertex] + peso
                caminho[vizinho] = caminho[atual_vertex] + [atual_vertex]

    caminho_completo = caminho[destino] + [destino]
    return distancia[destino], caminho_completo


grafo_cidade_base = {
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

origem_entrada = str(input('Saindo de: ').upper().rstrip().lstrip())
destino_entrada = str(input('Indo para: ').upper().rstrip().lstrip())
if origem_entrada not in grafo_cidade_base or destino_entrada not in grafo_cidade_base:
    print('Valores não existentes!!!')
elif origem_entrada == destino_entrada:
    print(f'Você já está em {destino_entrada}!')
else:
    distancia_total, caminho = dijkstra(grafo_cidade_base, origem_entrada, destino_entrada)
    print(f'O caminho mais curto de {origem_entrada} até {destino_entrada} é de {distancia_total} KM')
    print('Caminho percorrido:')
    print(' -> '.join(caminho))
