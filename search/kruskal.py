import math
import collections
from .data_structures import Tree, Vertex, Graph

parent = collections.OrderedDict()
rank = collections.OrderedDict()
S = []

def make_set(v):
    parent[v.get_id()] = v.get_id()
    rank[v.get_id()] = 0

def find_set(v_id):

    if parent[v_id] != v_id:
        parent[v_id] = find_set(parent[v_id])

    return parent[v_id]


def union(v, u):
    r1 = find_set(v)
    r2 = find_set(u)
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]: 
                rank[r2] += 1


def get_small_weight(G):
    global S
    small_w = float('inf')
    small_tuple = []
    for v in G:
        for u in v.get_connections():
            if v.get_weight(u) < small_w:
                if ([v.get_id(), u.get_id(), v.get_weight(u)] not in  S):
                    small_w = v.get_weight(u)
                    small_tuple = [v.get_id(), u.get_id(), small_w]

    if (small_tuple):
        S.append(small_tuple)
        return small_tuple
    else:
        return []


def kruskal(G):
    A = Tree()

    for v in G:
        make_set(v)

    for i in range(G.get_n_edges()):
        vertex_set = get_small_weight(G)
        if find_set(vertex_set[0]) != find_set(vertex_set[1]):
            union(vertex_set[0], vertex_set[1])
            A.set_child(vertex_set[0], vertex_set[1])
    
    return A


