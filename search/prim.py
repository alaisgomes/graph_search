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
#from .dijkstra import extract_min

key = {} # d
pi = {}
S = []

def extract_min(queue, r):
    min_distance = float('inf')
    min_id = 0
    for v in key:
        if key[v] < min_distance:
            if v not in S:
                min_distance = key[v]
                min_id = v

    removed_vertex = queue.remove_vertex(min_id)
    return removed_vertex
    

def prim(G, r):
    global key
    global S
    S = []

    for u in G:
        key[u.get_id()] = float('inf')
        pi[u.get_id()] = None

    key[r.get_id()] = 0

    queue = Graph()
    queue = copy.deepcopy(G)

    while queue.get_vertices():

        u = extract_min(queue, r)
        if (u):
            S.append(u.get_id())
            for v in u.get_connections():
                if (v in queue) and (u.get_weight(v) < key[v.get_id()]):
                    pi[v.get_id()] = u.get_id()
                    key[v.get_id()] = u.get_weight(v)
        else:
            break

    return pi


