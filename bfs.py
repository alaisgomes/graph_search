#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      BFS:             python main.py -b
#      Dijkstra:        python main.py -d
#      Bellman-Ford:    python main.py -bf
#      Floyd-Warshall:  python main.py -fw
#


import json
import collections
from data_structures import Tree, Vertex, Graph


def BFS(G, s):
    color = {}  # 0 = Branco; 1 = Cinza; 2 = Preto
    d = {}
    pi = {}
    queue = []

    s_id = s.get_id()

    for v in G:
        v_id = v.get_id()
        color[v_id] = 0
        d[v_id] = 0
        pi[v_id] = None

    color[s_id] = 1
    d[s_id] = 0
    pi[s_id] = None

    tree = Tree(s_id)
    queue.append(s)

    while queue:
        u = queue.pop(0)
        u_id = u.get_id()

        for v in u.get_connections():
            v_id = v.get_id()

            if color[v_id] == 0:
                tree.set_child(u_id, v_id)
                color[v_id] = 1
                d[v_id] = d[v_id] + 1
                pi[v_id] = u_id
                queue.append(v)

        color[u_id] = 2

    return tree