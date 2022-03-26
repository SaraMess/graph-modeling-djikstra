
import sys
sys.path.insert(1, '../')
from graphJava import *
from djikstra import *

############################  Test with Java graph class and Py4j module ##########################
print("################################")
print("Testing with Java graph class")
print("################################ \n")
gateway = JavaGateway()
e = gateway.jvm.etape1.Etape1() 
e.setGraphe("../Data/town10.txt",True) 
g=e.getGraphe()
gradic=g2d(g)
g=e.getGraphe()
print("Graph with 10 vortices from 0 to 9:\n")
djikstra(0,9,gradic,g,costJava)
print("Graph with 10 vortices from 1 to 7:\n")
djikstra(1,7,gradic,g,costJava)
print("Graph with 10 vortices from 2 to 9:\n")
djikstra(2,9,gradic,g,costJava)
print("Graph with 10 vortices from 5 to 9:\n")
djikstra(5,9,gradic,g,costJava)
print("###### 30 vortices ######")
e.setGraphe("../Data/town30.txt",True)  
g=e.getGraphe()
gradic=g2d(g)
g=e.getGraphe()
print("Graph with 30 vortices from 0 to 25:\n")
djikstra(0,25,gradic,g,costJava)
print("###### 146 vortices ######")
e.setGraphe("../Data/town150.txt",True) 
g=e.getGraphe()
gradic=g2d(g)
g=e.getGraphe()
print("Graph with 146 vortices from 0 to 145:\n")
djikstra(0,145,gradic,g,costJava)



