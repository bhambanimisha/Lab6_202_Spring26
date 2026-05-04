import unittest

from lab6_1 import Node, search, insert, delete


class TestSearch(unittest.TestCase):
    def test_search_finds_existing_value(self):
        tree = Node(
            8,
            Node(
                3,
                Node(1),
                Node(6)
            ),
            Node(
                10,
                None,
                Node(14)
            )
        )
        self.assertEqual(search(tree, 1), True)
        pass

    def test_search_returns_false_for_missing_value(self):
        tree = Node(
            8,
            Node(
                3,
                Node(1),
                Node(6)
            ),
            Node(
                10,
                None,
                Node(14)
            )
        )
        self.assertEqual(search(tree, 5), False)
        pass

    def test_search_on_empty_tree(self):
        tree = None
        self.assertEqual(search(tree, 4), False)
        pass


class TestInsert(unittest.TestCase):
    def test_insert_into_empty_tree(self):
        tree = None
        result = insert(tree, 3)
        self.assertEqual(result, Node(3))
        pass

    def test_insert_new_value_in_correct_position(self):
        tree = Node(
            8,
            Node(
                3,
                Node(1),
                Node(6)
            ),
            Node(
                10,
                None,
                Node(14)
            )
        )
        result = insert(tree, 5)
        self.assertEqual(result.left.right.left, Node(5))
        pass

    def test_insert_duplicate_returns_unchanged_tree(self):
        tree = Node(
            8,
            Node(
                3,
                Node(1),
                Node(6)
            ),
            Node(
                10,
                None,
                Node(14)
            )
        )
        result = insert(tree, 3)
        self.assertEqual(result, tree)
        pass


class TestDelete(unittest.TestCase):
    def test_delete_leaf_node(self):
        tree = Node(
            8,
            Node(
                3,
                Node(1),
                Node(6)
            ),
            Node(
                10,
                None,
                Node(14)
            )
        )
        result = delete(tree, 1)
        self.assertEqual(result.left.left, None)
        pass
    def test_delete_node_with_one_child(self):
        tree = Node(
            8,
            Node(
                3,
                Node(1),
                Node(6)
            ),
            Node(
                10,
                None,
                Node(14)
            )
        )
        result = delete(tree, 10)
        self.assertEqual(result.right.val, 14)
        pass

    def test_delete_node_with_two_children(self):
        tree = Node(
            8,
            Node(
                3,
                Node(1),
                Node(6)
            ),
            Node(
                10,
                None,
                Node(14)
            )
        )
        result = delete(tree, 3)
        self.assertEqual(result.left.val, 6)
        pass

if __name__ == "__main__":
    unittest.main()
