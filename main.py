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
            print ("( {} , {}, {})".format(v_id, wid, v.get_weight(w)))


def create_structures(matrix, n):
    g = Graph()
    try:
        for i in range(n):
            g.add_vertex(i+1)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] > 0:
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
        #print (G)
        if (sys.argv[1] == "-b"):
            for v in G:
                BFS(G, v)

        elif (sys.argv[1] == "-d"):
            for v in G:
                dijkstra(G, v)
        else:
             raise ValueError("Choose an algorithm to use: \n -b: BFS; \n -d: Dijkstra; \n")


    except ValueError as e:
        print(e)

    except IOError as e:
        print ("I/O error({0}): {1}.".format(e.errno, e.strerror))
    
    except SyntaxError as e:
        print("Syntax Error: Input provided wrongly.")

#    except:
#        print("Error: Unexpected error happened.")



if __name__ == '__main__':
    main()
