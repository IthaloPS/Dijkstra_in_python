import sys
import networkx as nx
import matplotlib.pyplot as plt


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


def visualizar_grafo(grafo, caminho, origem, destino):
    G = nx.Graph()
    for vertice, vizinhos in grafo.items():
        for vizinho, peso in vizinhos.items():
            G.add_edge(vertice, vizinho, weight=peso)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=600)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=1)

    caminho_arestas = [(caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=caminho_arestas, edge_color='red', width=2.0)

    nx.draw_networkx_nodes(G, pos, nodelist=[origem, destino], node_color='green', node_size=600)

    nx.draw_networkx_labels(G, pos, font_size=6)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

    plt.title("Grafo com Caminho Percorrido")
    plt.axis('off')
    plt.show()


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
while True:
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
        visualizar_grafo(grafo_cidade_base, caminho, origem_entrada, destino_entrada)
