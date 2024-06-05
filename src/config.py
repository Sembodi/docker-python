from dataclasses import dataclass
from typing import List, Any

@dataclass
class graph_config:
    name            : str
    nodes           : int
    tau1            : float=3
    tau2            : float=1.5
    mu              : float=0.1
    average_degree  : float=None
    min_degree      : int=None
    max_degree      : int=None
    min_community   : int=None
    max_community   : int=None
    tol             : float=1e-7
    max_iter        : int=500
    seed            : Any=None

    def to_list(self) -> List[Any]:
        return [self.nodes,
                self.tau1,
                self.tau2,
                self.mu,
                self.average_degree,
                self.min_degree,
                self.max_degree,
                self.min_community,
                self.max_community, 
                self.tol, 
                self.max_iter, 
                self.seed]
        
    def to_mapping(self):
        return {"n"                   : self.nodes,
                "tau1"                : self.tau1,
                "tau2"                : self.tau2,
                "mu"                  : self.mu,
                "average_degree"      : self.average_degree,
                "min_degree"          : self.min_degree,
                "max_degree"          : self.max_degree,
                "min_community"       : self.min_community,
                "max_community"       : self.max_community,
                "tol"                 : self.tol,
                "max_iters"           : self.max_iter,
                "seed"                : self.seed
                }
    
large_sparse_graph = graph_config("large_sparse_graphs"
                                 ,nodes=100000
                                 ,tau1=2
                                 ,tau2=2
                                 ,min_degree=10
                                 ,max_degree=50
                                 ,min_community=100
                                 ,max_community=999
                                 ,max_iter = 500)

medium_sparse_graph = graph_config("medium_sparse_graphs"
                                 ,nodes=10000
                                 ,min_degree=5
                                 ,max_degree=15
                                 ,min_community=200
                                 ,max_community=2000)

small_sparse_graph = graph_config("small_sparse_graphs"
                                 ,nodes=1000
                                 ,min_degree=5
                                 ,max_degree=15
                                 ,min_community=20
                                 ,max_community=200)

large_dense_graph = graph_config("large_dense_graphs"
                                 ,nodes=100000
                                 ,min_degree=100
                                 ,max_degree=500
                                 ,min_community=100
                                 ,max_community=1000
                                 ,max_iter = 500)

medium_dense_graph = graph_config("medium_dense_graphs"
                                 ,nodes=10000
                                 ,min_degree=50
                                 ,max_degree=200
                                 ,min_community=50
                                 ,max_community=300)

small_dense_graph = graph_config("small_dense_graphs"
                                 ,nodes=1000
                                 ,min_degree=20
                                 ,max_degree=100
                                 ,min_community=20
                                 ,max_community=100)
        
 