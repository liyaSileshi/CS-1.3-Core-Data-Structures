from set_tree import Set_Tree
import unittest

class SetTreeTest(unittest.TestCase):

    def test_init(self):
        elements = [2, 4, 3, 1, 5]
        set_tree = Set_Tree(elements)
        assert set_tree.size == 5

    def test_size(self):
        set_tree = Set_Tree()
        assert set_tree.size == 0
        set_tree.add('B')
        assert set_tree.size == 1
        set_tree.add('A')
        assert set_tree.size == 2
        set_tree.add('B') #B is already in the set
        assert set_tree.size == 2
        set_tree.add('D')
        assert set_tree.size == 3

     
if __name__ == '__main__':
    unittest.main()
