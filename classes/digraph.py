import networkx as nx
import numpy as np

class DiGraph():

    def __init__(self, _obj) -> None:
        self.digraph = _obj


    def complement(self):
        nodes, edges = self.digraph.nodes(), set(self.digraph.edges())
        all_edges = {(i, j) for j in nodes for i in nodes}
        new_edges = all_edges - edges
        self.digraph.remove_edges_from(edges)
        self.digraph.add_edges_from(new_edges)
        return self.digraph


    def inverse(self):
        pass
    

    def narrowing(self, set):
        #TODO Добавить валидацию
        return self.digraph.subgraph(set).copy()
    

    def intersection(self, second_digraph):
        #TODO Добавить валидацию
        pass
    

    def union(self, second_digraph):
        #TODO Добавить валидацию
        pass


    def difference(self, second_digraph):
        #TODO Добавить валидацию
        new_digraph = nx.DiGraph()
        new_digraph.add_nodes_from(self.digraph.nodes)
        new_digraph.add_edges_from(set(self.digraph.edges).difference(set(second_digraph.edges)))
        return new_digraph


    def symmetric_difference(self, second_digraph):
        #TODO Добавить валидацию
        pass
    

    def multiple(self, second_digraph):
        #TODO Добавить валидацию
        pass

