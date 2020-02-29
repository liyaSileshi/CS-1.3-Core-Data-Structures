from binarytree import BinarySearchTree

class Set(object):
    def __init__(self, elements=None):
        self.tree = BinarySearchTree()
        if elements is not None:
            for element in elements:
                self.add(element)

    def contains(self,item):
        

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def union(self, other_set):
        pass

    def intersection(self, other_set):
        pass

    def difference(self, other_set):
        pass

    def is_subset(self, other_set):
        pass
    

