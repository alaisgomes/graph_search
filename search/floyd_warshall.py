#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      BFS:             python main.py -b
#      Dijkstra:        python main.py -d
#      Bellman-Ford:    python main.py -bf
#      Floyd-Warshall:  python main.py -fw
#

import math

s = ""
error = False


def init(W, n):
    PI = [[None for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if (i != j and W[i][j] < float(math.inf)):
                PI[i][j] = i + 1

    return PI


def print_all_paths(PI, i, j):
    global s, error
    try:
        if i == j:
            s += " {}".format(i+1)
        elif PI[i][j] == None:
            print("There's no path between {} and {}".format(i+1, j+1))
        else:
            print_all_paths(PI, i, PI[i][j] - 1)
            s += " {}".format(j+1)
    except RecursionError as e:
        print("Error: {}\n".format(e))
        error = True


def floyd_warshall(W):
    global s, error

    n = len(W)
    D = W
    PI = init(W, n)

    # print (D)
    # print(PI)
    for k in range(n):

        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    PI[i][j] = PI[k][j]

        # print("\nIteraton n: {}".format(k+1))
        # print (D)
        # print(PI)

    for i in range(n):
        for j in range(n):
            s = ""
            error = False
            print_all_paths(PI, i, j)
            if not error:
                print("P({}, {}): {} \n".format(i+1, j+1, s))

