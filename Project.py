#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon October 13 2019

@author: Eugene Zhuravel, Carrie Jacob, Ethan Burkhart, Scott Carrington

Group Project
"""
from xml.dom import minidom
import pandas as pd

class Vector:
    def __init__ (self, name):
        self.name = name
        self.edges = []
        
class Map:
    def build_map(self,filename):
        # Reads in the xml file and builds a map. Format we
        # are using is: https://graphonline.ru/en/
        
        vectors = []
        xmldoc = minidom.parse(filename)
        itemlist = xmldoc.getElementsByTagName('node')
        edgelist = xmldoc.getElementsByTagName('node')

        print(itemlist.length)
        #for i in itemlist:
         #   print (i.attributes['id'].value)
          #  vector = Vector(i.attributes['id'].value
           # vectors.append())
    
    
    
    def find_path(self):
        # takes exisiting map and runs Dijkstra's algorithn
        pass
    
    def print_result(self):
        # prints out the path taken
        pass
        
    def print_map(self):
        # This is optional, we can print the graph first, then show the path we take.
        pass

# Print out the header info
print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: Eugene Zhuravel, Carrie Jacob, Ethan Burkhart, Scott Carrington")
print("")


map = Map()
map.build_map('map.graphml') 
map.print_map() # I think this can be optional
map.find_path()
map.print_map()