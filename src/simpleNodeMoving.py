import networkx as nx
import random
from typing import List, Tuple, Callable, Set

class snm:
    def __init__(self, 
                 graph: nx.Graph, 
                 measure_func: Callable[[nx.Graph, List[List[int]]], float], 
                 maximize: bool=True
                 ) -> None:
        """_summary_

        Args:
            graph (nx.Graph): _description_
            measure_func (Callable[[nx.Graph, List[List[int]]], float]): _description_
            maximize (bool, optional): _description_. Defaults to True.
        """
        self.graph         : nx.Graph                                     = graph
        self.maximize      : bool                                         = maximize
        self.score_func    : Callable[[nx.Graph, List[List[int]]], float] = measure_func
        self.partitions    : Tuple[List[int], List[int]]                  = self.__initial_two_partitions()
        self.old_partitions: Tuple[List[int], List[int]]                  = tuple(self.partitions)
        self.best_partition: Tuple[List[int], List[int]]                  = tuple(self.partitions)
        self.best_score    : float                                        = self.score_func(graph, self.best_partition)
        
        
    def __initial_two_partitions(self) -> Tuple[List[int], List[int]]:
        """ This function randomly partitions the graph into two equal size sets

        Args:
            graph (nx.Graph): is a community network.

        Returns:
            Tuple[List[int], List[int]]: Returns two partitions/sets of ≈ equal length.
        """
        nodes = List(self.graph.nodes())
        random.shuffle(nodes)
        center = len(nodes) * 0.5
        return nodes[:center], nodes[center:]
    
    def __move_node(self, node: int, from_partition: List[int], to_partition: List[int]) -> None:
        """ This function moves a node from one partition to the other partition.

        Args:
            node (int): The node to move.
            from_partition (List[int]): The partition in which the node is removed.
            to_partition (List[int]): The partition in which the node is added.
        """
        from_partition.remove(node)
        to_partition.append(node)
        
    def __compute_score_effect(self, node: int) -> float:
        """ This function calculates what the effect is of moving the given node to the other partition.

        Args:
            graph (nx.Graph): The community network.
            partitions (Tuple[List[int], List[int]]): The two partitions of the graph.
            node (int): The node that we move to the other partition.
            measure_func (Callable[[nx.Graph, List[List[int]]], float]): The function that determines the score based on the given measurement function.

        Returns:
            float: The measurement score if we would move the specified node to the other partition.
        """
        partition1, partition2 = self.partitions
        if node in partition1:
            score = self.__compute_score_step(self, node, partition1, partition2)
        else:
            score = self.__compute_score_step(self, node, partition2, partition1)

        return score
    
    def __compute_score_step(self, node: int, partition1: List[int], partition2: List[int]) -> float:
        """ This function calculates the score of moving `node` from `partition1` to `partition2`.

        Args:
            node (int): The node to move.
            partition1 (List[int]): The first partition.
            partition2 (List[int]): The second partition.

        Returns:
            float: The score of moving the node to the second partition.
        """
        self.__move_node(node,partition1,partition2)
        score = self.measure_func(self.graph, [partition1,partition2])
        self.__move_node(node,partition2,partition1)
        return score
    
    def __move_nodes(self) -> Tuple[Tuple[List[int], List[int]], float]:
        """_summary_

        Returns:
            Tuple[Tuple[List[int], List[int]], float]: _description_
        """
        partition1, partition2 = self.partitions

        X: Set[int] = set(self.graph.nodes())
        
        while X:
            best_node: int = None

            # Initialize best_effect to -inf when maximize = true, to +inf when maximize = false.
            sign = -1
            if not self.maximize: 
                sign = 1
            
            best_effect: float = sign * float('inf') # TODO: take maximize parameter into account
            
            for node in X:
                effect = self.__compute_score_effect(node)

                if self.__is_improving(effect, best_effect): 
                    best_effect = effect
                    best_node = node

            # if best_node is not None:
            if best_node in partition1:
                self.__move_node(best_node, partition1, partition2)
            else:
                self.__move_node(best_node, partition2, partition1)
                
            X.remove(best_node)
            current_score = self.score_func()
            
            if self.__is_improving(current_score, best_score):
                best_score = current_score
                best_partitions = (partition1.copy(), partition2.copy())

        return best_partitions, best_score
    
    def __is_improving(self, effect, best_effect) -> bool:
        if self.maximize:
            isBetter = effect > best_effect
        else:
            isBetter = effect < best_effect
        return isBetter
    
    def run(self) -> Tuple[Tuple[List[int], List[int]], float]:
        """ This function runs the algorithm and returns the best partitions and the corresponding measure score.

        Returns:
            Tuple[Tuple[List[int], List[int]], float]: partitions and measure score
        """
        improvement = True
        while improvement:
            new_partitions, new_score = self.__move_nodes()
            if new_score > self.best_score:
                self.best_partitions = new_partitions
                self.best_score = new_score
            else:
                improvement = False

        return self.best_partitions, self.best_score