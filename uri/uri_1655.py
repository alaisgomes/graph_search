#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#   Executar:
#       python3 uri_1655.py < input


def floyd_warshall(W):
    n = len(W)
    D = W

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if ((i == j) or (i == k) or (k == j)):
                    pass
                elif D[i][j] < D[i][k] * D[k][j]:
                    D[i][j] = D[i][k] * D[k][j]

    print("{0:.6f} percent\n".format(D[0][n-1]*100.0))


def main():
    try:
        try:
            n_vertices, m_edges = [int(n) for n in input().split()]
            matrix = [[0 for i in range(n_vertices)] for j in range(n_vertices)]

            for n in range(m_edges):
                i, j, p = [int(n) for n in input().split()]
                matrix[i-1][j-1] = p/100.0
                matrix[j-1][i-1] = p/100.0

            floyd_warshall(matrix)
        except ValueError:
            pass
    except:
        pass

if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass
    
    main()
