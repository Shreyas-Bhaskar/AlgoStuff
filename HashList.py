import re
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def delete(self, key):
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def increase(self, key):
        node = self.find(key)
        if node:
            node.value += 1
            return True
        return False

    def list_all_keys(self):
        keys = []
        current = self.head
        while current:
            keys.append(current.key)
            current = current.next
        return keys
    
    def delete(self, key):
        current = self.head
        previous = None

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next

        return False 
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash_function(self, key):
        hash_val = 0
        for char in key:
            hash_val = (hash_val * 31 + ord(char)) % self.size
        return hash_val

    def insert(self, key, value=1):
        index = self.hash_function(key)
        node = self.table[index].find(key)
        if node:
            node.value = value
        else:
            self.table[index].insert(key, value)

    def delete(self, key):
        index = self.hash_function(key)
        return self.table[index].delete(key)

    def increase(self, key):
        index = self.hash_function(key)
        return self.table[index].increase(key)

    def find(self, key):
        index = self.hash_function(key)
        node = self.table[index].find(key)
        return node.value if node else None

    def list_all_keys(self):
        keys = []
        for linked_list in self.table:
            keys.extend(linked_list.list_all_keys())
        return keys

    def list_lengths(self):
        return [lst.length() for lst in self.table]

def process_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return words

def count_words(text, hash_table_size):
    words = process_text(text)
    word_count_hash_table = HashTable(hash_table_size)

    for word in words:
        if word_count_hash_table.find(word):
            word_count_hash_table.increase(word)
        else:
            word_count_hash_table.insert(word)

    return word_count_hash_table

def save_word_counts(word_count_hash_table, output_file_path):
    with open(output_file_path, 'w') as file:
        for word in word_count_hash_table.list_all_keys():
            count = word_count_hash_table.find(word)
            file.write(f"{word}: {count}\n")

def calculate_variance(list_lengths):
    mean = sum(list_lengths) / len(list_lengths)
    squared_diffs = [(x - mean) ** 2 for x in list_lengths]
    variance = sum(squared_diffs) / len(list_lengths)
    return variance

def analyze_hash_table(hash_table, output_file_path):
    list_lengths = hash_table.list_lengths()
    variance = calculate_variance(list_lengths)
    histogram = {}
    for length in list_lengths:
        histogram[length] = histogram.get(length, 0) + 1
    sorted_histogram = sorted(histogram.items())
    sorted_lengths = sorted(list_lengths, reverse=True)
    top_10_percent_index = int(0.1 * len(sorted_lengths))
    longest_lists = sorted_lengths[:top_10_percent_index]
    with open(output_file_path, 'w') as file:
        file.write(f"Histogram of List Lengths:\n")
        for length, count in sorted_histogram:
            file.write(f"Length {length}: {'*' * count}\n")
        file.write(f"\nVariance of List Lengths: {variance}\n")
        file.write(f"Lengths of the Longest 10% of Lists: {longest_lists}\n")

    return variance, sorted_histogram, longest_lists

if __name__ == "__main__":
    input_file_path = "alice.txt"  
    output_file_path = "word_counts.txt"  
    hash_table_sizes = [30, 300, 1000]  

    try:
        with open(input_file_path, 'r') as file:
            alice_text = file.read()
        
        for size in hash_table_sizes:
            word_count_hash_table = count_words(alice_text, size)
            save_word_counts(word_count_hash_table, output_file_path)
            analyze_hash_table(word_count_hash_table,f"hash_table_analysis{size}.txt")
    
    except Exception as e:
        print(f"Error: {e}")