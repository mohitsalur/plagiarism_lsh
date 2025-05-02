#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Thu Oct  5 12:55:13 2017

@author: hcorrada
"""
def jaccard_similarity(text1: str, text2: str) -> float : 
    set1 = set(text1)
    set2 = set(text2)
    
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    return intersection / union if union != 0 else 0.0 


class Jaccard:
    def _init_(self):
        self._jaccard_dict = None
        
    def compute_similarity(self, shingled_data, docids=None):
        if docids is not None:
            shingled_data = [x for x in shingled_data if x[0] in docids]
        
        ndocs = len(shingled_data)
        self._jaccard_dict = dict()
        
        for i in range(ndocs-1):
            for j in range(i+1, ndocs):
                (doci, si) = shingled_data[i]
                (docj, sj) = shingled_data[j]
                
                key = tuple(sorted((doci, docj)))
                js = jaccard_similarity(si, sj)
                self._jaccard_dict[key] = js
        
    def get_similarity(self, doci, docj):
        key = tuple(sorted((doci, docj)))
        return self._jaccard_dict[key]