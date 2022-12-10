from typing import List

class SpaceNodes:

    def __init__(self,name,weight,parent,type="file") -> None:
        self.name = name
        self.weight = weight
        self.parent = parent
        self.type = type
    """
    initialize the object.

    name - contains the name of the current file object.
    weight - contains the weight of the current file object.
    contains - a container of all spaces nodes that leads from this object.
    parent - the space nodes that it came from
    """
    def __init__(self,name,weight,parent,contains=[],type="folder") -> None:
        self.name = name
        self.contains = contains
        self.weight = weight
        self.parent = parent
        self.type = type

    # Setters
    def setName(self,name):
        self.name = name
    # Setters
    def setContains(self, contains):
        self.contains = contains
    # Setters
    def setWeight(self, weight):
        self.weight += weight
    # Setters
    def setParent(self,parent):
        self.parent = parent

    # Getters
    def getName(self):
        return self.name
    # Getters
    def getContains(self):
        return self.contains
    # Getters
    def getWeight(self):
        return self.weight
    # Getters:
    def getParent(self):
        return self.parent

    # Append to list:
    def appendList(self, newNode):
        self.contains.append(newNode)
    
