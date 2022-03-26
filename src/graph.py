    # #######################################################
    #/ Graph modelisation and Djikstra shortest path solver
    # #######################################################
import math
import copy


class Graph:
    """ Modelling class for graphs
        extract from .txt file adjacents dictionnary and arc-coast dictionnary
    """
    def __init__(self,nbs,path):
        self.vortex=range(nbs)
        self.couple, self.adj = self.getData(path) #sommets + cout arc + dict 

    def getData(self,path):
        with open(path) as file :
                couple = {}
                adj = {}
                for i in file.readlines() :
                    i = i.split(' ')
                    couple[(int(i[0]),int(i[1]))]= float(i[2])
                    adj[int(i[0])]=adj.get(int(i[0]),[])
                    adj[int(i[0])].append(int(i[1]))
                    adj[int(i[1])]=adj.get(int(i[1]),[])
                    adj[int(i[1])].append(int(i[0]))
        return couple, adj
    
    def getArcs(self):
        return self.couple

    def getAllAdj(self):
        return self.adj

    def getAdjacent(self,vortex,adj):
        return self.adj.get(vortex,[])
    
    def getArcCoast(self,v1,v2):
        # if (v1,v2) in list(self.couple.keys):
        #     return self.couple.get((v1,v2))
        cout = self.couple.get((v1,v2),None)
        if cout != None : 
            return self.couple.get((v1,v2))
        return self.couple.get((v2,v1),math.inf)


def costPy(g,a,b):
    """ Use if Python
    """
    return g.getArcCoast(a,b)