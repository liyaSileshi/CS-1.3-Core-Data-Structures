from binarytree import BinarySearchTree

class Set_Tree(object):
    def __init__(self, elements=None):
        self.tree = BinarySearchTree()
        self.size = 0
        if elements is not None:
            for element in elements:
                self.add(element)

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'Set_Tree({!r})'.format(self.tree.items_in_order())

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
        for element in other_set.tree.items_in_order():
            new_set.add(element)
        print(new_set.tree.items_in_order())
        return new_set

    def intersection(self, other_set):
        #create new set
        new_set = Set_Tree()
        set1 = self.tree.items_in_order()
        set2 = other_set.tree.items_in_order()
        #for item in set1
        #if it's in set2, add it to the new_set
        for item in set1:
            if item in set2:
                new_set.add(item)
        # print(new_set.tree.items_in_order())
        return new_set
       

    def difference(self, other_set):
        #create a new set
        new_set = Set_Tree()
        set1 = self.tree.items_in_order()
        set2 = other_set.tree.items_in_order()
        #if item is in set1 but not in set2, add it
        for item in set1:
            if item not in set2:
                new_set.add(item)
        return new_set

    def is_subset(self, other_set):
        set1 = self.tree.items_in_order()
        set2 = other_set.tree.items_in_order()
        for element in set2:
            if element in set1:
                continue #continue looping
            else:
                return False #not all element of set2 are in set1
        return True #finished the loop, all elements are in set1

if __name__ == '__main__':
    set_tree1 = Set_Tree([1,2,3,4])
    set_tree2 = Set_Tree([1,2,3])
    new_set = set_tree1.difference(set_tree2)
    # print(new_set.tree.items_in_order())
    # assert new_set.tree.items_in_order() == [2, 3]
    print(set_tree1.is_subset(set_tree2))