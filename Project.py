#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon October 13 2019

@author: Eugene Zhuravel, Carrie Jacob, Ethan Burkhart, Scott Carrington

Group Project
"""
from xml.dom import minidom

class Vector:
    def __init__ (self, name, text):
        self.name = name
        self.text = text
        self.neighbors = {}
    
    def __repr__(self):
        if not self.text:
            return "Vector " + self.name
        else:
            return self.text
    
    def __eq__(self, other):
          return (self.name) == (other)
    
    def __hash__(self):
        return hash(self.name)
    
class Map:
    def __init__ (self):
        self.node_path = []
        
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
            self.vectors[vec.attributes['id'].value] = Vector(vec.attributes['id'].value, vec.attributes['mainText'].value)

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
    
    def find_path(self, start, target):
        
        if(not start):
            print ("Start not found")
            return 
        
        if(not start):
            print ("End not found")
            return 
            
        path ={start: (None, 0)}
        current_node = self.vectors[start]    
        visited = set()
        
        while current_node != target:
            visited.add(current_node)
            weight_to_current_node = path[current_node][1]
            
            for neighbor in current_node.neighbors:
                weight  = current_node.neighbors[neighbor][1] + weight_to_current_node
                
                if neighbor not in path:
                        path[neighbor] = (current_node, weight)                
                else:
                    current_shortest_weight = path[neighbor][1]
                    if current_shortest_weight > weight:
                        path[neighbor] = (current_node, weight)
            
            next_destinations = {node: path[node] for node in path if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
            # Work back through destinations in shortest path
        
        
        while current_node is not None:
            self.node_path.append(current_node)
            next_node = path[current_node][0]
            current_node = next_node
        # Reverse path
        self.node_path = self.node_path[::-1]
        
      

    
    def print_result(self):
        print ("Shortest rout:")
        print (*self.node_path, sep = " => ")
                
        
        
    def print_map(self):
        for vector in self.vectors:
            print(self.vectors[vector])
            print("    neighbors: " +str(self.vectors[vector].neighbors))
    
    def getVertex(self, name):
        
        if(name in self.vectors.keys()):
            return self.vectors[name]
        
        # check if they gave a name
        for i in self.vectors.values():
            if(i.text == name):
                return self.vectors[i.name]
            
        

# Print out the header info
print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: Eugene Zhuravel, Carrie Jacob, Ethan Burkhart, Scott Carrington")
print("")


map = Map()
map.build_map('map.graphml') 

map.print_map() # I think this can be optional

start = map.getVertex(input("Please name of starting point: "))
end =  map.getVertex(input("Please name of end point: "))



map.find_path(start, end)
map.print_result()
