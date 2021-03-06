#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      BFS:             python main.py -b
#      Dijkstra:        python main.py -d
#      Bellman-Ford:    python main.py -bf
#      Floyd-Warshall:  python main.py -fw
#      Prim:            python main.py -p
#      Kruskal:         python main.py -k
#

import json
import collections



class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent_weight = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent_weight])

    def add_neighbor(self, neighbor, weight=0.0):
        self.adjacent_weight[neighbor] = weight

    def get_connections(self):
        return self.adjacent_weight.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent_weight[neighbor]


class Graph:
    def __init__(self, direction=True):
        self.vertices_dict = collections.OrderedDict()
        self.num_vertices = 0
        self.num_edges = 0
        self.direction = direction

    def __iter__(self):
        return iter(self.vertices_dict.values())

    def __str__(self):
        string = ""
        for v in self:
            string = string + "#{} node => {}\n".format(v.get_id(), self.vertices_dict[v.get_id()])
        return string

    def set_direction(self, direction):
        self.direction = direction

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vertices_dict[node] = new_vertex
        return new_vertex

    def remove_vertex(self, node):
        if node in self.vertices_dict:
            self.num_vertices = self.num_vertices - 1
            removed_vertex = self.vertices_dict.pop(node)
            return removed_vertex

    def get_vertex(self, n):
        if n in self.vertices_dict:
            return self.vertices_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=-0.0):
        if frm not in self.vertices_dict:
            self.add_vertex(frm)
        if to not in self.vertices_dict:
            self.add_vertex(to)

        if (self.direction):
            self.num_edges += 1
            self.vertices_dict[frm].add_neighbor(self.vertices_dict[to], cost)
        else:
            self.num_edges += 2
            self.vertices_dict[frm].add_neighbor(self.vertices_dict[to], cost)
            self.vertices_dict[to].add_neighbor(self.vertices_dict[frm], cost)


    def get_vertices(self):
        return self.vertices_dict.keys()

    def get_n_vertices(self):
        return self.num_vertices

    def get_n_edges(self):
        return self.num_edges

    def reorder_graph(self, vertex_key):
        self.vertices_dict.move_to_end(vertex_key,last=False)


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

