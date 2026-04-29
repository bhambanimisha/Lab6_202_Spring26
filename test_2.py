import unittest

from lab6_2 import Node, preorder, inorder, postorder, bfs


class TestDFSAndBFS(unittest.TestCase):
    def setUp(self):
        self.tree = Node(
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

    def test_preorder_empty_tree(self):
        self.assertEqual(preorder(None), [])

    def test_preorder_nonempty_tree(self):
        self.assertEqual(preorder(self.tree), [8, 3, 1, 6, 10, 14])

    def test_inorder_empty_tree(self):
        self.assertEqual(inorder(None), [])

    def test_inorder_nonempty_tree(self):
        self.assertEqual(inorder(self.tree), [1, 3, 6, 8, 10, 14])

    def test_postorder_empty_tree(self):
        self.assertEqual(postorder(None), [])

    def test_postorder_nonempty_tree(self):
        self.assertEqual(postorder(self.tree), [1, 6, 3, 14, 10, 8])

    def test_bfs_empty_tree(self):
        self.assertEqual(bfs(None), [])

    def test_bfs_nonempty_tree(self):
        self.assertEqual(bfs(self.tree), [8, 3, 10, 1, 6, 14])

    def test_bfs_single_node(self):
        self.assertEqual(bfs(Node(42)), [42])


if __name__ == "__main__":
    unittest.main()