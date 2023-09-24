import networkx as nx
import numpy as np

class DiGraph():

    def __init__(self, _obj) -> None:
        self.digraph = _obj


    def complement(self):
        pass


    def inverse(self):
        return nx.reverse(self.digraph)
    

    def narrowing(self, set):
        #TODO Добавить валидацию
        pass
    

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
        #TODO Добавить валидацию
        pass
    

    def multiple(self, second_digraph):
        #TODO Добавить валидацию
        pass
