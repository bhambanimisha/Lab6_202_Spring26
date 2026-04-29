import unittest

from lab6_1 import Node, search, insert, delete


class TestSearch(unittest.TestCase):
    def test_search_finds_existing_value(self):
        pass

    def test_search_returns_false_for_missing_value(self):
        pass

    def test_search_on_empty_tree(self):
        pass


class TestInsert(unittest.TestCase):
    def test_insert_into_empty_tree(self):
        pass

    def test_insert_new_value_in_correct_position(self):
        pass

    def test_insert_duplicate_returns_unchanged_tree(self):
        pass


class TestDelete(unittest.TestCase):
    def test_delete_leaf_node(self):
        pass
    def test_delete_node_with_one_child(self):
        pass

    def test_delete_node_with_two_children(self):
        pass

if __name__ == "__main__":
    unittest.main()