import networkx as nx 
# import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
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
    # cmap = cm.get_cmap('hsv', num)
    colors = [mcolors.to_hex(cmap(i)) for i in range(num)]
    
    
    
    for i,community in enumerate(communities):
        nx.draw_networkx_nodes(graph,pos,nodelist=community,node_color=colors[i],label=f'C{i}_{len(community)}')
    
    plt.legend()
    plt.savefig('figure.png')
    
if __name__ == "__main__":
    main()