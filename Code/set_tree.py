from binarytree import BinarySearchTree

class Set_Tree(object):
    def __init__(self, elements=None):
        self.tree = BinarySearchTree()
        self.size = 0
        if elements is not None:
            for element in elements:
                self.add(element)

    def contains(self, element):
        return self.tree.contains(element)

    def add(self, element):
        #if the element is not already in the set, insert it
        if not self.contains(element):
            self.tree.insert(element)
            self.size += 1
    def remove(self, element):
        #delete from the set, if it's in the set
        #else raise key error
        if self.contains(element):
            self.tree.delete(element)
            self.size -= 1
        else:
            raise KeyError

    def union(self, other_set):
        #create a new set
        new_set = Set_Tree()
        #add everything from your set to new_set
        for element in self.tree.items_in_order():
            new_set.add(element)

        #then add everything from other_set to new_set
        for element in other_set.items_in_order():
            new_set.add(element)

    def intersection(self, other_set):
        pass

    def difference(self, other_set):
        pass

    def is_subset(self, other_set):
        pass
    

