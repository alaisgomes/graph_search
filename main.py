#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar:
#      BFS:        python main.py -b
#      Dijkstra:   python main.py -d
#

import sys
from data_structures import Tree, Vertex, Graph
from dijkstra import dijkstra
from bfs import BFS


def print_structures(g):
    for v in g:
        BFS(g, v)
        break
        for w in v.get_connections():
            v_id = v.get_id()
            wid = w.get_id()
            print '( {} , {}, {})'.format(v_id, wid, v.get_weight(w))


def create_structures(matrix, n):
    g = Graph()

    for i in range(n):
        g.add_vertex(i)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                g.add_edge(i, j, matrix[i][j])

    pass


def main():
    nro_vertices = int(input("# of vertces: "))

    matrix = [[0.0 for i in range(nro_vertices)] for j in range(nro_vertices)]

    for i in range(nro_vertices):
        for j in range(nro_vertices):
            matrix[i][j] = int(input())

    g = create_structures(matrix, nro_vertices)
    print (g)
    # g = Graph()

    # g.add_vertex(1)
    # g.add_vertex(2)
    # g.add_vertex(3)
    # g.add_vertex(4)
    # g.add_vertex(5)
    # g.add_vertex(6)

    # g.add_edge(1, 2, 0.8)
    # g.add_edge(2, 4, 0.1)
    # g.add_edge(2, 3, 0.3)
    # g.add_edge(3, 5, 0.7)
    # g.add_edge(4, 6, 0.25)
    # g.add_edge(5, 6, 0.4)

    try:
        if (sys.argv[1] == "-b"):
            for v in g:
                BFS(g, v)

        elif (sys.argv[1] == "-d"):
            #print(g)
            pass

    except:
        print("Choose an algorithm to use: \n -b: BFS; \n -d: Dijkstra; \n")



if __name__ == '__main__':
    main()
