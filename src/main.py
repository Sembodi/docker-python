from sklearn.metrics import normalized_mutual_info_score
import networkx          as nx 
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib        as mpl
import numpy             as np
import measures          as m
import simpleNodeMoving  as snm
import csv
import time

def main():
    print("Hello World!")
    
    # Generate network with LFR
    start_time = time.time()
    nodes= 250
    graph = nx.generators.community.LFR_benchmark_graph(n=nodes,              # Number of Nodes
                                                        tau1=3,             # Power Law exponent for degree distribution
                                                        tau2=1.5,           # Power law exponent for community size distribution
                                                        mu=0.1,             # Fraction of inter-community edges incident to each node
                                                        average_degree=5,   # Desired average degree of nodes in the created graph
                                                        min_degree=None,    # Minimum degree of nodes in the created graph
                                                        max_degree=None,    # Maximum degree of nodes in the created graph
                                                        min_community=int(nodes*0.25),   # Minimum degree for each node
                                                        max_community=int(nodes*0.75), # Maximum degree for each node
                                                        tol=1e-7,           # Tolerance when comparing floats
                                                        max_iters=500,      # Maximum number of iterations to try to create the community sizes
                                                        seed=10             # Indicator of random number generation state
                                                       )
    end_time = time.time()
    print(f'graph gen time: {end_time-start_time}')
    
    start_time = time.time()
    alg = snm.snm(graph=graph,measure_func=m.modularity,maximize=True)
    communities, score= alg.run()
    
    communitiesGroundTruth = {frozenset(graph.nodes[v]["community"]) for v in graph}
    nmi = normalized_mutual_info_score(convert_to_1d(nodes,communitiesGroundTruth), convert_to_1d(nodes,communities))
    end_time = time.time()
    
    print(f'modularity score: {score}, nmi score: {nmi}, computation time: {end_time-start_time}')
      
def convert_to_1d(size, communities):
    arr = np.zeros(size)
    for i, com in enumerate(communities):
        for node in com:
            arr[node] = i
    return arr
    
if __name__ == "__main__":
    main()
