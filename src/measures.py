import networkx as nx
import random

import numpy as np
from typing import List

# def initial_two_partitions(graph: nx.Graph) -> Tuple[List[int], List[int]]:
#     """ This function randomly partitions the graph into two equal size sets

#     Args:
#         graph (nx.Graph): is a community network.

#     Returns:
#         Tuple[List[int], List[int]]: Returns two partitions/sets of ≈ equal length.
#     """
#     nodes = List(graph.nodes())
#     random.shuffle(nodes)
#     center = len(nodes) * 0.5
#     return nodes[:center], nodes[center:]

# def move_node(node: int, from_partition: List[int], to_partition: List[int]) -> None:
#     """ This function moves a node from one partition to the other partition.

#     Args:
#         node (int): The node to move.
#         from_partition (List[int]): The partition in which the node is removed.
#         to_partition (List[int]): The partition in which the node is added.
#     """
#     from_partition.remove(node)
#     to_partition.append(node)

# def compute_measure_score_effect(graph: nx.Graph, 
#                                  partitions: Tuple[List[int], List[int]],
#                                  node: int,
#                                  measure_func: Callable[[nx.Graph, List[List[int]]], float]
#                                  )-> float:
#     """ This function calculates what the effect is of moving the given node to the other partition.

#     Args:
#         graph (nx.Graph): The community network.
#         partitions (Tuple[List[int], List[int]]): The two partitions of the graph.
#         node (int): The node that we move to the other partition.
#         measure_func (Callable[[nx.Graph, List[List[int]]], float]): The function that determines the score based on the given measurement function.

#     Returns:
#         float: The measurement score if we would move the specified node to the other partition.
#     """
#     partition1, partition2 = partitions
#     if node in partition1:
#         move_node(node,partition1,partition2)
#     else:
#         move_node(node,partition2,partition1)
        
#     score = measure_func(graph, [partition1,partition2])
    
#     if node in partition2:
#         move_node(node,partition2,partition1)
#     else:
#         move_node(node,partition1,partition2)
    
#     return score


# def simple_node_moving_naive(graph, measureFunc, maximize=True):
#     partition1, partition2 = initial_two_partitions(graph)
#     partitions = (partition1, partition2)
#     old_partitions = tuple(partitions) # * 1
#     best_partitions = tuple(partitions) #  * 1
#     best_score = measureFunc(graph, partitions)
    
#     for n in partition1:
#         move_and_assess(graph, n, partition1, partition2, measureFunc, maximize, old_partitions, best_partitions, best_score)
  
#     for n in partition2:
#         move_and_assess(graph, n, partition2, partition1, measureFunc, maximize, old_partitions, best_partitions, best_score)
        
#     old_partitions = best_partitions

#     return

# def move_and_assess(graph, node, p1, p2, measureFunc, maximize, old_ps, best_ps, best_score):
#     move_node(node, p1, p2)
#     score = measureFunc(graph, (p1, p2))
#     isBetter = False
#     if maximize:
#         isBetter = score > best_score
#     else:
#         isBetter = score < best_score

#     if isBetter: 
#         best_partitions = (p1, p2)
#         best_score = score
#     p1, p2 = old_ps

def modularity(graph: nx.Graph, partition: List[List[int]]) -> float:
    return nx.community.modularity(graph, partition)


def modularity_density(graph: nx.Graph, partition: List[List[int]]) -> float:
    #zelf definieren
    return

def performance(graph: nx.Graph, partition: List[List[int]]) -> float:
    return

def coverage(graph: nx.Graph, partition: List[List[int]]) -> float:
    return







sdfdfd   def func
dfdfdf   def func
dfdf   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
dffd   def func
# dffd  # def func





















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