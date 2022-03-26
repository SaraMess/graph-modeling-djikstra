
from py4j.java_gateway import JavaGateway

################ functions if using Java graph classes #################

def getSommets(e):
    l=[]
    for i in range(len(e.getSommets())):
        l.append(e.getSommets()[i])
    return  l

def getAdjacents(e,j):
    l=[]
    for i in range(len(e.getAdjacents(int(j)))):
        l.append(e.getAdjacents(int(j))[i])
    return l

def getCoutArete(g,a,b):
    return g.getCoutArete(int(a),int(b))

def g2d(e):
    """ Convert a Java graph to an arc-coast dictionnary like format graph
    """
    gra={}
    for a in getSommets(e):
        gra[a]=[]
        for aa in getAdjacents(e,a):
            gra[a].append(aa)
    return gra

def costJava(g,a,b):
    """ Use if Java
    """
    return getCoutArete(g,a,b) 
