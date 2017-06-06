#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#   Executar:
#       python uri_1655.py < input

import math

s = ""

def print_all_paths(PI, i, j):
    global s
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

def init(W, n):
    PI = [[None for i in range(n)] for j in range(n)]
    g = [[-math.inf for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if (i == j):
                g[i][j] = 0.0
            if (W[i][j] != 0):
                g[i][j] = -W[i][j]

    for i in range(n):
        for j in range(n):
            if (i != j and g[i][j] < float(math.inf)):
                PI[i][j] = i + 1

    return PI, g

def floyd_warshall(W):
    global s
    n = len(W)
    PI, g = init(W, n)

    D = g

    for k in range(n):
        print(D)
        print (PI)
        print("\n")
        for i in range(n):
            for j in range(n):
                if D[i][j] < D[i][k] * D[k][j]:
                    D[i][j] = D[i][k] * D[k][j]
                    PI[i][j] = PI[k][j]


    # get the probabilities

    print_all_paths(PI, 0, 4)
    print("P({}, {}): {} \n".format(0, 4, s))



def main():
    n_vertices, m_edges = [int(n) for n in input().split()]

    matrix = [[0.0 for i in range(n_vertices)] for j in range(n_vertices)]

    for n in range(m_edges):
        i, j, p = [int(n) for n in input().split()]
        matrix[i-1][j-1] = p
        matrix[j-1][i-1] = p
    
    #print (matrix)
    floyd_warshall(matrix)

if __name__ == '__main__':
    main()