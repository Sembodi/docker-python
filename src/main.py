import time
from typing          import List, Callable
from sklearn.metrics import normalized_mutual_info_score
import networkx           as nx 
import numpy              as np
import measures           as m
import generalizedLouvain as gl
import dataExport         as de
import config             as cfg


def compute_data(config: cfg.graph_config, 
                 measures: List[Callable[[nx.Graph, List[List[int]]], float]], 
                 num_iter: int = 5, random_seed: bool = False) -> None:
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
            nmi = normalized_mutual_info_score(to_labels(config.nodes,communitiesGroundTruth), to_labels(config.nodes,communities))
            
            # create data row
            row = config.to_list() + [score,nmi,computation_time]   

            mat3[i].append(row)
        
        succeeded += 1
        
    print(f' Saving data to files...')
    header = ["nodes","tau1","tau2","mu","average_degree","min_degree","max_degree","min_community","max_community","tol","max_iters","seed","score","nmi","time"]
    
    for i, measure in enumerate(measures):
        de.write_csv_file(config.name + "_" + measure.__name__,header,mat3[i])
    
def main():
    graph_types = [cfg.n100_dense    ,cfg.n100_sparse
                  ,cfg.n1000_dense   ,cfg.n1000_sparse
                  ,cfg.n10_000_dense ,cfg.n10_000_sparse
                  ,cfg.n100_000_dense,cfg.n100_000_sparse]
    
    for graph_type in graph_types:
        compute_data(graph_type,[m.modularity,m.zahn_condorcet],1)
    
def to_labels(size, communities):
    arr = np.zeros(size)
    for i, com in enumerate(communities):
        for node in com:
            arr[node] = i
    return arr
    
if __name__ == "__main__":
    main()