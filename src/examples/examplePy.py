import sys
sys.path.insert(1, '../')
from graph import Graph
from djikstra import *


############################  Test with Python graph class ##########################
print("################################")
print("Testing with Python graph class")
print("################################\n")
path = "../../Data/town10Py.txt"
gra = Graph(10,path)
couple, adj = gra.getArcs(), gra.getAllAdj()
print("Graph with 10 vortices from 0 to 9:\n")
djikstra(0,9,adj,gra,costPy)
path = "../../Data/town146Py.txt"
gra = Graph(146,path)
couple, adj = gra.getArcs(), gra.getAllAdj()
print("Graph with 146 vortices from 0 to 145:\n")
djikstra(0,145,adj,gra,costPy)