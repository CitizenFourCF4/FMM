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
        all_keys = list(set(list(self.section.keys())+list(second_section.keys())))
        new_section = {i:{'R+':[],'R-':[]} for i in all_keys}
        for el in all_keys:
            if el in self.section.keys():
                new_section[el]['R+']+=self.section[el]['R+']
                new_section[el]['R-']+=self.section[el]['R-']
            if el in second_section.keys():
                new_section[el]['R+']+=second_section[el]['R+']
                new_section[el]['R-']+=second_section[el]['R-']
            new_section[el]['R+'] = list(set(new_section[el]['R+']))
            new_section[el]['R-'] = list(set(new_section[el]['R-']))
        return new_section
    

    def difference(self, second_section):
        #TODO Добавить валидацию
        pass
    

    def symmetric_difference(self, second_section):
        #TODO Добавить валидацию
        pass
    

    def multiple(self, second_section):
        #TODO Добавить валидацию
        pass
