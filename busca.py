#   Univers_idade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares

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

    print(tree)


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


#################################
def print_structures():
    for v in g:
        BFS(g, v)
        break
        for w in v.get_connections():
            v_id = v.get_id()
            wid = w.get_id()
            print '( {} , {}, {})'.format(v_id, wid, v.get_weight(w))

    for v in g:
        print 'g.vert_dict[{}] = {}'.format(v.get_id(), g.vert_dict[v.get_id()])


def main():

    g = Graph()

    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)

    g.add_edge(1, 2, 0.8)
    g.add_edge(2, 4, 0.1)
    g.add_edge(2, 3, 0.3)
    g.add_edge(3, 5, 0.7)
    g.add_edge(4, 6, 0.25)
    g.add_edge(5, 6, 0.4)

    for v in g:
        BFS(g, v)


# ---------------------------------------------------

if __name__ == '__main__':
    main()
