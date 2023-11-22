import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.header = Node(-1, max_level)

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.max_level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if not current or current.value != value:
            random_level = self.random_level()
            new_node = Node(value, random_level)
            for i in range(random_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def display(self):
        print("Skip List Structure:")
        for i in range(self.max_level + 1):
            print(f"Level {i}: ", end="")
            node = self.header.forward[i]
            while node:
                print(node.value, end=" ")
                node = node.forward[i]
            print()

    def delete(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.max_level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.value == value:
            for i in range(len(current.forward)):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            print(f"Value {value} deleted")

    def lookup(self, value):
        print(f"Lookup for value: {value}")
        current = self.header
        for i in range(self.max_level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                print(f"Moving right at level {i}, from value {current.value} to {current.forward[i].value}")
                current = current.forward[i]
            if current.forward[i] and current.forward[i].value == value:
                print(f"Value {value} found at level {i}")
                return True
            print(f"Moving down from level {i} to level {i-1}")
        print(f"Value {value} not found")
        return False
def main():
    skip_list = SkipList(max_level=5)

    while True:
        operation = input("Enter operation (insert, delete, lookup) and value, or 'exit' to stop: ").split()

        if operation[0] == 'exit':
            break

        op, val = operation[0], int(operation[1])

        if op == 'insert':
            skip_list.insert(val)
        elif op == 'delete':
            skip_list.delete(val)
        elif op == 'lookup':
            skip_list.lookup(val)
        skip_list.display()

if __name__ == "__main__":
    main()
