#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      BFS:        python bfs.py
#      Dijkstra:   python dijkstra.py
#

import json
import collections


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vertices_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def __str__(self):
        string = ""
        for v in self:
            string = string + "#{} node => {}\n".format(v.get_id(), self.vertices_dict[v.get_id()])
        return string

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vertices_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices_dict:
            return self.vertices_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0.0):
        if frm not in self.vertices_dict:
            self.add_vertex(frm)
        if to not in self.vertices_dict:
            self.add_vertex(to)

        self.vertices_dict[frm].add_neighbor(self.vertices_dict[to], cost)
        self.vertices_dict[to].add_neighbor(self.vertices_dict[frm], cost)

    def get_vertices(self):
        return self.vertices_dict.keys()


class Tree():
    def __init__(self, root_vertex=None):
        self.tree = collections.OrderedDict()
        if(root_vertex):
            self.tree.setdefault(root_vertex, [])

    def __str__(self):
        string = "Root: {}\n".format(next(iter(self.tree)))
        string += "Tree: \n {} \n\n".format(json.dumps(self.tree))
        return string

    def set_child(self, parent, child):
        if (self.tree.get(parent) is None):
            self.tree.setdefault(parent, [])
        self.tree[parent].append(child)


#def ()