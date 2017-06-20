#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      Prim:            python main.py -p
#


import math
import copy
from .data_structures import Tree, Vertex, Graph
from .dijkstra import extract_min

key = {}
pi = {}

def prim(G, r):
    global key

    for u in G:
        key[u.get_id()] = float('inf')
        pi[u.get_id()] = None

    key[r.get_id()] = 0
    queue = Graph()
    queue = copy.deepcopy(G)

    while queue.get_vertices():
        u = extract_min(queue, r)
        if (u):
            for v in u.get_connections():
                if (v in queue) and (u.get_weight(v) < key[v.get_id()]):
                    pi[v.get_id()] = u.get_id()
                    key[v.get_id()] = u.get_weight(v)
        else:
            break

    return pi


