#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      BFS:        python aim.py
#      Dijkstra:   python dijkstra.py
#

# todo

import math
import copy
from data_structures import Tree, Vertex, Graph

d = {}
pi = {}
S = []


def initialize_single_source(G, s):
    for v in G:
        v_id = v.get_id()
        d[v_id] = math.inf
        pi[v_id] = None

    d[s.get_id()] = 0




def extract_min(queue, s):
    min_distance = math.inf
    min_id = 0
    for v in d:
        if d[v] < min_distance:
            if v not in S:
                min_distance = d[v]
                min_id = v

    removed_vertex = queue.remove_vertex(min_id)
    return removed_vertex


def relax(u, v):
    v_id = v.get_id()
    u_id = u.get_id()
    
    if d[v_id] > d[u_id] + u.adjacent_weight[v]:
        d[v_id] = d[u_id] + u.adjacent_weight[v]
        pi[v_id] = u_id



def dijkstra(G, s):
    initialize_single_source(G, s)

    global S
    S = []

    queue = Graph()
    queue = copy.deepcopy(G) 

    while queue.get_vertices():
        u = extract_min(queue, s)
        u_id = u.get_id()
        S.append(u_id)

        for v in u.get_connections():
            relax(u, v)

    print (pi)




