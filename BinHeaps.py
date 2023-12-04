import random

class BinomialTreeNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

class BinomialHeap:
    def __init__(self):
        self.head = None

    def link_trees(self, node1, node2):
        node1.parent = node2
        node1.sibling = node2.child
        node2.child = node1
        node2.degree += 1

    def merge(self, other):
        dummy = BinomialTreeNode(0)
        tail = dummy
        x = self.head
        y = other.head

        while x is not None and y is not None:
            if x.degree <= y.degree:
                tail.sibling = x
                x = x.sibling
            else:
                tail.sibling = y
                y = y.sibling
            tail = tail.sibling

        tail.sibling = x if x is not None else y
        return dummy.sibling

    def union(self, other):
        new_heap = BinomialHeap()
        new_heap.head = self.merge(other)

        if new_heap.head is None:
            return new_heap

        prev_x = None
        x = new_heap.head
        next_x = x.sibling

        while next_x is not None:
            if x.degree != next_x.degree or (next_x.sibling is not None and next_x.sibling.degree == x.degree):
                prev_x = x
                x = next_x
            else:
                if x.key <= next_x.key:
                    x.sibling = next_x.sibling
                    self.link_trees(next_x, x)
                else:
                    if prev_x is None:
                        new_heap.head = next_x
                    else:
                        prev_x.sibling = next_x
                    self.link_trees(x, next_x)
                    x = next_x
            next_x = x.sibling

        return new_heap

    def insert(self, key):
        node = BinomialTreeNode(key)
        new_heap = BinomialHeap()
        new_heap.head = node
        self.head = self.union(new_heap).head

    def minimum(self):
        if self.head is None:
            return None

        y = None
        x = self.head
        min_val = float('inf')

        while x is not None:
            if x.key < min_val:
                min_val = x.key
                y = x
            x = x.sibling

        return y.key

    def extract_min(self):
        if self.head is None:
            return None

        min_tree_parent = None
        min_tree = self.head
        prev = None
        curr = self.head

        while curr is not None:
            if curr.key == float('-inf'):
                min_tree = curr
                min_tree_parent = prev
                break
            elif curr.key < min_tree.key:
                min_tree = curr
                min_tree_parent = prev
            prev = curr
            curr = curr.sibling

        if min_tree_parent is not None:
            min_tree_parent.sibling = min_tree.sibling
        else:
            self.head = min_tree.sibling

        child = min_tree.child
        temp = BinomialHeap()
        while child is not None:
            next_child = child.sibling
            child.sibling = temp.head
            temp.head = child
            child = next_child

        self.head = self.union(temp).head
        return min_tree.key

    def extract_minx(self):
        min_tree_parent = None
        min_tree = self.head
        prev = None
        curr = self.head
        if curr.key == float('-inf'):
            min_tree = curr
        else:
            while curr.sibling is not None:
                if curr.sibling.key < min_tree.key:
                    min_tree = curr.sibling
                    min_tree_parent = prev
                prev = curr
                curr = curr.sibling

        if min_tree_parent is not None:
            min_tree_parent.sibling = min_tree.sibling
        else:
            self.head = min_tree.sibling

        child = min_tree.child
        temp = BinomialHeap()

        while child is not None:
            next_child = child.sibling
            child.sibling = temp.head
            temp.head = child
            child = next_child

        self.head = self.union(temp).head
        return min_tree.key
    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        node.key = new_key
        self._bubble_up(node)

    def _bubble_up(self, node):
        while node.parent and node.key < node.parent.key:
            node.key, node.parent.key = node.parent.key, node.key
            node = node.parent

    def decrease_keyx(self, x, new_key):
        if new_key > x.key:
            raise ValueError("New key is greater than current key")

        x.key = new_key
        parent = x.parent

        while parent is not None and x.key < parent.key:
            x.key, parent.key = parent.key, x.key
            node = parent
            parent = parent.parent

    def delete(self, x):
        self.decrease_key(x, float('-inf'))
        self.extract_min()

    #def print_heap(self):
        node = self.head
        while node is not None:
            self.print_tree(node)
            node = node.sibling

    #def print_tree(self, node, level=0):
        if node is None:
            return
        print(" " * (level * 4) + f"Key: {node.key}, Degree: {node.degree}")
        self.print_tree(node.child, level + 1)

    def print_heap(self):
        node = self.head
        while node is not None:
            self.print_tree(node)
            node = node.sibling

    def print_tree(self, node, level=0):
        if node is None:
            return
        print(" " * (level * 4) + f"Key: {node.key}, Degree: {node.degree}")
        child = node.child
        while child is not None:
            self.print_tree(child, level + 1)
            child = child.sibling
    

    def search(self, key, node):
        if node is None:
            return None
        if node.key == key:
            return node

        found = self.search(key, node.child)
        if found is not None:
            return found

        return self.search(key, node.sibling)
    def find_node(self, key):
        current = self.head
        while current is not None:
            found = self.search(key, current)
            if found is not None:
                return found
            current = current.sibling
        return None

binomial_heap = BinomialHeap()
keys = [7,2,4,17,1,11,6,8,15,10,20,5]
#[4,6,3,11,9,5,14,10,21,7,13,20,2]
for key in keys:
    binomial_heap.insert(key)
    binomial_heap.print_heap()
    print()
#print("deleting 5")

node_to_delete = None
current_node = binomial_heap.head
print("\n")

while current_node is not None:
    print(current_node.key)
    if current_node.key == 5:
        node_to_delete = current_node
        break
    current_node = current_node.sibling
print("\n")

#if node_to_delete is not None:
   # print(f"Deleted key {node_to_delete.key}")
    #binomial_heap.delete(node_to_delete)
#else:
    #print("Key not found in the heap")

binomial_heap.print_heap()
print("\n")


min_key = binomial_heap.minimum()
print(f"Minimum key: {min_key}")
print("\n")

extracted_key = binomial_heap.extract_min()
print(f"Extracted key: {extracted_key}")
binomial_heap.print_heap()
print("\n")


node_to_decrease = binomial_heap.find_node(15)
print(f"decreased key: {node_to_decrease.key}")
print("\n")
binomial_heap.decrease_key(node_to_decrease, 1)
binomial_heap.print_heap()

node_to_delete = binomial_heap.find_node(1)
print(f"deleted key: {node_to_delete.key}")
binomial_heap.delete(node_to_delete)

