from set_tree import Set_Tree
import unittest

class SetTreeTest(unittest.TestCase):

    def test_init(self):
        elements = [2, 4, 3, 1, 5]
        set_tree = Set_Tree(elements)
        assert set_tree.size == 5
        elements2 = []
        set_tree2 = Set_Tree(elements2)
        assert set_tree2.size == 0

    def test_size(self):
        set_tree = Set_Tree()
        assert set_tree.size == 0
        set_tree.add('B')
        assert set_tree.size == 1
        assert set_tree.contains('B') == True
        set_tree.add('A')
        assert set_tree.size == 2
        set_tree.add('B') #B is already in the set
        assert set_tree.size == 2
        set_tree.add('D')
        assert set_tree.size == 3

    def test_contains(self):
        set_tree = Set_Tree()
        set_tree.add('B')
        assert set_tree.contains('B') == True
        assert set_tree.contains('A') == False
        assert set_tree.size == 1
        set_tree.add('A')
        assert set_tree.contains('A') == True

    def test_add(self):
        set_tree = Set_Tree()
        assert set_tree.contains('B') == False
        set_tree.add('B')
        assert set_tree.contains('B') == True
        assert set_tree.tree.items_in_order() == ['B']
        set_tree.add('B') #won't be added
        assert set_tree.tree.items_in_order() == ['B']
        set_tree.add('C')
        assert set_tree.contains('C') == True
        assert set_tree.tree.items_in_order() == ['B', 'C']

    def test_remove(self):
        set_tree = Set_Tree()
        assert set_tree.contains('B') == False
        set_tree.add('B')
        assert set_tree.contains('B') == True
        assert set_tree.tree.items_in_order() == ['B']
        set_tree.remove('B')
        assert set_tree.contains('B') == False
        assert set_tree.tree.items_in_order() == []
        set_tree.add('C')
        assert set_tree.contains('C') == True
        assert set_tree.tree.items_in_order() == ['C']

    def test_union(self):
        set_tree1 = Set_Tree([1,2,3])
        set_tree2 = Set_Tree([4,5,6])
        new_set = set_tree1.union(set_tree2)
        assert new_set.tree.items_in_order() == [1, 2, 3, 4, 5, 6]
        set_tree3 = Set_Tree([2,3,4,6])
        new_set2 = set_tree1.union(set_tree3)
        assert new_set2.tree.items_in_order() == [1, 2, 3, 4, 6]
        set_tree4 = Set_Tree()
        new_set3 = set_tree1.union(set_tree4)
        assert new_set3.tree.items_in_order() == [1, 2, 3]

    def test_intersection(self):
        set_tree1 = Set_Tree([1,2,3])
        set_tree2 = Set_Tree([2,3,6,7])
        new_set = set_tree1.intersection(set_tree2)
        assert new_set.tree.items_in_order() == [2, 3]
        set_tree3 = Set_Tree([4,5,6])
        new_set2 = set_tree1.intersection(set_tree3)
        assert new_set2.tree.items_in_order() == [] #no items in common
        set_tree4 = Set_Tree()
        new_set3 = set_tree1.intersection(set_tree4)
        assert new_set3.tree.items_in_order() == [] #no items in common

    def test_difference(self):
        set_tree1 = Set_Tree([1,2,3])
        set_tree2 = Set_Tree([2,3,6,7])
        new_set = set_tree1.difference(set_tree2)
        assert new_set.tree.items_in_order() == [1]
        set_tree3 = Set_Tree([2,1, 3])
        new_set2 = set_tree1.difference(set_tree3)
        assert new_set2.tree.items_in_order() == [] #all items are similar
        set_tree4 = Set_Tree()
        new_set3 = set_tree1.difference(set_tree4)
        assert new_set3.tree.items_in_order() == [1,2,3] #no items in set4

    def test_subset(self):
        set_tree1 = Set_Tree([1,2,3,4])
        set_tree2 = Set_Tree([1,2,3])
        assert set_tree1.is_subset(set_tree2) == True
        set_tree3 = Set_Tree([])
        assert set_tree1.is_subset(set_tree3) == True #empty set is a subset of all sets
        set_tree4 = Set_Tree([1,2,3,5])
        assert set_tree1.is_subset(set_tree4) == False

if __name__ == '__main__':
    unittest.main()
