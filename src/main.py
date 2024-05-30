import networkx as nx 
# import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
import infomap as im
import modularitydensity as md
# from modularitydensity.metrics import modularity_density
# from modularitydensity.fine_tuned_modularity_density import fine_tuned_clustering_qds
import numpy as np
import measures as m
from sklearn.metrics import normalized_mutual_info_score
import csv
# matplotlib.use('Agg')

def main():
    print("Hello World!")
    
    # Generate network with LFR
    graph = nx.generators.community.LFR_benchmark_graph(n=250,              # Number of Nodes
                                                        tau1=3,             # Power Law exponent for degree distribution
                                                        tau2=1.5,           # Power law exponent for community size distribution
                                                        mu=0.1,             # Fraction of inter-community edges incident to each node
                                                        average_degree=5,   # Desired average degree of nodes in the created graph
                                                        min_degree=None,    # Minimum degree of nodes in the created graph
                                                        max_degree=None,    # Maximum degree of nodes in the created graph
                                                        min_community=20,   # Minimum degree for each node
                                                        max_community=None, # Maximum degree for each node
                                                        tol=1e-7,           # Tolerance when comparing floats
                                                        max_iters=500,      # Maximum number of iterations to try to create the community sizes
                                                        seed=10             # Indicator of random number generation state
                                                       )
    

    communitiesGroundTruth = {frozenset(graph.nodes[v]["community"]) for v in graph}

    # Detect communities
    communities = nx.algorithms.community.louvain_communities(G=graph,           # NetworkX graph
                                                              weight=None,     # The name of an edge attribute that holds the numerical value used as a weight
                                                              resolution=1,    # If resolution is less than 1, the algorithm favors larger communities. Greater than 1 favors smaller communities
                                                              threshold=1e-7,  # Modularity gain threshold for each level.
                                                              seed=20
                                                             )
    
    # Draw communities
    pos = nx.spring_layout(graph,seed=12)
    nx.draw(graph, pos, edge_color='k', with_labels=True, font_weight='light', node_size= 280, width= 0.9)
    
    # Give unique color and label to communities
    num = len(communities)
    
    cmap = mpl.colormaps['viridis'].resampled(num+1)
    colors = [mcolors.to_hex(cmap(i)) for i in range(num)]
    
    for i,community in enumerate(communities):
        nx.draw_networkx_nodes(graph,pos,nodelist=community,node_color=colors[i],label=f'C{i}_{len(community)}')
    
    plt.legend()
    plt.savefig('figure.png')
    
    
    # mod max
    
    rmax, rmaxPartition = m.modularity_maximization(graph)
    rlouvain = nx.community.modularity(graph, communities)
    
    print(f'ground truth: {communitiesGroundTruth}')
    print(f'comm: {communities}')
    print(f'rmax: {rmax} and rlouvain: {rlouvain}')
    
    nmi_louvain = normalized_mutual_info_score(convert_to_1d(250,communitiesGroundTruth), convert_to_1d(250,communities))
    nmi_modmax = normalized_mutual_info_score(convert_to_1d(250,communitiesGroundTruth), convert_to_1d(250,rmaxPartition))
    
    print(f'nmi score louvain: {nmi_louvain}')
    print(f'nmi score max: {nmi_modmax}')
    
    # map equation
    # infomap = im.Infomap()
    
    # for edge in graph.edges():
    #     infomap.add_link(edge[0], edge[1])
        
    # infomap.run()

    # communitiesME = infomap.getModules().items()
    # nmi_mapeq = normalized_mutual_info_score(convert_to_1d(250,communitiesGroundTruth), convert_to_1d(250,communitiesME))
    # print(f'nmi score map eq: {nmi_mapeq}')
    # for node, community in communitiesME.items():
    #     print(f"Node {node} is in community {community}")
    
    # codelength, partitionME = m.map_equation(graph)
    # print(f'Map Eq: {codelength}')
    # nmi_mapeq = normalized_mutual_info_score(convert_to_1d(250,communitiesGroundTruth), convert_to_1d(250,partitionME))
    # print(f'nmi score map eq: {nmi_mapeq}')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def convert_to_1d(size, communities):
    arr = np.zeros(size)
    for i, com in enumerate(communities):
        for node in com:
            arr[node] = i
    return arr


    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Greedy modularity maximization 
    # modMax = m.modularity_maximization(graph,communities,50)
    # print(f'modularity maximization: {modMax}')
    # mm = nx.community.greedy_modularity_communities(graph)
    # print(f' Number of communities: {len(mm)}, modularity maximization (greedy) of community 1: {mm[0]}')
    
    # # map equation
    # infomap = im.Infomap("--two-level")
    
    # for edge in graph.edges():
    #     infomap.add_link(edge[0], edge[1])
        
    # infomap.run()

        
    # communitiesME = infomap.getModules()
    # for node, community in communitiesME.items():
    #     print(f"Node {node} is in community {community}")
        
    # modularity density
    # adj = nx.to_scipy_sparse_array(graph) #convert to sparse matrix
    # communityArray = md.fine_tuned_modularity_density.fine_tuned_clustering_qds(graph)
    # modden = md.metrics.modularity_density(adj, communityArray, np.unique(communityArray))
    # print(f'modularity density: {modden}')
    
    

    
    
    
    
if __name__ == "__main__":
    main()


