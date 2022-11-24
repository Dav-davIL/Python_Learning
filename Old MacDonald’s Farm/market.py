# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 19:52:11 2022

@author: lenovo
"""

class Farm:
    
    def __init__(self, farm_name):
        print(farm_name,"'s farm")
        self.name = farm_name
        self.animals = {}
        
    def add_animal(self, animal_type, animal_number = 1):
        if animal_type in self.animals:
            self.animals[animal_type] = self.animals.get(animal_type) + animal_number
        else:
            self.animals[animal_type] = animal_number
    
    def get_info(self):
        info = ""
        for x,y in self.animals.items():
            info += x + ": " + str(y) + "\n"
        return info

    def get_animal_types(self):
        animal_list = []
        for value in self.animals.keys():
            animal_list.append(value)
        animal_list.sort()
        return animal_list

    def get_short_info(self):
        animal_types = self.get_animal_types()
        short_info = self.name + "'s farm has "
        for value in animal_types:
            if animal_types[len(animal_types)-1] == value:
                short_info += "and " + value + "."
            else:
                short_info += value + " "
        return short_info
            
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
        