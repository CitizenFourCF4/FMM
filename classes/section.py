import networkx as nx
import numpy as np

class Section():

    def __init__(self, _obj) -> None:
        self.section = _obj


    def complement(self):
        keys = self.section.keys()
        add_R = {key:{} for key in keys}
        for elem in keys:
            add_R[elem]['R+'] = add_R[elem].get('R+', [])+[i for i in set(keys) - set(self.section[elem]['R+'])]
            add_R[elem]['R-'] = add_R[elem].get('R-', [])+[i for i in set(keys) - set(self.section[elem]['R-'])]
        return add_R


    def inverse(self):
        for edge_env in self.section.values():
            edge_env['R+'], edge_env['R-'] = edge_env['R-'], edge_env['R+']
        return self.section

    def narrowing(self, set):
        narrowed = {}
        for key in self.section:
            if key in set:
                narrowed[key] = self.section[key]
                for node in narrowed[key]['R+']:
                    if node not in set:
                        narrowed[key]['R+'].remove(node)
                for node in narrowed[key]['R-']:
                    if node not in set:
                        narrowed[key]['R-'].remove(node)
        return narrowed

    def intersection(self, second_section):
        intersected = {}
        for key in self.section:
            intersected[key] = {'R+': [], 'R-': []}
            for node in self.section[key]['R+']:
                if node in second_section[key]['R+']:
                    intersected[key]['R+'].append(node)
            for node in self.section[key]['R-']:
                if node in second_section[key]['R-']:
                    intersected[key]['R-'].append(node)
        return intersected
    

    def union(self, second_section):
        #TODO Добавить валидацию
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
        for node in list(second_section.keys()):
            # Для R+
            for elem_r_plus in second_section[node]['R+']:
                if elem_r_plus not in self.section[node]['R+']:
                    self.section[node]['R+'].append(elem_r_plus)
            # Для R-
            for elem_r_minus in second_section[node]['R-']:
                if elem_r_minus not in self.section[node]['R-']:
                    self.section[node]['R-'].append(elem_r_minus)
        return self.section

    def multiple(self, second_section):
        multiple = {i: {'R+': [], 'R-': []} for i in self.section.keys()}
        for key in self.section:
            res = set([])
            for node in second_section[key]['R+']:
                res = res.union(set(self.section[node]['R+']))
            multiple[key]['R+'] = list(res)
            res = set([])
            for node in second_section[key]['R-']:
                res = res.union(set(self.section[node]['R-']))
            multiple[key]['R-'] = list(res)
        return multiple
