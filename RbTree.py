from sys import stdout

class Node:
    def __init__(self, key, color="RED"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color="BLACK")
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def rb_insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == self.NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        node.color = "RED"
        self.insert_fixup(node)

    def search(self, key):
        
        node = self.root
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node
    def insert_fixup(self, z):
        while z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right 
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)
        self.root.color = "BLACK"
    def tree_minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def tree_maximum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node

    def tree_successor(self, node):
        if node.right != self.NIL:
            return self.tree_minimum(node.right)
        y = node.parent
        while y != self.NIL and node == y.right:
            node = y
            y = y.parent
        return y

    def tree_predecessor(self, node):
        if node.left != self.NIL:
            return self.tree_maximum(node.left)
        y = node.parent
        while y != self.NIL and node == y.left:
            node = y
            y = y.parent
        return y

    def rb_transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def rb_delete_fixup(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = "BLACK"

    def rb_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self.rb_delete_fixup(x)

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)

    def height(self, node):
        if node == self.NIL:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def print_tree(self, node, indent="", last='updown'):
        if node != self.NIL:
            stdout.write(indent)
            if last == 'updown':
                stdout.write("Root----")
                indent += "     "
            elif last == 'right':
                stdout.write("R----")
                indent += "|    "
            else:
                stdout.write("L----")
                indent += "     "
        
            color = "RED" if node.color == "RED" else "BLACK"
            print(f"{node.key}({color})")
            self.print_tree(node.left, indent, last='right')
            self.print_tree(node.right, indent, last='left')


def read_input_file(filename):
    with open(filename, "r") as file:
        return [int(x) for x in file.read().split()]

def main():
    #filename = input("Enter the filename: ")
    numbers = [7,4,2]
    #[50,30,70,20,40,60,80,15,25,35,45,55,65,75,85]
    #read_input_file(filename)

    rb_tree = RedBlackTree()
    for num in numbers:
        rb_tree.rb_insert(num)

    while True:
        command = input("\nEnter command (insert x/sort/search x/min/max/successor x/predecessor x/delete x/exit): ").split()
        if command[0] == "exit":
            break
        elif command[0] == "insert":
            rb_tree.rb_insert(int(command[1]))
        elif command[0] == "sort":
            rb_tree.inorder_traversal(rb_tree.root)
        elif command[0] == "search":
            node = rb_tree.search(int(command[1]))
            if node != rb_tree.NIL:
                print("Found:", node.key)
            else:
                print("Not found")
        elif command[0] == "min":
            min_node = rb_tree.tree_minimum(rb_tree.root)
            if min_node != rb_tree.NIL:
                print("Minimum:", min_node.key)
            else:
                print("Tree is empty")
        elif command[0] == "max":
            max_node = rb_tree.tree_maximum(rb_tree.root)
            if max_node != rb_tree.NIL:
                print("Maximum:", max_node.key)
            else:
                print("Tree is empty")
        elif command[0] == "successor":
            node = rb_tree.search(int(command[1]))
            if node != rb_tree.NIL:
                succ = rb_tree.tree_successor(node)
                if succ != rb_tree.NIL:
                    print("Successor:", succ.key)
                else:
                    print("No successor found")
            else:
                print("Node not found")
        elif command[0] == "predecessor":
            node = rb_tree.search(int(command[1]))
            if node != rb_tree.NIL:
                pred = rb_tree.tree_predecessor(node)
                if pred != rb_tree.NIL:
                    print("Predecessor:", pred.key)
                else:
                    print("No predecessor found")
            else:
                print("Node not found")
        elif command[0] == "delete":
            node = rb_tree.search(int(command[1]))
            if node != rb_tree.NIL:
                rb_tree.rb_delete(node)
                print("Deleted:", int(command[1]))
            else:
                print("Node not found to delete")

        rb_tree.print_tree(rb_tree.root)
        print("\nHeight of the tree:", rb_tree.height(rb_tree.root))

if __name__ == "__main__":
    main()