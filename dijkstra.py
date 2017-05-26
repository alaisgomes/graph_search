#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      BFS:        python aim.py
#      Dijkstra:   python dijkstra.py
#

# todo
import json
import collections
from data_structures import Tree, Vertex, Graph


def initialize_single_source(G, s):
    pass

def extract_min(Q):
    pass

def relax(u, v):
    pass


def dijkstra(G, s):
    initialize_single_source(G, s)

    S = []

    for v in G:
        queue.append(v)

    while queue:
        u = extract_min(queue)
        u_id = u.get_id()

        if u_id not in S:
            S.append(u_id)

        for v in u.get_connections():
            relax(u, v)

