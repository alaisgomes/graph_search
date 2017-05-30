#   Universidade de Brasilia
#   TAG - Teoria e Aplicacao de Grafos
#   10/0091008 - Aline Lais Gomes Tavares
#
#    Para executar: 
#      BFS:             python main.py -b
#      Dijkstra:        python main.py -d
#      Bellman-Ford:    python main.py -bf
#

import sys
from data_structures import Tree, Vertex, Graph


def initialize_single_source(G, s):
	pass

def bellman_ford(G, s):
	initialize_single_source(G, s)
	
	for v in G:
		relax(v,u)

