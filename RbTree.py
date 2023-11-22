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

    def bst_delete(self, z):
        pass

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
    filename = input("Enter the filename: ")
    numbers = read_input_file(filename)

    rb_tree = RedBlackTree()
    for num in numbers:
        rb_tree.rb_insert(num)

    while True:
        command = input("\nEnter command (insert x/sort/search x/exit): ").split()
        if command[0] == "exit":
            break
        elif command[0] == "insert":
            rb_tree.rb_insert(int(command[1]))
        elif command[0] == "sort":
            rb_tree.inorder_traversal(rb_tree.root)
        elif command[0] == "search":
            node = rb_tree.search(int(command[1]))
            if node != rb_tree.NIL:
                print("Found")
            else:
                print("Not found")
        rb_tree.print_tree(rb_tree.root)
        print("\nHeight of the tree:", rb_tree.height(rb_tree.root))

if __name__ == "__main__":
    main()
