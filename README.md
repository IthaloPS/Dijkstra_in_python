<h1>O que é o algoritmo de Dijkstra.</h1>


O algoritmo de Dijkstra é um algoritmo clássico usado para encontrar o caminho mais curto entre dois pontos em um grafo, onde todas as arestas têm pesos não negativos. Foi concebido por Edsger W. Dijkstra em 1956.

Ele é comumente usado em problemas de roteamento em redes de computadores, como encontrar a rota mais curta entre dois nós em uma rede de computadores ou na determinação do trajeto mais curto em um sistema de transporte. O algoritmo é também aplicável a uma ampla variedade de outros problemas que podem ser modelados como um grafo ponderado, como em sistemas de logística, planejamento de rotas de veículos, design de circuitos integrados, entre outros.

Em essência, o algoritmo funciona encontrando iterativamente o caminho mais curto de um nó inicial para todos os outros nós no grafo, mantendo uma lista de distâncias mínimas conhecidas de um nó inicial para todos os outros nós. O algoritmo então seleciona o nó mais próximo (ou seja, aquele com a menor distância mínima conhecida) e atualiza as distâncias mínimas para todos os seus vizinhos, considerando os pesos das arestas. Esse processo continua até que todos os nós tenham sido visitados e as distâncias mínimas finais tenham sido determinadas.

Portanto, o algoritmo de Dijkstra é fundamental em muitas aplicações que envolvem encontrar rotas ou caminhos mais curtos em redes ou grafos ponderados.


<h1>Explicação da implementação.</h1>


O algoritmo de Dijkstra é implementado neste código para encontrar o caminho mais curto entre um nó de origem e um nó de destino em um grafo ponderado. Aqui está um breve resumo do funcionamento do método:

Inicialização: O código começa definindo a distância de cada nó do grafo em relação ao nó de origem como infinito (sys.maxsize). A distância do próprio nó de origem é definida como 0. Um conjunto de nós visitados é inicialmente vazio.

Iteração: O algoritmo continua iterando enquanto houver nós não visitados. A cada iteração, ele seleciona o nó não visitado mais próximo (com a menor distância até o momento) como o nó atual.

Atualização das distâncias: Para o nó atual, o algoritmo examina todos os seus vizinhos (ou seja, os nós conectados por uma aresta). Ele calcula a distância até esses vizinhos através do nó atual e atualiza suas distâncias mínimas se a distância recém-calculada for menor do que a distância atualmente registrada.

Marcação como visitado: Após calcular as distâncias mínimas para todos os vizinhos do nó atual, ele é marcado como visitado e removido da lista de nós não visitados.

Conclusão: O algoritmo continua até que todos os nós tenham sido visitados e suas distâncias mínimas tenham sido calculadas. Em seguida, retorna as distâncias mínimas de cada nó em relação ao nó de origem.

Este algoritmo garante encontrar o caminho mais curto de um nó de origem para todos os outros nós no grafo, não apenas para o nó de destino específico. O caminho mais curto do nó de origem para o nó de destino pode ser extraído da estrutura de dados de distâncias mínimas retornada pelo algoritmo.

![Figure_1](https://github.com/IthaloPS/Dijkstra_in_python/assets/102128741/f5d891a8-8974-48ef-b24e-951198d63478)
