import networkx as nx
import numpy as np

class Section():

    def __init__(self, _obj) -> None:
        self.section = _obj


    def complement(self):
        pass


    def inverse(self):
        for edge_env in self.section.values():
            edge_env['R+'], edge_env['R-'] = edge_env['R-'], edge_env['R+']
        return self.section
    

    def narrowing(self, set):
        #TODO Добавить валидацию
        pass
    

    def intersection(self, second_section):
        #TODO Добавить валидацию
        pass
    

    def union(self, second_section):
        #TODO Добавить валидацию
        pass

    def difference(self, second_section):
        for key in second_section:
            for node in second_section[key]['R+']:
                if node in self.section[key]['R+']:
                    self.section[key]['R+'].remove(node)
            for node in second_section[key]['R-']:
                if node in self.section[key]['R-']:
                    self.section[key]['R-'].remove(node)
        return self.section
    

    def symmetric_difference(self, second_section):
        #TODO Добавить валидацию
        pass
    

    def multiple(self, second_section):
        #TODO Добавить валидацию
        pass
