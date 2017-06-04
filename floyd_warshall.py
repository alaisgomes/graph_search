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
def init(W, n):
	PI = [[None for i in range(n)] for j in range(n)]

	for i in range(n):
		for j in range(n):
			if (i != j and W[i][j] < float(math.inf)):
				PI[i][j] = i+1

	return PI

def floyd_warshall(W):
	global s
	
	n = len(W)
	D = W
	PI = init(W, n)

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if D[i][j] > D[i][k] + D[k][j]:
					D[i][j] = D[i][k] + D[k][j]
					PI[i][j] = PI[k][j]

	
	for i in range(n):
			print (PI[i])
	
#	print(D)
