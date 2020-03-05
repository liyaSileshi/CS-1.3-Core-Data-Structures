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

    def __iter__(self):
        for item in self.tree.items_in_order():
            yield item

    def contains(self, element):
        '''
        Return true if this set contains the given element, False otherwise
        Time complexity: O(logn)
        Space complexity: O(logn) if recursive, O(1) if iterative
        '''
        return self.tree.contains(element)

    def add(self, element):
        '''
        Adds element to a set if it's not already in the set
        Time complexity: O(logn).O(logn)
        Space complexity: O(1)
        '''
        #if the element is not already in the set, insert it
        if not self.contains(element): #O(logn)
            self.tree.insert(element)   #O(logn)
            self.size += 1

    def remove(self, element): 
        '''
        Removes the element from the set, if it exists
        Time complexity: O(n) + O(logn) = O(n)
        Space complexity: O(n) getting the inorder item to find successor
        '''
        #delete from the set, if it's in the set
        #else raise key error
        if self.contains(element): #O(1)
            self.tree.delete(element) #O(n)
            self.size -= 1
        else:
            raise KeyError

    def union(self, other_set):
        '''
        Return a new set that is the union of this set and other_set
        Time complexity: O(mlogm) + O(nlogn)
        Space complexity: O(m+n)
        '''
        #create a new set with items of self
        new_set = Set_Tree(self) #O(mlogm)
        #then add everything from other_set to new_set
        for element in other_set: #O(n)
            new_set.add(element) #O(logn)
        return new_set

    def intersection(self, other_set):
        '''
        Return a new set that is the intersection of this set and other_set
        Time complexity: O(mlogn).O(mlog(min(m,n)))
        Space complexity: O(log(min(m,n)))
        '''
        #create new set
        new_set = Set_Tree() #O(1)
        ##########check to see which one is smaller####
        #for item in set1
        #if it's in set2, add it to the new_set
        for item in self: #O(m)
            if other_set.contains(item): #O(logn)
                new_set.add(item) #O(log(min(m,n)))
        return new_set
       
    def difference(self, other_set):
        '''
        Return a new set that is the difference of this set and other_set
        Time complexity: O(mlog(mn))
        Space complexity: O(log(min(m,n)))
        '''
        #create a new set
        new_set = Set_Tree()
        #if item is in set1 but not in set2, add it
        for item in self: #O(m)
            if not other_set.contains(item):#O(logn) #if other set doesn't contain item O(logn)
                new_set.add(item) #O(1)
        return new_set

    def is_subset(self, other_set):
        '''
        Return a boolean indicating whether other_set is a subset of this set
        Time complexity: O(nlogm)
        Space complexity: O(n)
        '''
        if other_set.size > self.size: #it can't be a subset if it has more items
            return False
        for element in other_set: #O(n)
            if not self.contains(element): #O(logm)
                return False #not all element of set2 are in set1
        return True #finished the loop, all elements are in set1
        # return other_set.difference(self).tree.items_in_order() == []

if __name__ == '__main__':
    set_tree1 = Set_Tree([1,2,3,4])
    set_tree2 = Set_Tree([1,2,3])
    # new_set = set_tree1.difference(set_tree2)
    # print(new_set.tree.items_in_order())
    # assert new_set.tree.items_in_order() == [2, 3]
    # print(set_tree1.is_subset(set_tree2))
