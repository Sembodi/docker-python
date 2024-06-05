import networkx as nx
import random

import numpy as np
from typing import List, Tuple

# def modularity(graph: nx.Graph, partition: List[List[int]]) -> float:
#     return nx.community.modularity(graph, partition)


def modularity(graph: nx.Graph, partition: List[List[int]]) -> float:
    sum = 0
    edges = len(graph.edges())

    alpha = 2
    
    for i, com in enumerate(partition):
        ci = len(com)
        eIn, eOut = calc_Ein_Eout(graph, com)

        sum += eIn / edges - ((alpha * eIn + eOut)/(alpha * edges))**2

    return sum

def deviation_to_uniformity(graph: nx.Graph, partition: List[List[int]]) -> float:
    sum = 0
    nodes = len(graph.nodes())
    edges = len(graph.edges())

    alpha = 2
    
    for i, com in enumerate(partition):
        ci = len(com)
        eIn, eOut = calc_Ein_Eout(graph, com)

        sum += eIn / edges - (ci/nodes)**2

    return sum


# def modularity_density(graph: nx.Graph, partition: List[List[int]]) -> float:
#     alpha = 2
#     edges = len(graph.edges())
#     sum = 0
    
#     for i, com in enumerate(partition):
#         ci = len(com)
#         eIn, eOut = calc_Ein_Eout(graph, com)
#         dci = calc_dci(alpha, eIn, ci)

#         step = eIn / edges * dci - ((alpha * eIn + eOut)/(alpha * edges)*dci)**2

#         for other in np.delete(partition, i, 0):
#             cj = len(other)
#             ecicj = calc_Ecicj(graph, com, other)
#             dcicj = calc_dcicj(ecicj, ci, cj)

#             step += ecicj / (alpha * edges) * dcicj
        
#         sum += step

#     return sum

def calc_Ein_Eout(graph: nx.Graph, part: List[int]) -> Tuple[int, int]:
    ein, eout = 0, 0
    
    for node in part:
        for neighbor in graph.neighbors(node):
            if (neighbor in part):
                ein += .5
            else:
                eout += 1
    return ein, eout


# def calc_Ecicj(graph: nx.Graph, ci: List[int], cj: List[int]) -> int:
#     ecicj = 0
    
#     for node in ci:
#         for neighbor in graph.neighbors(node):
#             if (neighbor in cj):
#                 ecicj += 1
#     return ecicj

# def calc_dci(alpha, ein, ci) -> int:
#     if (ci < 2):
#         return alpha*ein
#     return alpha * ein / (ci*(ci - 1))

# def calc_dcicj(ecicj, ci, cj) -> int:
#     return ecicj / (ci*cj)



# def performance(graph: nx.Graph, partition: List[List[int]]) -> float:
#     return

# def coverage(graph: nx.Graph, partition: List[List[int]]) -> float:
#     return



















# import infomap as im
# import numpy    as np















# def modularity_maximization(graph, partition, max_iter=100):
# # ! Maybe need to use greedy instead, since this method is expensive to run on large networks.
#     """ Calculates the modularity maximization of the given partition of the graph.

#     Args:
#         graph (NetworkX graph) : The network 
#         partition (List)       : Initial communities partition
#         max_iter (Int)         : Maximum number of iterations to determine the best partition

#     Returns:
#         List: ...
#     """
#     # partition = {node: i for i, node in enumerate(graph.nodes())}
#     array = np.zeros(len(graph.nodes()))
    
#     for i, com in enumerate(partition):
#         for n in com:
#             array[n] = i



#     # Initial modularity
#     max_modularity = nx.community.modularity(graph, partition)
#     best_partition = array.copy()

#     # Repeat until maximum number of iterations or no improvement
#     for _ in range(max_iter):
#         # Local optimization
#         for node in graph.nodes():
#             current_community = partition[node]
#             for neighbor in graph.neighbors(node):
#                 partition[node] = partition[neighbor]
#                 mod = nx.community.modularity(graph, partition)
#                 if mod > max_modularity:
#                     max_modularity = mod
#                     best_partition = partition.copy()
#                 partition[node] = current_community

#     return best_partition

# def swap_community_node(node,comm1,comm2):
#     comm1.remove(node)
#     comm2.append(node)

# def modularity_maximization(graph):
#     partition = nx.community.greedy_modularity_communities(graph)
#     return nx.community.modularity(graph, partition), partition

    
# def map_equation(graph):
#     infomap = im.Infomap('--silent')
    
#     for edge in graph.edges():
#         infomap.add_link(edge[0], edge[1])
        
#     infomap.run()

#     partition = infomap.getModules().items()
#     codelength = infomap.codelength
#     return codelength, partition

    
    # """ Calculates the map equation of the given partition of the graph.

    # Args:
    #     graph (NetworkX graph): The network
    #     partition (List): The communities

    # Returns:
    #     Float: Map Equation value
    # """
    # # Initialize variables
    # L = 0  # Total number of links
    # B = 0  # Total number of bits

    # # Calculate total number of links
    # for u, v in graph.edges():
    #     L += graph[u][v].get('weight', 1)

    # # Calculate map equation
    # for i in set(partition.values()):
    #     nodes_in_community = [n for n in partition.keys() if partition[n] == i]
    #     subgraph = graph.subgraph(nodes_in_community)
    #     lc = subgraph.number_of_edges()
    #     kc = sum([graph.degree(n) for n in nodes_in_community])

    #     # Calculate size of community in bits
    #     size_in_bits = np.log2(kc)

    #     # Calculate contribution to map equation
    #     B += lc * (size_in_bits + np.log2(L)) / L

    # return B