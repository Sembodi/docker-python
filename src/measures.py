from typing     import List, Tuple
import networkx as nx

def modularity(graph: nx.Graph, partition: List[List[int]]) -> float:
    sum = 0
    edges = len(graph.edges())

    alpha = 2
    
    for i, com in enumerate(partition):
        ci = len(com)
        eIn, eOut = calc_Ein_Eout(graph, com)

        sum += eIn / edges - ((alpha * eIn + eOut)/(alpha * edges))**2

    return sum

def zahn_condorcet(graph, partition) -> float:
    sum = 0
    nodes = len(graph.nodes())
    edges = len(graph.edges())
    norm_fac = 2 / (nodes*(nodes - 1))

    for i, com in enumerate(partition):
        ci = len(com)
        cOther = nodes - ci
        eIn, eOut = calc_Ein_Eout(graph, com)

        sum += norm_fac*(eIn + (ci * cOther - eOut)/2)
    
    return sum

def calc_Ein_Eout(graph: nx.Graph, part: List[int]) -> Tuple[int, int]:
    ein, eout = 0, 0
    
    for node in part:
        for neighbor in graph.neighbors(node):
            if (neighbor in part):
                ein += .5
            else:
                eout += 1
    return ein, eout