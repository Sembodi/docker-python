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
import generalizedLouvain as gl
import dataExport as de
import config as cfg
from typing import List, Tuple, Callable, Set


def compute_data(config: cfg.graph_config, 
                 measures: List[Callable[[nx.Graph, List[List[int]]], float]], 
                 num_iter: int = 10, random_seed: bool = False) -> None:
    print(f'computing {config.name}.')
    mat3 = [[] for _ in measures]
    
    succeeded = 0
    if random_seed:
        config.seed = None
    else:
        config.seed = -1

    
    
    while succeeded < num_iter:
        if not random_seed:
            config.seed +=1
        print(f'Compute iteration {succeeded} ...')
        print(f'Generating graph ...')
        try:
            graph = nx.generators.community.LFR_benchmark_graph(**config.to_mapping())
            communitiesGroundTruth = {frozenset(graph.nodes[v]["community"]) for v in graph}
        except Exception as e:
            print(f'Error: {e}. \nFailed to generate with current seed!')
            print(f'Retrying with new seed')
            continue
        
        print(f'Detect communities with generalized Louvain...')
        # for measure in measures:
        for i, measure in enumerate(measures):
            print(f'detect using measure: {measure.__name__} ...')
            start_time = time.time()
            communities = gl.louvain_communities(graph, measure)
            score = measure(graph, communities)
            end_time = time.time()
            
            computation_time = end_time - start_time
            
            # calculate nmi 
            nmi = normalized_mutual_info_score(convert_to_1d(config.nodes,communitiesGroundTruth), convert_to_1d(config.nodes,communities))
        
            # create data row
            row = config.to_list() + [score,nmi,computation_time]   

            mat3[i].append(row)
        
        succeeded += 1
        
    print(f' Saving data to files...')
    header = ["nodes","tau1","tau2","mu","average_degree","min_degree","max_degree","min_community","max_community","tol","max_iters","seed","score","nmi","time"]
    
    for i, measure in enumerate(measures):
        de.write_csv_file(config.name + "_" + measure.__name__,header,mat3[i])
    

def main():
    compute_data(cfg.medium_sparse_graph,[m.modularity,m.deviation_to_uniformity])
    
    
    # print("Hello World!")
    
    # # Generate network with LFR
    # start_time = time.time()
    # nodes= 250
    # tau1=3
    # tau2=1.5
    # mu=0.1
    # average_degree=5
    # min_degree=None
    # max_degree=None
    # min_community=20
    # max_community=None
    # tol=1e-7
    # max_iters=500
    # seed=10

    
    # print("step1")
    # graph = nx.generators.community.LFR_benchmark_graph(n=nodes,              # Number of Nodes
    #                                                     tau1=tau1,             # Power Law exponent for degree distribution
    #                                                     tau2=tau2,           # Power law exponent for community size distribution
    #                                                     mu=mu,             # Fraction of inter-community edges incident to each node
    #                                                     average_degree=average_degree,   # Desired average degree of nodes in the created graph
    #                                                     min_degree=min_degree,    # Minimum degree of nodes in the created graph
    #                                                     max_degree=max_degree,    # Maximum degree of nodes in the created graph
    #                                                     min_community=min_community,   # Minimum degree for each node
    #                                                     max_community=max_community, # Maximum degree for each node
    #                                                     tol=tol,           # Tolerance when comparing floats
    #                                                     max_iters=max_iters,      # Maximum number of iterations to try to create the community sizes
    #                                                     seed=seed            # Indicator of random number generation state
    #                                                    )
    # print(f'step2')
    # end_time = time.time()
    # print(f'graph gen time: {end_time-start_time}')
    
    # start_time = time.time()
    # # nx.community.louvain_communities(graph)
    # communities = gl.louvain_communities(graph, m.modularity)#m.modularity)
    # score = m.modularity(graph, communities)
    # # alg = snm.snm(graph=graph,measure_func=m.modularity,maximize=True)
    # # communities, score= alg.run()
    
    # communitiesGroundTruth = {frozenset(graph.nodes[v]["community"]) for v in graph}
    # nmi = normalized_mutual_info_score(convert_to_1d(nodes,communitiesGroundTruth), convert_to_1d(nodes,communities))
    # end_time = time.time()
    
    # print(f'Computation time: {end_time-start_time}')
    # print(f'modularity score: {score}, nmi score: {nmi}, computation time: {end_time-start_time}')
    
    # header = ["nodes","tau1","tau2","mu","average_degree","min_degree","max_degree","min_community","max_community","tol","max_iters","seed","score","nmi","time"]
    # row = [nodes,tau1,tau2,mu,average_degree,min_degree,max_degree,min_community,max_community,tol,max_iters,seed,score,nmi,end_time-start_time]
    
    # de.write_csv_file("test.csv",header,[row])
      
def convert_to_1d(size, communities):
    arr = np.zeros(size)
    for i, com in enumerate(communities):
        for node in com:
            arr[node] = i
    return arr
    
if __name__ == "__main__":
    main()
