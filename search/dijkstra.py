#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      Dijkstra:        python main.py -d
#


import math
import copy
from .data_structures import Tree, Vertex, Graph

d = {}
pi = {}
S = []


def initialize_single_source(G, s):
    for v in G:
        v_id = v.get_id()
        d[v_id] = float('inf')
        pi[v_id] = None

    d[s.get_id()] = 0.0




def extract_min(queue, s):
    min_distance = float('inf')
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

    if d[v_id] > d[u_id] + u.get_weight(v):
        d[v_id] = float(d[u_id] + u.get_weight(v))
        pi[v_id] = u_id



def dijkstra(G, s):
    initialize_single_source(G, s)

    global S
    S = []

    queue = Graph()
    queue = copy.deepcopy(G) 

    while queue.get_vertices():
        u = extract_min(queue, s)
        if (u):
            u_id = u.get_id()
            S.append(u_id)

            for v in u.get_connections():
                relax(u, v)
        else:
            break

    return pi

def bellman_ford(G, s):
    initialize_single_source(G, s)
    
    H = Graph()
    H = copy.deepcopy(G) 
    H.reorder_graph(s.get_id())

    for i in range(len(H.get_vertices())):
        for u in H:
            for v in u.get_connections():
                relax(u, v)

    for u in H:
        for v in u.get_connections():
            u_id = u.get_id()
            v_id = v.get_id()

            if d[v_id] > float(d[u_id] + u.get_weight(v)) and d[u_id] != float(math.inf):
                return False

    return pi




