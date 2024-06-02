import networkx as nx
from typing import List

def modularity(graph: nx.Graph, partition: List[List[int]]) -> float:
    return nx.community.modularity(graph, partition)


def modularity_density(graph: nx.Graph, partition: List[List[int]]) -> float:
    #zelf definieren
    return

def performance(graph: nx.Graph, partition: List[List[int]]) -> float:
    return

def coverage(graph: nx.Graph, partition: List[List[int]]) -> float:
    return