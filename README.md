# Binary Tree Operations Using Python

## Aim
To implement a binary tree in Python and perform operations such as finding the minimum element, maximum element, calculating the sum of all elements, and performing preorder, inorder, and postorder traversals.

## Description
This program implements a binary tree using Python classes and object-oriented programming concepts. Each node stores a data value and references to its left and right child nodes.

The program generates 10 random integers between 1 and 100 and inserts them into the tree level by level using a queue. It then performs various operations, including finding the minimum and maximum elements, calculating the sum of all elements, and displaying the elements using three tree traversal techniques.

## Features
- Creates a binary tree using Python classes.
- Inserts 10 randomly generated integers.
- Finds the minimum element in the tree.
- Finds the maximum element in the tree.
- Calculates the sum of all elements.
- Performs preorder traversal.
- Performs inorder traversal.
- Performs postorder traversal.
- Uses recursion to process tree nodes.
- Displays the results in the terminal.

## Technologies Used
- Python 3
- Random Module
- Object-Oriented Programming
- Recursion
- Queue
- Binary Tree Data Structure

## Complete Python Code

```python
import random

class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class FullBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TNode(data)
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if not current.left:
                current.left = TNode(data)
                break

            elif not current.right:
                current.right = TNode(data)
                break

            else:
                queue.append(current.left)
                queue.append(current.right)

    def find_min(self):
        return min(self.in_order()) if self.root else None

    def find_max(self):
        return max(self.in_order()) if self.root else None

    def cal_sum(self):
        return self._calculate_sum(self.root)

    def _calculate_sum(self, node):
        if not node:
            return 0

        return (
            node.data
            + self._calculate_sum(node.left)
            + self._calculate_sum(node.right)
        )

    def pre_order(self):
        traversal = []
        self._pre_order_traversal(self.root, traversal)
        return traversal

    def _pre_order_traversal(self, node, traversal):
        if node:
            traversal.append(node.data)
            self._pre_order_traversal(node.left, traversal)
            self._pre_order_traversal(node.right, traversal)

    def post_order(self):
        traversal = []
        self._post_order_traversal(self.root, traversal)
        return traversal

    def _post_order_traversal(self, node, traversal):
        if node:
            self._post_order_traversal(node.left, traversal)
            self._post_order_traversal(node.right, traversal)
            traversal.append(node.data)

    def in_order(self):
        traversal = []
        self._in_order_traversal(self.root, traversal)
        return traversal

    def _in_order_traversal(self, node, traversal):
        if node:
            self._in_order_traversal(node.left, traversal)
            traversal.append(node.data)
            self._in_order_traversal(node.right, traversal)


# Main program
tree = FullBinaryTree()

for _ in range(10):
    data = random.randint(1, 100)
    tree.insert(data)

print("Minimum element:", tree.find_min())
print("Maximum element:", tree.find_max())
print("Sum of elements is:", tree.cal_sum())
print("Pre order traversal is:", tree.pre_order())
print("Post order traversal is:", tree.post_order())
print("In order traversal is:", tree.in_order())
```

## Concepts Used

### 1. Binary Tree
A binary tree is a hierarchical data structure in which each node can have at most two children: a left child and a right child.

### 2. Node
The `TNode` class represents a node. Each node contains:
- `data`: Stores the value.
- `left`: Stores the reference to the left child.
- `right`: Stores the reference to the right child.

### 3. Insertion
The `insert()` method inserts new nodes level by level using a queue. It fills the left child position first and then the right child position.

### 4. Finding the Minimum Element
The `find_min()` method finds the smallest element in the tree using the inorder traversal result and Python's `min()` function.

### 5. Finding the Maximum Element
The `find_max()` method finds the largest element in the tree using the inorder traversal result and Python's `max()` function.

### 6. Calculating the Sum
The `cal_sum()` method calls `_calculate_sum()`, which recursively adds the values of the current node, left subtree, and right subtree.

### 7. Preorder Traversal
Preorder traversal visits nodes in the following order:

**Root → Left → Right**

### 8. Inorder Traversal
Inorder traversal visits nodes in the following order:

**Left → Root → Right**

### 9. Postorder Traversal
Postorder traversal visits nodes in the following order:

**Left → Right → Root**

## Algorithm

1. Start the program.
2. Import the `random` module.
3. Define the `TNode` class to create tree nodes.
4. Define the `FullBinaryTree` class and initialize the root as `None`.
5. Insert 10 random integers between 1 and 100 into the tree using level-order insertion.
6. Find the minimum element using inorder traversal.
7. Find the maximum element using inorder traversal.
8. Calculate the sum of all elements using recursion.
9. Perform preorder traversal.
10. Perform postorder traversal.
11. Perform inorder traversal.
12. Display all the results.
13. Stop the program.

## How the Program Works

1. The `random` module generates random integers between 1 and 100.
2. The `TNode` class creates individual nodes.
3. The `FullBinaryTree` class manages the tree operations.
4. A queue helps insert nodes level by level.
5. The `find_min()` method identifies the smallest value.
6. The `find_max()` method identifies the largest value.
7. The `cal_sum()` method calculates the total of all node values.
8. The traversal methods visit the nodes in different orders.
9. The results are displayed using `print()` statements.

## Sample Output

The program generates random numbers, so the output varies each time.

```text
Minimum element: 12
Maximum element: 90
Sum of elements is: 456
Pre order traversal is: [45, 23, 12, 34, 67, 56, 78, 90, 89, 57]
Post order traversal is: [12, 34, 23, 56, 57, 89, 90, 78, 67, 45]
In order traversal is: [12, 23, 34, 45, 56, 57, 67, 78, 89, 90]
```

**Note:** The above output is only an illustration. The actual output will depend on the randomly generated numbers. The sum, minimum, maximum, and traversals must match the same set of numbers.

## How to Run the Program

### Prerequisites
- Python 3 installed on your computer.
- A code editor such as VS Code or IDLE.

### Execution Steps

1. Save the Python program in a file named `binary_tree.py`.
2. Open Command Prompt or a terminal.
3. Navigate to the folder containing the file.
4. Run the following command:

```bash
python binary_tree.py
```

5. The output will display the minimum element, maximum element, sum, and all three tree traversals.

## Time Complexity

Let `n` represent the number of nodes in the tree.

| Operation | Time Complexity |
|---|---|
| Insertion | O(n) worst case per insertion |
| Find Minimum | O(n) |
| Find Maximum | O(n) |
| Calculate Sum | O(n) |
| Preorder Traversal | O(n) |
| Inorder Traversal | O(n) |
| Postorder Traversal | O(n) |

### Space Complexity
- **Tree Storage:** O(n)
- **Traversal Storage:** O(n)
- **Recursive Call Stack:** O(h), where `h` is the height of the tree.
- **Insertion Queue:** O(n) in the worst case.

## Applications
- Learning binary tree data structures.
- Understanding recursion.
- Practicing tree traversal algorithms.
- Finding minimum and maximum values.
- Calculating the sum of tree elements.
- Understanding queue-based insertion.
- Learning object-oriented programming in Python.
- Practicing fundamental data structures and algorithms.

## Advantages
- Demonstrates multiple binary tree operations in one program.
- Uses classes to organize the code.
- Uses recursion for tree processing.
- Supports three standard tree traversal techniques.
- Automatically generates test data.
- Helps understand hierarchical data structures.

## Limitations
- The program uses randomly generated data, so results change between executions.
- The tree does not provide a search-based insertion method like a Binary Search Tree.
- Finding the minimum and maximum requires visiting all nodes.
- The recursive methods may encounter recursion-depth limitations for sufficiently deep trees.

## Important Note
Although the class is named `FullBinaryTree`, its insertion method actually constructs a **complete binary tree**.

- **Full Binary Tree:** Every node has either zero or two children.
- **Complete Binary Tree:** Every level is filled except possibly the last, which is filled from left to right.

Renaming the class to `CompleteBinaryTree` would make its name more accurate. If you rename the class, update the object creation statement accordingly.

## Conclusion
This program demonstrates the implementation of a binary tree using Python. It performs insertion, minimum and maximum element identification, sum calculation, and preorder, inorder, and postorder traversals. It provides practical experience with recursion, queues, classes, and fundamental tree operations.

## Author
Python Programming Practical
