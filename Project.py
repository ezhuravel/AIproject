#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon October 13 2019

@author: Eugene Zhuravel, Carrie Jacob, Ethan Burkhart, Scott Carrington

Group Project
"""
from xml.dom import minidom
import numpy as np

class Vector:
    def __init__ (self, name):
        self.name = name
        self.neighbors = {}
    
    def __repr__(self):
        return "Vector " + self.name
    
    def __eq__(self, other):
          return (self.name) == (other)
    
    def __hash__(self):
        return hash(self.name)
    
class Map:
    def build_map(self,filename):
        # Reads in the xml file and builds a map. Format we
        # are using is: https://graphonline.ru/en/
        
        #read xml file
        xmldoc = minidom.parse(filename)
        
        #declare empty nparray
        self.vectors ={}
    
        #parse out vectors, save to dictionary    
        itemlist = xmldoc.getElementsByTagName('node')    
        for vec in itemlist:                     
            self.vectors[vec.attributes['id'].value] = Vector(vec.attributes['id'].value)

        # read edges and connect the graph 
        edgelist = xmldoc.getElementsByTagName('edge')
        for edge in edgelist:
            start_vect = self.vectors[edge.attributes['vertex1'].value]
            end_vect = self.vectors[edge.attributes['vertex2'].value]
            weight = int(edge.attributes['weight'].value)
            
            #adds a tuple, index 0 is the vector object, and index 1 is the weight of that object
            start_vect.neighbors[end_vect] = (end_vect,weight)
            
            #check if directional
            if edge.attributes['isDirect'].value != "true":
                end_vect.neighbors[start_vect] = (start_vect,weight)
    
    def find_path(self):
        # takes exisiting map and runs Dijkstra's algorithn
        pass
    
    def print_result(self):
        # prints out the path taken
        pass
        
    def print_map(self):
        for vector in self.vectors:
            print(self.vectors[vector])
            print("    neighbors: " +str(self.vectors[vector].neighbors))
      
           
            
        

# Print out the header info
print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: Eugene Zhuravel, Carrie Jacob, Ethan Burkhart, Scott Carrington")
print("")


map = Map()
map.build_map('map.graphml') 
map.print_map() # I think this can be optional
map.find_path()
map.print_map()