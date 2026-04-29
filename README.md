# Lab 6: Binary Search Trees

## Course

**CS 202**

## Title

**Lab 6: Binary Search Tree Operations and Breadth-First Search**

## Objective

In this lab, you will work with binary search trees implemented using immutable nodes. You will implement core BST operations and a breadth-first traversal.

---

## Day 1: BST Operations

You are given a binary search tree node defined as a frozen dataclass:

```python
@dataclass(frozen=True)
class Node:
    val: int
    left: Optional["Node"]
    right: Optional["Node"]
```

Because the dataclass is frozen, you may not modify an existing node after it is created. Your functions must return updated trees as needed.

### Tasks

Implement the following functions:

* `search(tree, x)`
* `insert(tree, x)`
* `delete(tree, x)`

### Requirements

#### `search(tree, x)`

Return whether `x` exists in the binary search tree.

#### `insert(tree, x)`

Insert `x` into the binary search tree and return the updated tree.

#### `delete(tree, x)`

Delete `x` from the binary search tree and return the updated tree.

### Testing

Write **3 unit test cases for each function**:

* 3 tests for `search`
* 3 tests for `insert`
* 3 tests for `delete`

---

## Day 2: Breadth-First Search

You have been given implementations of the following depth-first traversals:

* preorder DFS
* postorder DFS
* inorder DFS

Each function returns a list representing the traversal order.

### Task

Implement:

* `bfs(tree)`

Your BFS function should return a list of values in level-order traversal.

### Queue Rule

For this task, you may use a Python list as a queue:

* use `q.append(x)` to enqueue
* use `q.pop(0)` to dequeue


