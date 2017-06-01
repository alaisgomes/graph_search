#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      BFS:             python main.py -b
#      Dijkstra:        python main.py -d
#      Bellman-Ford:    python main.py -bf
#    Uma opcao extra pode ser utilizada passando o arg -reg 
#        se deseja que o input seja interpretado como grafo 
#        nao-orientado regular.
#
#

import sys
from data_structures import Tree, Vertex, Graph
from dijkstra import dijkstra, bellman_ford
from bfs import BFS
import collections


def print_structures(g):
    for v in g:
        for w in v.get_connections():
            v_id = v.get_id()
            wid = w.get_id()
            print ("( {} , {}, {})".format(v_id, wid, v.get_weight(w)))


def create_structures(matrix, n):
    g = Graph()

    if ("-reg" in sys.argv):
        g.set_direction(False) # if undirected graph

    try:
        for i in range(n):
            g.add_vertex(i+1)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0:
                    g.add_edge(i+1, j+1, matrix[i][j])

        return g


    except IndexError as e:
        print (e)

    


def main():
    nro_vertices = int(input())
    matrix = [[0.0 for i in range(nro_vertices)] for j in range(nro_vertices)]

    try:
        for i in range(nro_vertices):
            matrix[i] = [float(n) for n in input().split()]
        
        G = create_structures(matrix, nro_vertices)

        #print_structures(G)

        if ("-b" in sys.argv):
            for v in G:
                print ("s = {}. BFS() return:\n {} \n \
                    ".format(v.get_id(), BFS(G, v)))

        elif ("-d" in sys.argv):
            for v in G:
                print ("s = {}. dijkstra() return:\n {} \n \
                    ".format(v.get_id(), dijkstra(G, v)))

        elif ("-bf" in sys.argv):
            for v in G:
                print ("s = {}. bellman_ford() return:\n {} \n \
                    ".format(v.get_id() , bellman_ford(G,v))) 
                

        else:
            raise ValueError("Choose an algorithm to use:\n \
                            -b: BFS; \n -d: Dijkstra; \n")


    except ValueError as e:
        print(e)

    except IOError as e:
        print ("I/O error({0}): {1}.".format(e.errno, e.strerror))
    
    except SyntaxError as e:
        print("Syntax Error: Input provided wrongly.")

    except:
        print("Error: Unexpected error happened.")



if __name__ == '__main__':
    main()
