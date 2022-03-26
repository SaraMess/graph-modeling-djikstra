
    # #######################################################
    #/ Graph modelisation and Djikstra shortest path solver
    # #######################################################

import math
import copy

class Stack:
    """ Stack data structure
    """
    def __init__(self):
            self._stack = []
            self.nb_element=0
    def stack(self, val):
        self.nb_elm=self.nb_element+1
        self._stack.append(val)
    def pop(self):
        if self._nb_elm ==0 :
            return None
        else :
            self._nb_elm =self._nb_elm -1
            return self._stack
    def show(self):
        return self._stack


class Matrix:
    """Matrix data structure saving the paths, coast and state of the vortex
    """
    def __init__(self,heads):
        self._dict={}
        for i in heads:
            self._dict[i]=[[],math.inf,False]
    
    def update(self, head, road, cost, mark=False):
        self._dict[head][0]=road
        self._dict[head][1]=cost
        self._dict[head][2]=mark
    def mark(self, head):
        self._dict[head][2]=True
    
    def get(self,head,n):
        return self._dict[head][n]

    def get_min(self):
        l=[]
        for key,val in self._dict.items() :
            if not val[2]:
                l.append([key, val[1]])
        l.sort(key=lambda x:x[1])
        if l==[] :
            return None 
        return l[0][0]
    def __str__(self):
        return "list of heads {}".format([a for a in self._dict.keys()])

def BFS(to_visit,graph,fifo=Stack(),visited=set()):
    """ Breadth first search graph exploration
    """
    if type(to_visit)==int :
        to_visit=[[to_visit,k] for k in graph[to_visit]]
    while(to_visit !=[]):
        vsn=[]
        visit_next=[]
        done=set([k for i,k in to_visit])
        visited=visited|set(done)
        for i,l in enumerate(to_visit): #left vorteces 
            vsn.append(l)
            for j in graph[l[1]] :  #next vortices for each vortex
                if j not in visited:
                    visit_next.append([l[1],j])
            if i==len(to_visit)-1:
                fifo.stack(vsn) # vorteces by order 
        to_visit = copy.deepcopy(visit_next)
    return fifo.show(), visited
        


def djikstra(start,end,graph,g_class,cost):
    """ Shortes path solver
        Input: start: start vortex, end: end vortex, graph: dictionnary of adjacent vorteces, 
            g_class: graph class either Python or Java class, cost: cost function
        Output: Shortest paths matrix for all the visited sub-graph vorteces
    """
    pgl,heads=BFS(start,graph)
    mat=Matrix(heads | set([start,]))
    mat.update(start,[],0,True)
    while(start !=None):
        mat.mark(start)
        f=Stack()
        pgll,g=BFS(start,graph,f)
        if pgll!=[]:
            for k,i in pgll[0] :
                if mat.get(i,1)>mat.get(start,1)+cost(g_class,start,i):
                    mat.update(i,mat.get(start,0)+[start,],mat.get(start,1)+cost(g_class,start,i))
        start=mat.get_min()
    if start == None :
        sol = mat.get(end,0)
        for i in sol:
            print(i,'->',end=' ')
        print(end)
        return mat








