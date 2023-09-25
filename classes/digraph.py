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
        return nx.reverse(self.digraph)
    

    def narrowing(self, set):
        #TODO Добавить валидацию
        return self.digraph.subgraph(set).copy()
    

    def intersection(self, second_digraph):
        #TODO Добавить валидацию
        new_digraph = nx.DiGraph()
        new_digraph.add_nodes_from(self.digraph.nodes)
        new_digraph.add_edges_from(set(self.digraph.edges).intersection(set(second_digraph.edges)))
        return new_digraph
    

    def union(self, second_digraph):
        #TODO Добавить валидацию
        new_digraph = nx.DiGraph()
        new_digraph.add_nodes_from(self.digraph.nodes)
        new_digraph.add_edges_from(set(self.digraph.edges).union(set(second_digraph.edges)))
        return new_digraph


    def difference(self, second_digraph):
        #TODO Добавить валидацию
        new_digraph = nx.DiGraph()
        new_digraph.add_nodes_from(self.digraph.nodes)
        new_digraph.add_edges_from(set(self.digraph.edges).difference(set(second_digraph.edges)))
        return new_digraph


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
        res_graph, res_graph_edges = nx.DiGraph(), []
        for edge_of_G1 in list(self.digraph.edges()):
            for  edge_of_G2 in list(second_digraph.edges()):
                if edge_of_G1[-1] == edge_of_G2[0]:
                    res_graph_edges.append((edge_of_G1[0], edge_of_G2[-1]))
        res_graph.add_edges_from(res_graph_edges)
        return res_graph

