import json

# Load JSON data
with open('recipesAll.json', 'r') as file:
    recipes_data = json.load(file)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# modified hash table using chaining for difficulty filter
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.size = 0 
        self.table = [None] * capacity

    # hash function
    def _hash(self, key):
        return hash(key) % self.capacity

    def add(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:             # if true, create a new node with the key-value and
            self.table[index] = Node(key, value)  # and set it as the head of the list
            self.size += 1                       
        else:
            current = self.table[index]
            while current.next:  # iterate through the list till the last node is found 
                current = current.next
            current.next = Node(key, value) #create a new node and add it to the singly linked list
            self.size += 1

    #takes advantage of collision, all values sharing the same key are accessed 
    def findAndFilter(self, key):
        index = self._hash(key)
        indices_list = [] 
        current = self.table[index]
        while current:
            indices_list.append(current.value)
            current = current.next
        return indices_list #returns an indices list according to difficulty level

# create the hash table
difficulty_hash_table = HashTable(5) #capacity is set to 5 since difficulty range is from 1-5 only

# make difficulty levels as the keys and indices of the json file as the values
for index in range(len(recipes_data)): #iterate through the file and add elements to the table
    difficulty_hash_table.add(recipes_data[index]["difficulty"], index)


#`````````````for modification```````````````

# difficulty filter input
filter_input = int(input("Enter difficulty: ")) 
indices_list = difficulty_hash_table.findAndFilter(filter_input) #final indices list for difficulty filter
print(indices_list)
#````````````````````````````````````````````


