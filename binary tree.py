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
    
            
            
        
              