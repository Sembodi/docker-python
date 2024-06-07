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
    
n100_000_sparse = graph_config("n100_000_sparse_graphs"
                               ,nodes=100000
                               ,mu=0.3
                               ,min_degree=10
                               ,max_degree=50
                               ,min_community=100
                               ,max_community=1000)

n100_000_dense = graph_config("n100_000_dense_graphs"
                              ,nodes=100000
                              ,mu=0.3
                              ,min_degree=100
                              ,max_degree=500
                              ,min_community=100
                              ,max_community=1000)

n10_000_sparse = graph_config("n10_000_sparse_graphs"
                              ,nodes=10000
                              ,mu=0.2
                              ,min_degree=5
                              ,max_degree=15
                              ,min_community=50
                              ,max_community=500)

n10_000_dense = graph_config("n10_000_dense_graphs"
                             ,nodes=10000
                             ,mu=0.2
                             ,min_degree=50
                             ,max_degree=150
                             ,min_community=50
                             ,max_community=500)

n1000_sparse = graph_config("n1000_sparse_graphs"
                            ,nodes=1000
                            ,min_degree=5
                            ,max_degree=15
                            ,min_community=20
                            ,max_community=200)

n1000_dense = graph_config("n1000_dense_graphs"
                           ,nodes=1000
                           ,min_degree=20
                           ,max_degree=100
                           ,min_community=20
                           ,max_community=200)

n100_sparse = graph_config("n100_sparse_graphs"
                           ,nodes=100
                           ,min_degree = 2
                           ,max_degree = 10
                           ,min_community=20
                           ,max_community=60)

n100_dense = graph_config("n100_dense_graphs"
                          ,nodes=100
                          ,min_degree=15
                          ,max_degree=40
                          ,min_community=20
                          ,max_community=60)
        
 