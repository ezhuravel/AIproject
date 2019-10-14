#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon October 13 2019

@author: Eugene Zhuravel, Carrie Jacob, Ethan Burkhart, Scott Carrington

Group Project
"""

class Map:
    def build_map(filename):
        # Reads in the xml file and builds a map. Format we
        # are using is: https://graphonline.ru/en/
        pass
    
    def find_path():
        # takes exisiting map and runs Dijkstra's algorithn
        pass
    
    def print_result():
        # prints out the path taken
        pass
        
    def print_map():
        # This is optional, we can print the graph first, then show the path we take.
        pass

# Print out the header info
print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: Eugene Zhuravel, Carrie Jacob, Ethan Burkhart, Scott Carrington")
print("")


map = Map()
map.build_map("file") 
map.print_map("file") # I think this can be optional
map.find_path()
map.print_map()