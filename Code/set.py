from binarytree import BinarySearchTree

class Set(object):
    def __init__(self, elements=None):
        self.tree = BinarySearchTree()
        if elements is not None:
            for element in elements:
                self.add(element)

    def contains(self,element):
        return self.tree.contains(element)

    def add(self, element):
        #if the element is not already in the set, insert it
        if not self.contains(element):
            self.tree.insert(element)

    def remove(self, element):
        #delete from the set, if it's in the set
        #else raise key error
        if self.contains(element):
            self.tree.delete(element)
        else:
            raise KeyError

    def union(self, other_set):
        pass

    def intersection(self, other_set):
        pass

    def difference(self, other_set):
        pass

    def is_subset(self, other_set):
        pass
    

