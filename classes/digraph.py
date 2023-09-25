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
        pass


    def symmetric_difference(self, second_digraph):
        nodes1 = set(self.digraph.nodes)
        nodes2 = set(second_digraph.digraph.nodes)
        nodes_set = nodes1.union(nodes2)
        nodes = [i for i in nodes_set]
        edges_set = set(self.digraph.edges).symmetric_difference(set(second_digraph.digraph.edges))
        edges = [i for i in edges_set]
        G = nx.DiGraph()
        G.add_edges_from(edges)
        return DiGraph(G)
    

    def multiple(self, second_digraph):
        #TODO Добавить валидацию
        pass

